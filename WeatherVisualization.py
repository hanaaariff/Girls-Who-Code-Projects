import weather
list_of_report = weather.get_weather()

#import matplotlib.pyplot as plt; plt.rcdefaults()
#import numpy as np
import matplotlib.pyplot as plt

# ask user for a state
state = input("Enter a state to find out its average temperatures on January 1, 2017: ")

# find avg temps and their corresponding cities for that state
city_temps = {}
for item in list_of_report:
    if (item['Station']['State'] == state):
        city_temps[item['Station']['City'] : item['Data']['Temperature']['Avg Temp']

# plot those values on a column/bar chart
    # x-axis = cities
    # y-axis = average temperatures

print(city_temps)

# for item in list_of_report:
#     print(item)
#     print()

# objects = (list_of_report[0]["Data"]["Temperature"]["Avg Temp"], list_of_report[0]["Data"]["Temperature"]["Max Temp"], list_of_report[0]["Data"]["Temperature"]["Min Temp"])
# #y_pos = np.arange(len(objects))
# performance = [50,45,40,35,30,25,20,15,10,5]
#
# plt.bar(y_pos, performance, align='center', alpha=0.5)
# plt.xticks(y_pos, objects)
# plt.ylabel('Usage')
# plt.title('Programming language usage')
#
# plt.show()

# --------------------------------------------------------------
# temperature
# import matplotlib.pyplot as temperature
#
# temps = [
#     list_of_report[0]["Data"]["Temperature"]["Avg Temp"],
#     list_of_report[0]["Data"]["Temperature"]["Max Temp"],
#     list_of_report[0]["Data"]["Temperature"]["Min Temp"]
# ]
#
# temperature.hist(temps, bins=[-1, -0.5, 0.0, 0.5, 1])
# temperature.xlabel('Avg, Max, and Min Temperatures for 01-03-2016')
# temperature.ylabel('Degrees in Fahrenheit')
# temperature.title('Histogram of Weather in Birmingham, Alabama')
# temperature.axis([0, 1.1, 0, 50])
# temperature.grid(True)
# temperature.show()

# wind

# precipitation
