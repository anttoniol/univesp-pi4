import os
import requests
import datetime
import json
from json_reader import read_json_file


properties = read_json_file("properties.json")

url_forecast = "http://api.openweathermap.org/data/2.5/air_pollution/forecast"

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
