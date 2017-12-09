import csv
import regex as re



def count_titles(csv_file_name):
    with open(csv_file_name,'r') as f:
        reader = csv.reader(f,delimiter=',')
        rad = list(reader)
        Titles = []
        for l in rad[1:]:
            Titles.append(l[2])
        Titles1 =[]
        for s in Titles:
            s = re.sub(r'[.]', "", s)
            Titles1.append(s.strip().replace('is ','of '))
        d = {}
        for s in Titles1:
            d[s] = 0
        for s in Titles1:
            d[s] += 1
        print(d)
        return d

count_titles('faculty.csv')
