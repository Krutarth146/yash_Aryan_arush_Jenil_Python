list1 = [10,20,30,555,66,32, 30,30]

print(list1)  # [10, 20, 30, 555, 66, 32]
print(sum(list1))   # 713
print(len(list1))   # 6

print(all(list1))   # True
print(any(list1))   # True

print(min(list1))  # 10

list4 = ['Yash', 'Jenilllllll']
print(max(list4))   # Yash


list1.append('str1')
list1.append(500)

print(list1)  # [10, 20, 30, 555, 66, 32, 30, 30, 'str1', 500]
list1.append(list4)
print(list1)  # [10, 20, 30, 555, 66, 32, 30, 30, 'str1', 500, ['Yash', 'Jenilllllll']]


# list1.extend(10)
# print(list1)   #  'int' object is not iterable

list1.extend("str3")
print(list1)   # [10, 20, 30, 555, 66, 32, 30, 30, 'str1', 500, ['Yash', 'Jenilllllll'], 's', 't', 'r', '3']


l4 = ['str1', 90, 89]

# list1.append(l4)
# print(list1)    # [10, 20, 30, 555, 66, 32, 30, 30, 'str1', 500, ['Yash', 'Jenilllllll'], 's', 't', 'r', '3', ['str1', 90, 89]]
# print(len(list1))  # 16

list1.extend(l4)
print(list1)   # [10, 20, 30, 555, 66, 32, 30, 30, 'str1', 500, ['Yash', 'Jenilllllll'], 's', 't', 'r', '3', 'str1', 90, 89]
print(len(list1))   # 18


# del list1

del list1[5:]
print(list1)   # [10, 20, 30, 555, 66]

list1.insert(1,500)

print(list1)   # [10, 500, 20, 30, 555, 66]

list1.insert(-1, 432)
print(list1)   # [10, 500, 20, 30, 555, 432, 66]



list1[-1] = 900
print(list1)  # [10, 500, 20, 30, 555, 432, 900]



list1.pop()
print(list1)  # [10, 500, 20, 30, 555, 432]

x = list1.pop(3)
print(x)   # 30

print(list1)   # [10, 500, 20, 555, 432]

list1.remove(500)

print(list1)   # [10, 20, 555, 432]


list2 = list1.copy()   # Shallow Copy
print(list2)   # Xerox


list3 = list1   # Digilocker   # Deep Copy
 
list1.append(9100)
print(list1,list2,list3)  # [10, 20, 555, 432, 9100] [10, 20, 555, 432] [10, 20, 555, 432, 9100]

list3.append(3021)
print(list1)   # [10, 20, 555, 432, 9100, 3021]

list1.sort()
# print(list1)   # [10, 20, 432, 555, 3021, 9100]

# list1.reverse()
# print(list1)   # [9100, 3021, 555, 432, 20, 10]

list1.sort(reverse=True)
print(list1)   # [9100, 3021, 555, 432, 20, 10]


list1 = [[10,20], [40,590], [40,1], [22,31]]

list1.sort()

print(list1)  # [[10, 20], [22, 31], [40, 1], [40, 590]]
c = 0


# for i in range(len(list1)):   # 4 ---> 0 to 3
#     for j in range(i+1, len(list1)):   # 
#         if list1[i][1] > list1[j][-1]:  # list1[0][1]
#             list1[i], list1[j] = list1[j], list1[i]
#         c+=1

# print(list1)   # [[40, 1], [10, 20], [22, 31], [40, 590]]
# print(c)   # 6


# -------------------------------------
def sort_1(tup1):
    return tup1[-1]


list1.sort(key=sort_1)
print(list1)   # [[40, 1], [10, 20], [22, 31], [40, 590]]