list1 = [[10,90,89], 
         [43,98,31], 
         [55,66,33]]


# print(len(list1))   # 3
# print(list1[0])  #    [10, 90, 89]
# print(len(list1[0]))  # 3


# for sublist in list1:   # i = [10, 90, 89]
#     for k in sublist:
#         if k % 2 != 0:
#             print(k,end=' ')


list1 = [[10,90,89], 
         [43,98,31], 
         [55,66,33]]


for row in range(len(list1)):    # 3  ---> 0,1,2   # list1[0] = [10,90,89]
    for col in range(len(list1[row])):  # 3  ---> 0,1,2   
        # print(list1[row][col])   # list1[1][0]
        if row == col:
            print(list1[col][row])   # list1[1][0]

    
print(list1[0])


for row in range(len(list1)):
    print(list1[row][len(list1) - 1 - row])   # list1[0]     [10, 90, 89]   [43, 98, 31]   [55, 66, 33]
  


list1 = [10,20,30,40]

for i in list1:
    a = str(list1)
    print(a)
    print(a[3])   # ,
    print(type(a[3]))   