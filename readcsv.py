import csv
import re

file = csv.reader(open('Email_Telefone_Dandan.csv', 'r'))
header = sorted(next(file))
print(header)
print('')
for row in file:
    email, phone, _id = row
    # print(row)
    print(email, phone, _id)
