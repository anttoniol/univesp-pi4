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

url = "http://api.openweathermap.org/data/2.5/air_pollution/history"
folder = properties['folder']
os.makedirs(folder, exist_ok=True)

delta = datetime.timedelta(days=1)
format = "%Y-%m-%d"
start_date = datetime.datetime.strptime(properties["initial_date"], format).timestamp()
end_date = datetime.datetime.strptime(properties["final_date"], format).timestamp()

lat = properties["lat"]
lon = properties["lon"]
appid = properties["key"]
params = {
    "lat": lat,
    "lon": lon,
    "appid": appid

}
params["start"] = int(start_date)
params["end"] = int(end_date)

result = requests.get(url, params=params)
data = result.json()

filename = f"{properties['initial_date']}_{properties['final_date']}.json"
with open(f"{folder}/{filename}", 'w') as f:
    json.dump(data, f, indent=4)
