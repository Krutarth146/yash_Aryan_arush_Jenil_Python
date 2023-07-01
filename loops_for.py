# Prime Number

# 23 ---> 1,23
# 24 ---> 1,2,3,4,6,8,12,24
# 29 ---> 1,29
# 2  ---> 1,2
# start = int(input())
# end = int(input())


# num = 29
# counter = 0

# i = 1
# while i<=num:
#     if num % i == 0:
#         print(i)
#         counter+=1
#     i+=1

# print(counter)

# if counter == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")


# 1 to 10000


for j in range(10):   # start = 0, End = 10 (n-1) 9
    print(j,end=' ')  # 0 1 2 3 4 5 6 7 8 9
print()

for g in range(5,26):
    print(g,end=' ')   # 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25


print()

for ayush in range(1,101,1):
    print(ayush,end=' ')
print()

for ayush in range(1,101,2):  # start - 1, End - 100, step - 2(n-1) = 1
    print(ayush,end=' ')   # 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31 33 35 37 39 41 43 45 47 49 51 53 55 57 59 61 63 65 67 69 71 73 75 77 79 81 83 85 87 89 91 93 95 97 99

for gh in range(20,10,-1):
    print(gh,end=' ')


#  --------------------------------------

# Prime Number

print()
print()
print()
for num in range(1, 100):  
    counter = 0   # num = 24

    i = 1
    while i<=num:    # 1 <= 24
        if num % i == 0:  # 25 %  == 0
            counter+=1
        i+=1


    if counter == 2:
        print(num,end= ' ')


# Palindrome, Armstrong, Perfect, Sum of Digits, Sum of Numbers, Twin, Factroial, Fibonnaccii,
#  POwer, TOtal Count of Numbers

# num = 3, step = 4

# 3
# 33
# 333
# 3333
# 33333