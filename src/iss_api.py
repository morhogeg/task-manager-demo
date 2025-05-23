# src/iss_api.py
import requests

def get_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # raises an error for bad status codes
        data = response.json()
        position = data['iss_position']
        return {
            "latitude": position['latitude'],
            "longitude": position['longitude']
        }
    except requests.RequestException as e:
        print("API error:", e)
        return None