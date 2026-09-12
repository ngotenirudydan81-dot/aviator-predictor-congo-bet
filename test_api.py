"""
Test script for the Aviator Predictor API
"""
import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000/api"

def test_health():
    """Test health endpoint"""
    print("Testing /api/health...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print("-" * 50)

def test_single_prediction():
    """Test single prediction"""
    print("Testing /api/predict (single)...")
    data = {
        "previous_multiplier": 45.5,
        "game_duration": 30,
        "time_of_day": 14,
        "day_of_week": 3,
        "volatility_index": 65.2
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print("-" * 50)

def test_batch_prediction():
    """Test batch prediction"""
    print("Testing /api/batch-predict...")
    data = [
        {
            "previous_multiplier": 45.5,
            "game_duration": 30,
            "time_of_day": 14,
            "day_of_week": 3,
            "volatility_index": 65.2
        },
        {
            "previous_multiplier": 78.2,
            "game_duration": 25,
            "time_of_day": 18,
            "day_of_week": 5,
            "volatility_index": 72.1
        },
        {
            "previous_multiplier": 32.1,
            "game_duration": 45,
            "time_of_day": 20,
            "day_of_week": 6,
            "volatility_index": 55.3
        }
    ]
    response = requests.post(f"{BASE_URL}/batch-predict", json=data)
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print("-" * 50)

def test_model_info():
    """Test model info endpoint"""
    print("Testing /api/model-info...")
    response = requests.get(f"{BASE_URL}/model-info")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print("-" * 50)

def test_stats():
    """Test stats endpoint"""
    print("Testing /api/stats...")
    response = requests.get(f"{BASE_URL}/stats")
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print("-" * 50)

def test_invalid_request():
    """Test invalid request"""
    print("Testing invalid request...")
    data = {
        "previous_multiplier": 45.5
        # Missing required fields
    }
    response = requests.post(f"{BASE_URL}/predict", json=data)
    print(f"Status: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    print("-" * 50)

if __name__ == "__main__":
    print(f"🚀 Aviator Predictor API Test Suite")
    print(f"Testing: {BASE_URL}")
    print(f"Time: {datetime.utcnow().isoformat()}")
    print("=" * 50)
    
    try:
        test_health()
        test_model_info()
        test_stats()
        test_single_prediction()
        test_batch_prediction()
        test_invalid_request()
        
        print("✅ All tests completed!")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Make sure the server is running!")
