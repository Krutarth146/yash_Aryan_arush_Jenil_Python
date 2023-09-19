# CSV ---> Comma Seprated Values

# 10,20,30,40


# fp = open('BlackFriday.csv','+ab')
# jenil = open('Manoj.txt','w')   # Overwrite, If file not Found then It will Create a New

# jenil.write("Hello Sam")

# jenil.close()


# jk = open('Manoj.txt','r')   # If file Not FOund then it will create an Error
# print(jk)    # <_io.TextIOWrapper name='Manoj.txt' mode='r' encoding='cp1252'>

# new_data = jk.read()
# print(new_data)   # Hello Sam


# new_data = jk.read()
# print(new_data)
# print(jk.tell())   # 0
# print(jk.readline())
# print(jk.tell())  # 11
# print(jk.readline())
# print(jk.tell())   # 13
# print(len(jk.readline()))  # Aman has 8 Rs. only.
# print(jk.tell())   # 36
# print(len(jk.readline()))  # Aman has 8 Rs. only.
# print(jk.tell())   # 38
# print(jk.readline())  # Aman has 8 Rs. only.
# print(jk.tell())   # 38


# for k in jk.read():
#     print(k)

# jk.seek(0)

# print(jk.readlines())   # ['Hello Sam\n', '\n', 'Aman has 8 Rs. only. \n', '\n', 'Royal Techno\n', '\n', 'Aman University']

# jk.seek(0)

# print(jk.readline(2))   # He


# photo = open('Manoj.txt','rt')

# ans = photo.read()

# list1 = photo.readlines()


# print(list1)   # ['Hello Sam\n', '\n', 'Aman has 8 Rs. only. \n', '\n', 'Royal Techno\n', '\n', 'Aman University']


# photo.seek(0)
# list1 =  photo.readlines()
# print(list1)

# new = []

# for i in list1:
#     if i != '\n':
#         new.append(i)
# print(new)   # ['Hello Sam\n', 'Aman has 8 Rs. only. \n', 'Royal Techno\n', 'Aman University']

# for word in new:
#     # print(word)
#     if word[:2] == 'Ro':
#         print(word)   # Royal Techno

# print(data)
# print(type(data))
# words = []
# for j in list1:
#     words.append(j)

# print(words)

import csv

file_name = 'BlackFriday.csv'

heading = []
data = []

with open(file_name,'r') as csvfile:
    csvreader = csv.reader(csvfile)

    heading = next(csvreader)
    print(heading)   # ['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category', 'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3', 'Purchase']

    for row in csvreader:
        data.append(row)   # ['1004964', 'P0095842', 'M', '36-45', '0', 'A', '1', '1', '3', '4', '12', '7997']

    # print(data)

    print('Total No. of Rows are %d'%(csvreader.line_num))   # 537578
print()

print('feilds are : ' + ', '.join(i for i in heading))


for row5 in data[:5]:
    for col in row5:
        print("%10s"%col,end=' ')
    print('\n')

# list1 = [10,20,30,50,61]

# for i in list1:
#     if i % 2 != 0:  
#         print(i)   # 61

# list2 = [(i,j) for i in list1 for j in list1]
# print(list2)


fields = ['Name', 'Roll', 'Contact', 'School']

rows = [
    ['Aman', 90, 9002, 'Raman'],
    ['Aman', 90, 9002, 'Raman'],
    ['Aman', 90, 9002, 'Raman'],
    ['Aman', 90, 9002, 'Raman'],
    ['Aman', 90, 9002, 'Raman']
]

# [
#     {'Name' : 'Manoj', 'Roll' : 900, 'contact' : 900, 'school' : 'HBK'}
# ]

# filename = 'schoolrecord.csv'

with open('school.csv','w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

# Dictwriter