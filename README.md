# GEO Utility (`geo-util`)

This is a command-line utility that fetches latitude, longitude, and place information from OpenWeather's Geocoding API.

## Features
- Supports querying by city/state or ZIP code.
- Handles multiple location inputs at once.
- Returns structured output with latitude, longitude, and place details.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/geo-util.git
   cd geo-util
2. Install Dependencies
    ```sh
    pip install -r requirements.txt
3. Usage
- Run the utility with city/state or ZIP codes as arguments:
    ```sh
    python geo_util.py "Madison, WI" "10001"
- Example Output
    ```sh
  Madison, WI, US -> Lat: 43.0731, Lon: -89.4012
  New York, NY, US -> Lat: 40.7128, Lon: -74.0060

## Alternative running with Docker(Recommended)

Make sure docker is running

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/geo-util.git
   cd geo-util
2. Building docker image
    ```sh
    docker build -t geo-util .
3. Usage
- Run geo-util
    ```sh
    docker run --rm -it geo-util geo_util.py "Madison, WI" "10001"
- Run tests
    ```sh
  docker run --rm geo-util -m unittest discover tests

    
# Single city/state lookup

    python geo_util.py "Chicago, IL"

# Single ZIP code lookup
    
    python geo_util.py "60601"

# Multiple locations (mix of city/state and ZIP)
    
    python geo_util.py "San Francisco, CA" "30301" "Seattle, WA"

## Testing
- Run the integration tests using unittest:
    ```sh
    python -m unittest discover tests/
## Requirements
- Python 3.x
- requests library (installed via requirements.txt)

## API Information
This utility uses the OpenWeather Geocoding API:

    City/State API: https://openweathermap.org/api/geocoding-api#direct_name
    ZIP Code API: https://openweathermap.org/api/geocoding-api#direct_zip
    API Key Used: f897a99d971b5eef57be6fafa0d83239

