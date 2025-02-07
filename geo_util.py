import requests
import argparse

API_KEY = "f897a99d971b5eef57be6fafa0d83239"
BASE_URL_NAME = "http://api.openweathermap.org/geo/1.0/direct"
BASE_URL_ZIP = "http://api.openweathermap.org/geo/1.0/zip"


def get_location_data(location):
    """Fetch geolocation data based on city/state or ZIP code."""
    if location.isdigit():  # Handle ZIP code case
        url = f"{BASE_URL_ZIP}?zip={location},US&appid={API_KEY}"
    else:  # Handle city/state case
        url = f"{BASE_URL_NAME}?q={location},US&limit=1&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code != 200:
        return {"error": f"Failed to fetch data for {location} (HTTP {response.status_code})"}

    data = response.json()

    if not data:
        return {"error": f"No data found for {location}"}

    if isinstance(data, list):  # City/state responses return lists
        data = data[0]

    return {
        "location": location,
        "latitude": data.get("lat"),
        "longitude": data.get("lon"),
        "name": data.get("name"),
        "state": data.get("state", "N/A"),
        "country": data.get("country", "N/A"),
    }


def main():
    parser = argparse.ArgumentParser(description="Fetch geolocation data using OpenWeather API.")
    parser.add_argument("locations", nargs="+", help="List of city,state or ZIP codes to lookup")
    args = parser.parse_args()

    results = [get_location_data(loc) for loc in args.locations]

    for res in results:
        if "error" in res:
            print(f"Error: {res['error']}")
        else:
            print(f"{res['name']}, {res['state']}, {res['country']} -> Lat: {res['latitude']}, Lon: {res['longitude']}")


if __name__ == "__main__":
    main()
