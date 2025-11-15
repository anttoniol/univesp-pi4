from json_reader import read_json_file
import pandas as pd


filename = "data/air_pollution/2025-10-02_2025-10-15"
initial_format = ".json"
content = read_json_file(filename + initial_format)

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

final_format = ".csv"
dataframe.to_csv(filename + final_format, sep = ";", index=False, index_label=True)
