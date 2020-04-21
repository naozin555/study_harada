import re
import datetime

from class_file import Data

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


# データを格納するメソッド
def input_data(self):
    datas_list = []
    for data in self:
        datas = Data(data.split(',')[0], data.split(',')[1], data.split(',')[2],
                     data.split(',')[3], data.split(',')[4], data.split(',')[5],
                     data.split(',')[6], data.split(',')[7], data.split(',')[8],
                     data.split(',')[9], data.split(',')[10], data.split(',')[11],
                     data.split(',')[12], data.split(',')[13], data.split(',')[14],
                     )
        datas_list.append(datas)
    return datas_list

# 月の需給を計算するメソッド
def percentage_every_month(self, ym):
    total_demand = 0
    total_nuclear = 0
    total_thermal = 0
    total_water = 0
    total_geo_thermal = 0
    total_biomass = 0
    total_solar = 0
    total_controlled_solar = 0
    total_wind = 0
    total_controlled_wind = 0
    total_pumped_water = 0
    total_interconnection = 0
    total_total_supply = 0

    for data_every_hour in self:
        if data_every_hour.date.startswith(ym):
            total_demand += int(data_every_hour.demand)
            total_nuclear += int(data_every_hour.nuclear)
            total_thermal += int(data_every_hour.thermal)
            total_water += int(data_every_hour.water)
            total_geo_thermal += int(data_every_hour.geo_thermal)
            total_biomass += int(data_every_hour.biomass)
            total_solar += int(data_every_hour.solar)
            total_controlled_solar += int(data_every_hour.controlled_solar)
            total_wind += int(data_every_hour.wind)
            total_controlled_wind += int(data_every_hour.controlled_wind)
            total_pumped_water += int(data_every_hour.pumped_water)
            total_interconnection += int(data_every_hour.interconnection)
            total_total_supply += int(data_every_hour.total_supply)

        percentage_nuclear = total_nuclear / total_total_supply * 100
        percentage_thermal = total_thermal / total_total_supply * 100
        percentage_water = total_water / total_total_supply * 100
        percentage_geo_thermal = total_geo_thermal / total_total_supply * 100
        percentage_biomass = total_biomass / total_total_supply * 100
        percentage_solar = total_solar / total_total_supply * 100
        percentage_controlled_solar = total_controlled_solar / \
                                      total_total_supply * 100
        percentage_wind = total_wind / total_total_supply * 100
        percentage_controlled_wind = total_controlled_wind / \
                                     total_total_supply * 100
        percentage_pumped_water = total_pumped_water / total_total_supply * 100
        percentage_interconnection = total_interconnection / \
                                     total_total_supply * 100

    demand_supply_month = [ym, percentage_nuclear, percentage_thermal,
                           percentage_water, percentage_geo_thermal,
                           percentage_biomass, percentage_solar,
                           percentage_controlled_solar,
                           percentage_wind,
                           percentage_controlled_wind,
                           percentage_pumped_water,
                           percentage_interconnection,
                           ]
    return demand_supply_month

# 月の需給を表示するメソッド
def display(self):
    print('日付：' + str(self[0]))
    print('原子力：{:.2f}%'.format(self[1]))
    print('火力：{:.2f}%'.format(self[2]))
    print('水力：{:.2f}%'.format(self[3]))
    print('地熱：{:.2f}%'.format(self[4]))
    print('バイオマス：{:.2f}%'.format(self[5]))
    print('太陽光発電実績：{:.2f}%'.format(self[6]))
    print('太陽光出力制御量：{:.2f}%'.format(self[7]))
    print('風力発電実績：{:.2f}%'.format(self[8]))
    print('風力出力制御量：{:.2f}%'.format(self[9]))
    print('揚水：{:.2f}%'.format(self[10]))
    print('連系線：{:.2f}%'.format(self[11]))

from_date = datetime.date(2019, 4, 1)
to_date = datetime.date(2020, 4, 1)
period = to_date - from_date
period = int(period.days)
datas_list = []
datas_list = input_data(data_list)
for d in range(period):
    day = from_date + datetime.timedelta(days=d)
    # 需給割合を出す処理を記載予定
    # if day.strftime("%Y/%m")
    # display()




