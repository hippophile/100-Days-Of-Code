# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()

# print(data)

# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#             print(row)

#     print(temperatures)

# pandas

# data = pd.read_csv("weather_data.csv")
# avrg_temp = data["temp"].mean()
# print(avrg_temp)

# print(f"The max temp is:", data["temp"].max())

# print(data[data.temp == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(((monday.temp)*1.8)+32)

# Createa dataframe from screach
# data_dict = {
#     "students": ["Filip", "Vas"],
#     "scores": [12, 34]
# }
# data = pd.DataFrame(data_dict)
# data.index.name = 'id'
# data.to_csv("new_data.csv", index=False)
# print(data)

# Create: fur/color/count table
import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260210.csv")
# print(data.columns) 
# "Primary Fur Color" Black, Gray, Cinnamon

black_c = len(data[data["Primary Fur Color"] == "Black"])
grey_c = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_c = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = []

data_dict.append({"color": "Black", "count": black_c})
data_dict.append({"color": "Grey", "count": grey_c})
data_dict.append({"color": "Cinnamon", "count": cinnamon_c})

data = pd.DataFrame(data_dict)
data.to_csv("skiouroi.csv", index=False)


# new_data = {}
# new_data.to_csv("new_data.csv")
