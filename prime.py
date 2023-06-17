

# 24 ---> 1,2,3,4,6,8,12,24
# 23 ---> 1, 23
# 29 ---> 1, 29
# 37 ---> 1, 37
# 22 ---> 1,2,11,22 


# num = 28
# print(type(num))

num = int(input())
# print(type(num1))
factors = 0

i = 1
while i <= num:
    if num % i == 0:   # 22 % 2 == 0
        print(i,end=' ')
        factors += 1
    i+=1 


print("Factors = %d" %factors)

if factors == 2:
    print("Prime Number")

