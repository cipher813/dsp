import csv
import regex as re



def get_dict():
    with open('faculty.csv','r') as f:
        reader = csv.reader(f,delimiter=',')
        rad = list(reader)
        LN = []
        V = []
        for l in rad[1:]:
            LN.append(l[0])
            V.append(l[1:])
        LN1 =[]
        for s in LN:
            LN1.append(s.strip())
        LN2 = []
        for s in LN1:
            LN2.append(s.split(' ')[-1])
        d = {}
        i = 0
        for s in LN2:
            d[s] = [V[i]]
            i += 1
        print(d)
        return d

get_dict()
