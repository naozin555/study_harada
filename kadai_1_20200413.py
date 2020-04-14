import re
import csv
import numpy as np

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

# print(header)
# for data in data_list:
#     print(data)

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0, len(l), cols)]


with open('area-2019_a.csv', 'w') as fa:
    fa.write(header + '\n')
    convert_1d_to_2d(data_list, 2)
    writer = csv.writer(fa, lineterminator='\n', delimiter=',')
    writer.writerows(data_list)
