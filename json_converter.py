from json_reader import read_json_file
import pandas as pd


filepath = "data/air_pollution/2025-09-01_2025-10-01.json"
content = read_json_file(filepath)

elements = content["list"]
array = list()

columns = ["dt", "co", "no", "no2", "o3", "so2", "pm2_5", "pm_10", "nh3", "aqi"]
dataframe = pd.DataFrame(columns=columns)

for element in elements:
    row = list()
    row.append(int(element["dt"]))
    row.append(element["components"]["co"])
    row.append(element["components"]["no"])
    row.append(element["components"]["no2"])
    row.append(element["components"]["o3"])
    row.append(element["components"]["so2"])
    row.append(element["components"]["pm2_5"])
    row.append(element["components"]["pm10"])
    row.append(element["components"]["nh3"])
    row.append(element["main"]["aqi"])
    dataframe.loc[len(dataframe)] = row

dataframe.to_csv("data/air_pollution/2025-09-01_2025-10-01.csv", sep = ";", index=False)
