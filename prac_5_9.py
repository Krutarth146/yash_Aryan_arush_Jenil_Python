list1 = [10,90,89,45,32,35,67]


# for i in range(7):  # 7  ---> 0 to 6
# for i in range(0,7):  # 7  ---> 0 to 6

# for i in range(len(list1)-1):  # 6  ---> 0 to 5
#     for j in range(i+1,len(list1)): # 
#         if list1[i] > list1[j]:
#             list1[i], list1[j] = list1[j], list1[i]
# print(list1)


# x,y,z = 10,20,30



# # Linear Search
# list1 = [10, 32, 35, 45, 67, 89, 90]

# # list1 = "A","M","a","n"

# ele = input()
# print(list1)
# for i in list1:
#     if i == ele:
#         print("Element is Found")
#         break
# else:
#     print('Not Found')





list1 = [10, 32, 35, 45, 67, 89, 90]

ele = int(input())

min = 0
max = len(list1)-1



while min <= max:
    mid = (min + max) // 2

    if list1[mid] == ele:
        print("Element is Found")
        break
    elif ele > list1[mid]:
        min = mid + 1
    elif ele < list1[mid]:
        max = mid - 1
else:
    print("Not Found")


print(list1.index(ele))