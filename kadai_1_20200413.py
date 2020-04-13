
count = 0

with open('area-2019_a.csv', 'w+') as fa:
    with open('area-2019.csv', 'r') as f:
        for line in f:
            count += 1
            if count == 2:
                l2 = line.strip()
                # print(l2)
            if count == 3:
                # ,を削除して結合
                l3 = l2 + line.strip()[2:]
                # print(l3)
                fa.write(l3)
            if count == 4:
                fa.write(line)
                break
