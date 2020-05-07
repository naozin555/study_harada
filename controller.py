import datetime
from dateutil.relativedelta import relativedelta

from service import Service, ServiceKansai, Compare


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
                for month in month_list:
                    sum_month_Tokyo = Service.sum(datas_list, month)
                    percentage_month_Tokyo = Service.percentage(sum_month_Tokyo)
                    Service.display_month(percentage_month_Tokyo)

            if area == 'Kansai':
                print('関西電力の需給割合')
                for month in month_list:
                    sum_month_Kansai = ServiceKansai.sum(datas_list, month)
                    percentage_month_Kansai = ServiceKansai.percentage(sum_month_Kansai)
                    ServiceKansai.display_month(percentage_month_Kansai)

        Compare.compare(2019/4, percentage_month_Tokyo, percentage_month_Kansai)