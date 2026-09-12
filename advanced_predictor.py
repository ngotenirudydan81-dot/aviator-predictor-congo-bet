"""Advanced ML predictor using technical analysis"""
import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from typing import Dict, Tuple, List
import joblib
import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TechnicalAnalyzer:
    """Technical analysis on Aviator game data"""
    
    @staticmethod
    def calculate_sma(data: List[float], period: int = 20) -> List[float]:
        return pd.Series(data).rolling(window=period).mean().tolist()
    
    @staticmethod
    def calculate_ema(data: List[float], period: int = 20) -> List[float]:
        return pd.Series(data).ewm(span=period).mean().tolist()
    
    @staticmethod
    def calculate_rsi(data: List[float], period: int = 14) -> List[float]:
        deltas = np.diff(data)
        seed = deltas[:period+1]
        up = seed[seed >= 0].sum() / period
        down = -seed[seed < 0].sum() / period
        rs = up / down if down != 0 else 0
        rsi = [100 - 100 / (1 + rs)]
        
        for delta in deltas[period:]:
            up = (up * (period - 1) + (delta if delta > 0 else 0)) / period
            down = (down * (period - 1) + (-delta if delta < 0 else 0)) / period
            rs = up / down if down != 0 else 0
            rsi.append(100 - 100 / (1 + rs))
        
        return rsi
    
    @staticmethod
    def calculate_volatility(data: List[float], period: int = 20) -> List[float]:
        return pd.Series(data).rolling(window=period).std().tolist()

class AdvancedPredictor:
    """Advanced ML predictor for Aviator"""
    
    def __init__(self):
        self.crash_classifier = None
        self.multiplier_regressor = None
        self.scaler = StandardScaler()
        self.analyzer = TechnicalAnalyzer()
        self.feature_names = []
        self.model_path = 'models/advanced_predictor.pkl'
        self.scaler_path = 'models/advanced_scaler.pkl'
        self.load_or_train()
    
    def extract_features(self, games: List[Dict]) -> np.ndarray:
        if not games or len(games) < 30:
            return None
        
        multipliers = [g['multiplier'] for g in games]
        crashed = [1 if g['crashed'] else 0 for g in games]
        durations = [g['duration'] for g in games]
        
        sma_20 = self.analyzer.calculate_sma(multipliers, 20)[-1] or np.mean(multipliers)
        ema_20 = self.analyzer.calculate_ema(multipliers, 20)[-1] or np.mean(multipliers)
        rsi = self.analyzer.calculate_rsi(multipliers)[-1] if len(self.analyzer.calculate_rsi(multipliers)) > 0 else 50
        volatility = self.analyzer.calculate_volatility(multipliers)[-1] or np.std(multipliers)
        
        crash_rate = sum(crashed) / len(crashed) if crashed else 0
        avg_multiplier = np.mean(multipliers)
        max_multiplier = max(multipliers)
        min_multiplier = min(multipliers)
        avg_duration = np.mean(durations)
        
        recent_5 = multipliers[-5:]
        trend_5 = np.mean(recent_5) / (np.mean(multipliers) + 1e-6)
        
        recent_10 = multipliers[-10:]
        trend_10 = np.mean(recent_10) / (np.mean(multipliers) + 1e-6)
        
        consecutive_crashes = 0
        for i in range(len(crashed) - 1, -1, -1):
            if crashed[i]:
                consecutive_crashes += 1
            else:
                break
        
        consecutive_safe = 0
        for i in range(len(crashed) - 1, -1, -1):
            if not crashed[i]:
                consecutive_safe += 1
            else:
                break
        
        hour = datetime.now().hour
        peak_hours = 1 if 14 <= hour <= 22 else 0
        
        features = np.array([
            sma_20, ema_20, rsi, volatility,
            crash_rate, avg_multiplier, max_multiplier, min_multiplier,
            avg_duration, trend_5, trend_10,
            consecutive_crashes, consecutive_safe, peak_hours, len(multipliers)
        ], dtype=np.float32)
        
        self.feature_names = [
            'sma_20', 'ema_20', 'rsi', 'volatility',
            'crash_rate', 'avg_mult', 'max_mult', 'min_mult',
            'avg_dur', 'trend_5', 'trend_10', 'crashes', 'safe_games', 'peak_hour', 'sample_count'
        ]
        
        return features.reshape(1, -1)
    
    def train(self, games: List[Dict]):
        logger.info("Training predictor...")
        
        X = []
        y_crash = []
        
        for i in range(min(200, len(games) - 30)):
            start_idx = i
            end_idx = start_idx + 30
            window = games[start_idx:end_idx]
            features = self.extract_features(window)
            
            if features is not None:
                X.append(features[0])
                if end_idx < len(games):
                    next_game = games[end_idx]
                    y_crash.append(1 if next_game['crashed'] else 0)
        
        if len(X) < 10:
            logger.warning("Not enough data")
            return
        
        X = np.array(X)
        y_crash = np.array(y_crash)
        X_scaled = self.scaler.fit_transform(X)
        
        self.crash_classifier = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=5)
        self.crash_classifier.fit(X_scaled, y_crash)
        
        os.makedirs('models', exist_ok=True)
        joblib.dump({'crash_classifier': self.crash_classifier}, self.model_path)
        joblib.dump(self.scaler, self.scaler_path)
    
    def load_or_train(self):
        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            logger.info("Loading existing model...")
            models = joblib.load(self.model_path)
            self.crash_classifier = models.get('crash_classifier')
            self.scaler = joblib.load(self.scaler_path)
    
    def predict(self, games: List[Dict]) -> Dict:
        if self.crash_classifier is None:
            return {'error': 'Model not trained', 'message': 'Need more data'}
        
        features = self.extract_features(games)
        if features is None:
            return {'error': 'Insufficient data', 'message': 'Need at least 30 games'}
        
        features_scaled = self.scaler.transform(features)
        crash_prob = self.crash_classifier.predict_proba(features_scaled)[0][1]
        next_mult = np.mean([g['multiplier'] for g in games]) * (1 - crash_prob * 0.5)
        
        if crash_prob > 0.65:
            recommendation = "HIGH CRASH RISK"
            action = "WAIT or SMALL BET"
        elif crash_prob > 0.50:
            recommendation = "MEDIUM RISK"
            action = "SMALL BET"
        else:
            recommendation = "LOW CRASH RISK"
            action = "BET"
        
        return {
            'next_multiplier': round(max(1.0, min(next_mult, 999.99)), 2),
            'crash_probability': round(crash_prob * 100, 2),
            'safe_probability': round((1 - crash_prob) * 100, 2),
            'recommendation': recommendation,
            'action': action,
            'confidence': round(max(crash_prob, 1 - crash_prob) * 100, 2),
            'timestamp': datetime.now().isoformat()
        }