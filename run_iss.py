# run_iss.py
from src.iss_api import get_iss_position

position = get_iss_position()

if position:
    print("🚀 ISS Location:")
    print(f"Latitude: {position['latitude']}")
    print(f"Longitude: {position['longitude']}")
else:
    print("Failed to fetch ISS location.")