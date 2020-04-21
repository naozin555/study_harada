# データのモデルクラス
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
