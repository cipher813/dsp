import csv
import regex as re

def count_degrees(csv_file_name):
    with open(csv_file_name,'r') as f:
        reader = csv.reader(f,delimiter=',')
        rad = list(reader)
        # print(type(rad))
        # print(rad)
        Degrees = []
        for l in rad[1:]:
            Degrees.append(l[1])
        Degrees1 =[]
        for l in Degrees:
            l = re.sub(r'[.]', "", l)
            Degrees1.append(l.strip().split())
        # print(Degrees1)
        Degrees2 = []
        for l in Degrees1:
            for e in l:
                Degrees2.append(e)
        d = {}
        for s in Degrees2:
            d[s] = 0
        for s in Degrees2:
            d[s] += 1
        print(d)
        return d

count_degrees('faculty.csv')
