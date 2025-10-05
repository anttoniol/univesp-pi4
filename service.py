import os
import requests
import datetime
import json


def read_json_file(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filepath}'. Check file format.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


properties = read_json_file("properties.json")

lat = properties["lat"]
lon = properties["lon"]
tz = properties["tz"]
units = "metric"
appid = properties["key"]
params = {
    "lat": lat,
    "lon": lon,
    "tz": tz,
    "units": units,
    "appid": appid

}
url = "https://api.openweathermap.org/data/3.0/onecall/day_summary"
folder = properties['folder']
os.makedirs(folder, exist_ok=True)

delta = datetime.timedelta(days=1)
format = "%Y-%m-%d"
start_date = datetime.datetime.strptime(properties["initial_date"], format)
end_date = datetime.datetime.strptime(properties["final_date"], format)
current_date = start_date

while current_date <= end_date:
    date = datetime.datetime.strftime(current_date, format)
    params["date"] = date
    result = requests.get(url, params=params)
    data = result.json()
    
    filename = f"{date}.json"

    with open(f"{folder}/{filename}", 'w') as f:
        json.dump(data, f, indent=4)

    current_date += delta
