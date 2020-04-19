
# データを操作するクラス
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

    def input_data(data_list):
        datas_list = []
        for data in data_list:
            datas = Data(data.split(',')[0], data.split(',')[1], data.split(',')[2],
                         data.split(',')[3], data.split(',')[4], data.split(',')[5],
                         data.split(',')[6], data.split(',')[7], data.split(',')[8],
                         data.split(',')[9], data.split(',')[10], data.split(',')[11],
                         data.split(',')[12], data.split(',')[13], data.split(',')[14],
                         )
            datas_list.append(datas)
        return(datas_list)

    def percentage_every_month(datas_list, ym):
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

        for data_every_hour in datas_list:
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
            percentage_controlled_solar = total_controlled_solar / total_total_supply * 100
            percentage_wind = total_wind / total_total_supply * 100
            percentage_controlled_wind = total_controlled_wind / total_total_supply * 100
            percentage_pumped_water = total_pumped_water / total_total_supply * 100
            percentage_interconnection = total_interconnection / total_total_supply * 100

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

    def display(datas_list):
        print('日付：' + str(datas_list[0]))
        print('原子力：{:.2f}%'.format(datas_list[1]))
        print('火力：{:.2f}%'.format(datas_list[2]))
        print('水力：{:.2f}%'.format(datas_list[3]))
        print('地熱：{:.2f}%'.format(datas_list[4]))
        print('バイオマス：{:.2f}%'.format(datas_list[5]))
        print('太陽光発電実績：{:.2f}%'.format(datas_list[6]))
        print('太陽光出力制御量：{:.2f}%'.format(datas_list[7]))
        print('風力発電実績：{:.2f}%'.format(datas_list[8]))
        print('風力出力制御量：{:.2f}%'.format(datas_list[9]))
        print('揚水：{:.2f}%'.format(datas_list[10]))
        print('連系線：{:.2f}%'.format(datas_list[11]))

        # print(' 原子力：{:.2f}%'.format(percentage_nuclear_2019_4))
        # print('2019/4 火力：{:.2f}%'.format(percentage_thermal_2019_4))
        # print('2019/4 水力：{:.2f}%'.format(percentage_water_2019_4))
        # print('2019/4 地熱：{:.2f}%'.format(percentage_geo_thermal_2019_4))
        # print('2019/4 バイオマス：{:.2f}%'.format(percentage_biomass_2019_4))
        # print('2019/4 太陽光発電実績：{:.2f}%'.format(percentage_solar_2019_4))
        # print('2019/4 太陽光出力制御量：{:.2f}%'.format(percentage_controlled_solar_2019_4))
        # print('2019/4 風力発電実績：{:.2f}%'.format(percentage_wind_2019_4))
        # print('2019/4 風力出力制御量：{:.2f}%'.format(percentage_controlled_wind_2019_4))
        # print('2019/4 揚水：{:.2f}%'.format(percentage_pumped_water_2019_4))
        # print('2019/4 連系線：{:.2f}%'.format(percentage_interconnection_2019_4))
