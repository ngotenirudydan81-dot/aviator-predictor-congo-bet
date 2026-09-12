"""Real-time data collector for Aviator Congo Bet"""
import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import numpy as np
import pandas as pd
import sqlite3
from dataclasses import dataclass, asdict
from collections import deque

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class GameRound:
    """Represents a single Aviator game round"""
    round_id: str
    timestamp: datetime
    multiplier: float
    duration: float
    crashed: bool
    bet_amount: Optional[float] = None
    win_amount: Optional[float] = None
    status: str = 'completed'

class DataCollector:
    """Collects and stores real Aviator game data"""
    
    def __init__(self, db_path: str = 'data/aviator_games.db'):
        self.db_path = db_path
        self.games: deque = deque(maxlen=1000)
        self.init_database()
    
    def init_database(self):
        """Initialize SQLite database"""
        import os
        os.makedirs('data', exist_ok=True)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_rounds (
                round_id TEXT PRIMARY KEY,
                timestamp DATETIME,
                multiplier REAL,
                duration REAL,
                crashed BOOLEAN,
                bet_amount REAL,
                win_amount REAL,
                status TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS predictions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                round_id TEXT,
                predicted_multiplier REAL,
                predicted_crash_probability REAL,
                confidence REAL,
                actual_multiplier REAL,
                accuracy BOOLEAN,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (round_id) REFERENCES game_rounds(round_id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def add_game(self, game: GameRound):
        """Add a game round to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO game_rounds 
            (round_id, timestamp, multiplier, duration, crashed, bet_amount, win_amount, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            game.round_id,
            game.timestamp.isoformat(),
            game.multiplier,
            game.duration,
            game.crashed,
            game.bet_amount,
            game.win_amount,
            game.status
        ))
        
        conn.commit()
        conn.close()
        self.games.append(game)
    
    def get_recent_games(self, limit: int = 100) -> List[GameRound]:
        """Get recent games from database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT round_id, timestamp, multiplier, duration, crashed, bet_amount, win_amount, status
            FROM game_rounds
            ORDER BY timestamp DESC
            LIMIT ?
        ''', (limit,))
        
        games = []
        for row in cursor.fetchall():
            games.append(GameRound(
                round_id=row[0],
                timestamp=datetime.fromisoformat(row[1]),
                multiplier=row[2],
                duration=row[3],
                crashed=row[4],
                bet_amount=row[5],
                win_amount=row[6],
                status=row[7]
            ))
        
        conn.close()
        return games
    
    def get_statistics(self) -> Dict:
        """Get statistics from game history"""
        games = self.get_recent_games(500)
        
        if not games:
            return {}
        
        multipliers = [g.multiplier for g in games]
        crashes = sum(1 for g in games if g.crashed)
        
        return {
            'total_games': len(games),
            'avg_multiplier': np.mean(multipliers),
            'max_multiplier': max(multipliers),
            'min_multiplier': min(multipliers),
            'crash_rate': crashes / len(games) if games else 0,
            'volatility': np.std(multipliers),
            'median_multiplier': np.median(multipliers),
            'percentile_95': np.percentile(multipliers, 95),
            'percentile_75': np.percentile(multipliers, 75),
            'percentile_25': np.percentile(multipliers, 25)
        }

class RealTimeSimulator:
    """Simulates real-time Aviator games with realistic data"""
    
    def __init__(self):
        self.collector = DataCollector()
        self.round_counter = 0
    
    def generate_realistic_game(self) -> GameRound:
        """Generate a realistic game round"""
        self.round_counter += 1
        
        rand = np.random.random()
        
        if rand < 0.60:
            multiplier = np.random.exponential(2.0) + 1.0
            duration = np.random.uniform(5, 15)
            crashed = True
        elif rand < 0.85:
            multiplier = np.random.exponential(3.5) + 3.0
            duration = np.random.uniform(15, 40)
            crashed = np.random.random() < 0.3
        else:
            multiplier = np.random.exponential(8.0) + 8.0
            duration = np.random.uniform(30, 120)
            crashed = np.random.random() < 0.1
        
        multiplier = max(1.0, min(multiplier, 999.99))
        
        game = GameRound(
            round_id=f"CONGO_{datetime.now().strftime('%Y%m%d%H%M%S')}_{self.round_counter}",
            timestamp=datetime.now(),
            multiplier=multiplier,
            duration=duration,
            crashed=crashed,
            bet_amount=np.random.choice([100, 200, 500, 1000, 2000]),
            status='completed'
        )
        
        if not crashed and np.random.random() < 0.7:
            game.win_amount = game.bet_amount * multiplier
        
        return game