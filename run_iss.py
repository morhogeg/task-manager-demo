# run_iss.py
from src import iss_api

position = iss_api.get_iss_position()

if position:
    print("🚀 ISS Location:")
    print(f"Latitude: {position['latitude']}")
    print(f"Longitude: {position['longitude']}")
else:
    print("Failed to fetch ISS location.")