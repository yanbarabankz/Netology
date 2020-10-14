countries_temperature = [
['Thailand'], [75.2, 77, 78.8, 73.4, 68, 75.2, 77],
['Germany'], [57.2, 55.4, 59, 59, 53.6],
['Russia'], [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6],
['Poland'], [50, 50, 53.6, 57.2, 55.4, 55.4]]


thailand = 0
germany = 0
russia = 0
poland = 0

for x in range(len(countries_temperature[1])):
    thailand += countries_temperature[1][x]
print(*countries_temperature[0], '-', round((5/9*((thailand/(len(countries_temperature[1])))-32)), 1), 'C')

for x in range(len(countries_temperature[3])):
    germany += countries_temperature[3][x]
print(*countries_temperature[2], '-', round((5/9*((germany/(len(countries_temperature[3])))-32)), 1), 'C')

for x in range(len(countries_temperature[5])):
    russia += countries_temperature[5][x]
print(*countries_temperature[4], '-',round((5/9*((russia/(len(countries_temperature[5])))-32)), 1), 'C')

for x in range(len(countries_temperature[7])):
    poland += countries_temperature[7][x]
print(*countries_temperature[6], '-', round((5/9*((poland/(len(countries_temperature[7])))-32)), 1), 'C')