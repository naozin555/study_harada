import re
import datetime
from dateutil.relativedelta import relativedelta

from service import Service


class Controller(object):

    def execute(self):
        with open(self, 'r') as f:

            header = ''
            data_list = []

            for line in f:

                if re.search('供給力$', line):
                    header = line.strip()[:-4]

                if re.search('^,,,', line):
                    header = header + line.strip()[2:]

                if ':' in line:
                    data_list.append(line.strip())

        datas_list = []
        datas_list = Service.input_data(data_list)

        start_date = datetime.date(2019, 4, 1)
        end_date = datetime.date(2020, 3, 31)
        m_period = (end_date.year - start_date.year) * 12 + \
                   (end_date.month - start_date.month)
        month_list = []
        month_list.append(start_date)
        for m in range(m_period):
            month_list.append(month_list[m] + relativedelta(months=1))
        print(month_list)

        for month in month_list:
            sum_month = Service.sum_month(datas_list, month)
            percentage_month = Service.percentage_month(sum_month)
            Service.display(percentage_month)
