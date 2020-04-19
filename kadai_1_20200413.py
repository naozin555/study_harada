import re

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


# headers = header.split(',')
# print(headers)

# for data in data_list:
#    print(data.split(','))


datas_list = []
datas_list = Data.input_data(data_list)
demand_supply_month = Data.percentage_every_month(datas_list, '2019/4')
Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/5')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/6')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/7')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/8')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/9')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/10')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/11')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2019/12')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2020/1')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2020/2')
# Data.display((demand_supply_month))
# demand_supply_month = Data.percentage_every_month(datas_list, '2020/3')
# Data.display((demand_supply_month))


