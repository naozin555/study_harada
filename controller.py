import datetime
from dateutil.relativedelta import relativedelta

from service import Service, ServiceKansai


class Controller(object):

    def execute():

        area_list = ['Tokyo', 'Kansai']
        for area in area_list:

            if area == 'Tokyo':
                raw_data = Service.file_open('area-2019.csv')
                header = raw_data[0]
                data_list = raw_data[1]
                datas_list = []
                datas_list = Service.input_data(data_list)
            elif area == 'Kansai':
                raw_data = ServiceKansai.file_open('area_jyukyu_jisseki_2019.csv')
                header = raw_data[0]
                data_list = raw_data[1]
                datas_list = []
                datas_list = ServiceKansai.input_data(data_list)

            start_date = datetime.date(2019, 4, 1)
            end_date = datetime.date(2020, 2, 29)
            m_period = (end_date.year - start_date.year) * 12 + \
                       (end_date.month - start_date.month)
            month_list = []
            month_list.append(start_date)
            for m in range(m_period):
                month_list.append(month_list[m] + relativedelta(months=1))

            if area == 'Tokyo':
                print('東京電力の需給割合')
                tokyo_data = []
                for month in month_list:
                    sum_month_tokyo = Service.sum(datas_list, month)
                    percentage_month_tokyo = Service.percentage(sum_month_tokyo)
                    # Service.display_month(percentage_month_tokyo)
                    tokyo_data.append(Service.dict(percentage_month_tokyo))
                print(tokyo_data)

            if area == 'Kansai':
                # print('関西電力の需給割合')
                kansai_data = []
                for month in month_list:
                    sum_month_kansai = ServiceKansai.sum(datas_list, month)
                    percentage_month_kansai = ServiceKansai.percentage(sum_month_kansai)
                    # ServiceKansai.display_month(percentage_month_kansai)
                    kansai_data.append(Service.dict(percentage_month_kansai))


        for tokyo_datum in tokyo_data:
            Service.max_sort(tokyo_datum)

        # PowerSupplyAnalyzer.compare(2019/4, percentage_month_Tokyo, percentage_month_Kansai)