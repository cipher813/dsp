import csv
import regex as re



def emails(csv_file_name):
    with open(csv_file_name,'r') as f:
        reader = csv.reader(f,delimiter=',')
        rad = list(reader)
        Emails = []
        for l in rad[1:]:
            Emails.append(l[3])
        print(Emails)
        return Emails

emails('faculty.csv')
