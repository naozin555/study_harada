import re
import datetime
from dateutil.relativedelta import relativedelta

from serve import Serve


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
        datas_list = Serve.input_data(data_list)

        start_date = datetime.date(2019, 4, 1)
        end_date = datetime.date(2020, 3, 31)
        d_period = (end_date - start_date)
        m_period = int(int(d_period.days) / 30)
        month_list = []
        month_list.append(start_date)
        for m in range(m_period-1):
            month_list.append(month_list[m] + relativedelta(months=1))

        for month in month_list:
            sum_month = Serve.sum_month(datas_list, month)
            percentage_month = Serve.percentage_month(sum_month)
            Serve.display(percentage_month)

