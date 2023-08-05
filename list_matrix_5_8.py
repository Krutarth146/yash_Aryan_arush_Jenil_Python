list5 = [30,21,90,44,32,21,1]

ans = [[30,30], [30,21], [30,90]]

c = 0
javab =  []

for k in list5:   # k = 30
    for j in list5:  # j = 90
        javab.append([k,j])
        c+=1

print(javab)
print(c)


# ----------------------------------------------------

# List Matrices

list1 = [[10,90,89], 
         [43,98,31], 
         [55,66,33]]


print(list1)   # [[10, 90, 89], [43, 98, 31], [55, 66, 33]]
print(list1[1])   # [43, 98, 31]
print(list1[1][1])   # 98
print(list1[1][-2])   # 98
# print(list1[1][-2])   # [98]
# print(list1[1:][2:0:-1])   # [[55, 66, 33]]
# print(list1[1:][2])   # 

# import numpy as np

# list1 = np.array(list1)

# print(list1[1:,2:0:-1])


# list1 = [10,0,304,450]

# # print(list1[start : end(n-1) : step(n-1)])
# print(list1[1:3:1])   # [0, 304]



list1 = [[10,90,89], 
         [43,98,31], 
         [55,66,33]]


for sublist in list1:   # i = [10,90,89]
    for ele in sublist:
        print(ele,end=' ')   # 10 90 89 43 98 31 55 66 33


# for row in range(3):
for row in range(len(list1)):
    print(list1[row])

for row in range(len(list1)):   # 0 to 2   # row = 0
    for col in range(len(list1[row])):  # 0 to 2  # col = 1
        print(list1[row][col])  # list1[0][1]



list1 = [[10,90,89], 
         [43,98,31], 
         [55,66,33]]


# Transpose
for row in range(len(list1)):   # 0 to 2   # row = 0
    for col in range(len(list1[row])):  # 0 to 2  # col = 1
        print(list1[col][row])  # list1[1][0]   # 10  43



# 10 + 98 + 33  = ?
sum = 0
for row in range(len(list1)):   # 0 to 2   # row = 0
    for col in range(len(list1[row])):  # 0 to 2  # col = 1
        if row == col:
            sum += list1[row][col]


print(sum)   # 141

# 89 + 98 + 55  = ?