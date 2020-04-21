from class_file import Data


class Serve(object):

    # データを格納するメソッド
    def input_data(self):
        datas_list = []
        for data in self:
            datas = Data(data.split(',')[0], data.split(',')[1],
                         data.split(',')[2], data.split(',')[3],
                         data.split(',')[4], data.split(',')[5],
                         data.split(',')[6], data.split(',')[7],
                         data.split(',')[8], data.split(',')[9],
                         data.split(',')[10], data.split(',')[11],
                         data.split(',')[12], data.split(',')[13],
                         data.split(',')[14]
                         )
            datas_list.append(datas)
        return datas_list

    # 月の需給合計を計算するメソッド
    def sum_month(self, month):
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

        ym = month.strftime("{}/{}".format(month.year, month.month))
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

        total_time = 'XXX'
        sum_month = Data(ym, total_time, total_demand, total_nuclear,
                         total_thermal, total_water, total_geo_thermal,
                         total_biomass, total_solar, total_controlled_solar,
                         total_wind, total_controlled_wind, total_pumped_water,
                         total_interconnection, total_total_supply
                         )
        return sum_month

    # 月の需給割合を計算するメソッド
    def percentage_month(self):
        date = self.date
        time = self.time
        percentage_demand = self.demand / self.total_supply *100
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
        print('年月：' + self.date,
              '原子力：{:.2f}%'.format(self.nuclear),
              '火力：{:.2f}%'.format(self.thermal),
              '水力：{:.2f}%'.format(self.water),
              '地熱：{:.2f}%'.format(self.geo_thermal),
              'バイオマス：{:.2f}%'.format(self.biomass),
              '太陽光発電実績：{:.2f}%'.format(self.solar),
              '太陽光出力制御量：{:.2f}%'.format(self.controlled_solar),
              '風力発電実績：{:.2f}%'.format(self.wind),
              '風力出力制御量：{:.2f}%'.format(self.controlled_wind),
              '揚水：{:.2f}%'.format(self.pumped_water),
              '連系線：{:.2f}%'.format(self.interconnection)
              )