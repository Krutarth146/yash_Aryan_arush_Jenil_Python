# CSV ---> Comma Seprated Values

# 10,20,30,40

import csv

filename = 'BlackFriday.csv'

fields = []
data = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:
        data.append(row)


    print(csvreader.line_num)