import csv
import random
from more_itertools import flatten
from pprint import pprint
names = {"Grade 9":[],"Grade 10":[],"Grade 11":[],"Grade 12":[]}
with open("students.csv") as f:
    file = csv.reader(f, delimiter=',')
    for row in file:
        names[row[0]].append(row[1])

for grade, name in names.items():
    for n in name:
        new = n.lower().replace(" ", "").split(",")
        name[name.index(n)]= new[1][:2]+new[0]+"@packer.edu"

def get_emails(num):
    final_emails = []
    for grade, emails in names.items():
        final_emails.append(random.sample(emails,k=num))
    final_emails = list(flatten((item) for item in final_emails))    
    print(', '.join(final_emails)) 
    
get_emails(int(input("# of emails from each grade\n>")))
