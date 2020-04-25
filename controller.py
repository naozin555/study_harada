import datetime
from dateutil.relativedelta import relativedelta

from service import Service, ServiceKansai


class Controller(object):

    def execute(self):

        if self == 'Tokyo':
            raw_data = Service.file_open('area-2019.csv')
            header = raw_data[0]
            data_list = raw_data[1]
            datas_list = []
            datas_list = Service.input_data(data_list)
            print(datas_list)
        elif self == 'Kansai':
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

        if self == 'Tokyo':
            for month in month_list:
                sum_month = Service.sum_month(datas_list, month)
                percentage_month = Service.percentage_month(sum_month)
                Service.display(percentage_month)
        if self == 'Kansai':
            for month in month_list:
                sum_month = ServiceKansai.sum_month(datas_list, month)
                percentage_month = Service.percentage_month(sum_month)
                Service.display(percentage_month)
