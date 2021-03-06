from class_file import Data


class Service(object):

    # データを格納するメソッド
    def input_data(self):
        datas_list = []
        for data in self:
            splited_data = data.split(',')
            datas = Data(splited_data[0], splited_data[1], splited_data[2],
                         splited_data[3], splited_data[4], splited_data[5],
                         splited_data[6], splited_data[7], splited_data[8],
                         splited_data[9], splited_data[10], splited_data[11],
                         splited_data[12], splited_data[13], splited_data[14]
                         )
            datas_list.append(datas)
        return datas_list

    # 月の需給合計を計算するメソッド
    def sum_month(self, month):
        sum_demand = 0
        sum_nuclear = 0
        sum_thermal = 0
        sum_water = 0
        sum_geo_thermal = 0
        sum_biomass = 0
        sum_solar = 0
        sum_controlled_solar = 0
        sum_wind = 0
        sum_controlled_wind = 0
        sum_pumped_water = 0
        sum_interconnection = 0
        sum_total_supply = 0

        ym = month.strftime("{}/{}".format(month.year, month.month))
        for data_every_hour in self:
            if data_every_hour.date.startswith(ym):
                sum_demand += int(data_every_hour.demand)
                sum_nuclear += int(data_every_hour.nuclear)
                sum_thermal += int(data_every_hour.thermal)
                sum_water += int(data_every_hour.water)
                sum_geo_thermal += int(data_every_hour.geo_thermal)
                sum_biomass += int(data_every_hour.biomass)
                sum_solar += int(data_every_hour.solar)
                sum_controlled_solar += int(data_every_hour.controlled_solar)
                sum_wind += int(data_every_hour.wind)
                sum_controlled_wind += int(data_every_hour.controlled_wind)
                sum_pumped_water += int(data_every_hour.pumped_water)
                sum_interconnection += int(data_every_hour.interconnection)
                sum_total_supply += int(data_every_hour.total_supply)

        total_time = 'XXX'
        sum_month = Data(ym, total_time, sum_demand, sum_nuclear,
                         sum_thermal, sum_water, sum_geo_thermal,
                         sum_biomass, sum_solar, sum_controlled_solar,
                         sum_wind, sum_controlled_wind, sum_pumped_water,
                         sum_interconnection, sum_total_supply
                         )
        return sum_month

    # 月の需給割合を計算するメソッド
    def percentage_month(self):
        date = self.date
        time = self.time
        percentage_demand = self.demand / self.total_supply * 100
        percentage_nuclear = self.nuclear / self.total_supply * 100
        percentage_thermal = self.thermal / self.total_supply * 100
        percentage_water = self.water / self.total_supply * 100
        percentage_geo_thermal = self.geo_thermal / self.total_supply * 100
        percentage_biomass = self.biomass / self.total_supply * 100
        percentage_solar = self.solar / self.total_supply * 100
        percentage_controlled_solar = self.controlled_solar / \
                                      self.total_supply * 100
        percentage_wind = self.wind / self.total_supply * 100
        percentage_controlled_wind = self.controlled_wind / \
                                     self.total_supply * 100
        percentage_pumped_water = self.pumped_water / self.total_supply * 100
        percentage_interconnection = self.interconnection / \
                                     self.total_supply * 100
        percentage_total_supply = self.total_supply / self.total_supply * 100

        percentage_month = Data(date, time, percentage_demand,
                                percentage_nuclear, percentage_thermal,
                                percentage_water, percentage_geo_thermal,
                                percentage_biomass, percentage_solar,
                                percentage_controlled_solar, percentage_wind,
                                percentage_controlled_wind,
                                percentage_pumped_water,
                                percentage_interconnection,
                                percentage_total_supply
                                )
        return percentage_month

    # 月の需給を表示するメソッド
    def display(self):
        print('年月：' + self.date + ',',
              '原子力：{:.2f}%,'.format(self.nuclear),
              '火力：{:.2f}%,'.format(self.thermal),
              '水力：{:.2f}%,'.format(self.water),
              '地熱：{:.2f}%,'.format(self.geo_thermal),
              'バイオマス：{:.2f}%,'.format(self.biomass),
              '太陽光発電実績：{:.2f}%,'.format(self.solar),
              '太陽光出力制御量：{:.2f}%,'.format(self.controlled_solar),
              '風力発電実績：{:.2f}%,'.format(self.wind),
              '風力出力制御量：{:.2f}%,'.format(self.controlled_wind),
              '揚水：{:.2f}%,'.format(self.pumped_water),
              '連系線：{:.2f}%'.format(self.interconnection)
              )
