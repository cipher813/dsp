import csv

def write_to_csv(list_of_emails):
    with open('emails.csv','w',newline='') as csvfile:
        f = csv.writer(csvfile)
        f.writerows(['baloney'])
        f.writerows([r] for r in list_of_emails)

write_to_csv(['bellamys@mail.med.upenn.edu','warren@upenn.edu','branma@upenn.edu'])
