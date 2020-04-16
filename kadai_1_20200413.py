import re

with open('area-2019.csv', 'r') as f:

    header = ''
    data_list = []

    for line in f:

        if re.search('供給力$', line):
            header = line.strip()[:-4]

        if re.search('^,,,', line):
            header = header + line.strip()[2:]

        if ':' in line:
            data_list.append(line.strip())


headers = header.split(',')
print(headers)


class Data(object):
    def __init__(self, date, time, demand, nuclear, thermal, water, geo_thermal,
                 biomass, solar, controlled_solar, wind, controlled_wind,
                 pumped_water, interconnection, total):
        self.date = date
        self.time = time
        self.demand = demand
        self.nuclear = nuclear
        self.thermal = thermal
        self.water = water
        self.geo_thermal = geo_thermal
        self.biomass = biomass
        self.solar = solar
        self.controlled_solar = controlled_solar
        self.wind = wind
        self.controlled_wind = controlled_wind
        self.pumped_water = pumped_water
        self.interconnection = interconnection
        self.total = total

# for i
#     data = Data(data_list[0][i], data_list[1][i], data_list[2][i], data_list[3][i],
#                 data_list[4][i], data_list[5][i], data_list[6][i], data_list[8][i],
#                 data_list[9][i], data_list[10][i], data_list[11][i], data_list[12][i],
#                 data_list[13][i], data_list[14][i], data_list[15][i])
#
# print(data_list[1])


