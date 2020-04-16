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

for data in data_list:
    print(data.split(','))

class Data(object):
    def __init__(self, date, time, demand, nuclear, thermal, water, geo_thermal,
                 biomass, solar, controlled_solar, wind, controlled_wind,
                 pumped_water, interconnection, total_supply):
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
        self.total_supply = total_supply

datas_list = []
for data in data_list:
    datas = Data(data.split(',')[0], data.split(',')[1], data.split(',')[2],
                 data.split(',')[3], data.split(',')[4], data.split(',')[5],
                 data.split(',')[6], data.split(',')[7], data.split(',')[8],
                 data.split(',')[9], data.split(',')[10], data.split(',')[11],
                 data.split(',')[12], data.split(',')[13], data.split(',')[14],
                 )
    datas_list.append(datas)

# 2019年4月1日の火力の出力
print(datas_list[0].thermal)

# ４月　変数定義
total_demand_2019_4 = 0
total_nuclear_2019_4 = 0
total_thermal_2019_4 = 0
total_water_2019_4 = 0
total_geo_thermal_2019_4 = 0
total_biomass_2019_4 = 0
total_solar_2019_4 = 0
total_controlled_solar_2019_4 = 0
total_wind_2019_4 = 0
total_controlled_wind_2019_4 = 0
total_pumped_water_2019_4 = 0
total_interconnection_2019_4 = 0
total_total_supply_2019_4 = 0

# 4月　需給合計
for data_every_hour in datas_list:
    if data_every_hour.date.startswith('2019/4'):
        total_demand_2019_4 += int(data_every_hour.demand)
        total_nuclear_2019_4 += int(data_every_hour.nuclear)
        total_thermal_2019_4 += int(data_every_hour.thermal)
        total_water_2019_4 += int(data_every_hour.water)
        total_geo_thermal_2019_4 += int(data_every_hour.geo_thermal)
        total_biomass_2019_4 += int(data_every_hour.biomass)
        total_solar_2019_4 += int(data_every_hour.solar)
        total_controlled_solar_2019_4 += int(data_every_hour.controlled_solar)
        total_wind_2019_4 += int(data_every_hour.wind)
        total_controlled_wind_2019_4 += int(data_every_hour.controlled_wind)
        total_pumped_water_2019_4 += int(data_every_hour.pumped_water)
        total_interconnection_2019_4 += int(data_every_hour.interconnection)
        total_total_supply_2019_4 += int(data_every_hour.total_supply)

# 4月　需給割合　算出
percentage_nuclear_2019_4 = total_nuclear_2019_4/total_total_supply_2019_4*100
percentage_thermal_2019_4 = total_thermal_2019_4/total_total_supply_2019_4*100
percentage_water_2019_4 = total_water_2019_4 / total_total_supply_2019_4*100
percentage_geo_thermal_2019_4 = total_geo_thermal_2019_4 / total_total_supply_2019_4*100
percentage_biomass_2019_4 = total_biomass_2019_4 / total_total_supply_2019_4*100
percentage_solar_2019_4 = total_solar_2019_4 / total_total_supply_2019_4*100
percentage_controlled_solar_2019_4 = total_controlled_solar_2019_4 / total_total_supply_2019_4 * 100
percentage_wind_2019_4 = total_wind_2019_4 / total_total_supply_2019_4*100
percentage_controlled_wind_2019_4 = total_controlled_wind_2019_4 / total_total_supply_2019_4*100
percentage_pumped_water_2019_4 = total_pumped_water_2019_4 / total_total_supply_2019_4*100
percentage_interconnection_2019_4 = total_interconnection_2019_4 / total_total_supply_2019_4*100

# 4月　需給割合　出力
print('2019/4 原子力：{:.2f}%'.format(percentage_nuclear_2019_4))
print('2019/4 火力：{:.2f}%'.format(percentage_thermal_2019_4))
print('2019/4 水力：{:.2f}%'.format(percentage_water_2019_4))
print('2019/4 地熱：{:.2f}%'.format(percentage_geo_thermal_2019_4))
print('2019/4 バイオマス：{:.2f}%'.format(percentage_biomass_2019_4))
print('2019/4 太陽光発電実績：{:.2f}%'.format(percentage_solar_2019_4))
print('2019/4 太陽光出力制御量：{:.2f}%'.format(percentage_controlled_solar_2019_4))
print('2019/4 風力発電実績：{:.2f}%'.format(percentage_wind_2019_4))
print('2019/4 風力出力制御量：{:.2f}%'.format(percentage_controlled_wind_2019_4))
print('2019/4 揚水：{:.2f}%'.format(percentage_pumped_water_2019_4))
print('2019/4 連系線：{:.2f}%'.format(percentage_interconnection_2019_4))

