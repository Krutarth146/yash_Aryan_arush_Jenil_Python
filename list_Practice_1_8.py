list1 = [30,40,20,10,90,10,10,50]

list1.append(401)
list1.append([401])
print(list1)   # [30, 40, 20, 10, 90, 10, 10, 50, 401, [401]]

list1.extend('Jenil123')

print(list1)  # [30, 40, 20, 10, 90, 10, 10, 50, 401, [401], 'J', 'e', 'n', 'i', 'l', '1', '2', '3']

list1.extend(["Jenil123"])
list1.extend([["Jenil123"]])

print(list1)   # [30, 40, 20, 10, 90, 10, 10, 50, 401, [401], 'J', 'e', 'n', 'i', 'l', '1', '2', '3', 'Jenil123', ['Jenil123']]

# Add --- > Insert, extend, Append

del list1[5:]
print(list1)  # [30, 40, 20, 10, 90]


# Remove ----> pop, pop(index), remove, del
print(list1)   # [30, 40, 20, 10, 90]
list1.pop(3)
print(list1)   # [30, 40, 20, 90]



# list1 = [30, 40, 20, 90, 30,50,30]


# for i in list1:
#     if i == 30:
#         list1.remove(30)

# print(list1)   # [40, 20, 90, 50]

list1 = [30, 40, 20, 90, 30,50,30,30]

# for i in list1:
#     if i == 30:
#         list1.remove(30)

# print(list1)   # [40, 20, 90, 50]

unique = []

for i in list1:
    if i not in unique and i != 30:
        unique.append(i)

print(unique)   # [30, 40, 20, 90, 50]


lst1 = [10,90,34,562,23,12,78,55,11,11]   # Odd nUmbers & their Indexes

# for jenil in lst1:
#     print(jenil,end=' ')   # 10 90 34 562 23 12 78 55 11 11

# # for yash in range(len(lst1)):
# for yash in range(10):  # 0 to 9
#     # print(yash,end=' ')   # 0 1 2 3 4 5 6 7 8 9
#     print(lst1[yash],end=' ')   # 10,90,34,562,23,12,78,55,11,11


for jenil in range(len(lst1)):
    if lst1[jenil] % 2 != 0:
        # ind = lst1.index(lst1[jenil], jenil)

        # print(lst1[jenil], ind)
        print(lst1[jenil], jenil)


list5 = [30,21,90,44,32,21,1]

ans = [[30,30], [30,21], [30,90]]