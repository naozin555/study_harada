import re
import csv
import numpy as np

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


header = header.split(',')
print(header)

for i, data in enumerate(data_list):
    data_list[i] = data.split(',')
# print(data_list)

index_Date = header.index('DATE')
# index_Time = header.index('Time')
index_Demand = header.index('東京エリア需要')
# index_Nuclear = header.index('原子力')
# index_Thermal = header.index('火力')
# index_Water = header.index('水力')
# index_Geothermal = header.index('地熱')
# index_Biomass = header.index('バイオマス')
# index_Solar = header.index('太陽光発電実績')
# index_ControlledSolar = header.index('太陽光出力制御量')
# index_Wind = header.index('風力発電実績')
# index_ControlledWind = header.index('風力出力制御量')
# index_PumpedWater = header.index('揚水')
# index_Interconnection = header.index('連系線')
# index_Total = header.index('合計')

years = [2019, 2020]
num_months = 12
ym = [0]*12
data_Demand = []
for year in years:
    for month in range(num_months):
        ym[month-1] = str(year) + "/" + str(month) + "/"
        print(ym[month-1])
        for i, data in enumerate(data_list):
            if data[index_Date].startswith(ym[month-1]):
                data_Demand[i][].append(data[index_Demand])
                print(data_Demand)
        sum(data_Demand[i])

