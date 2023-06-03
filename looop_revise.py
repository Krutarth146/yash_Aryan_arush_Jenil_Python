# Loops ----> 1. Entry control loops

# 1. Entry Control loops ---> 1. for   2. while

# Intialization, End position, Flow (Incre / Decre)

num = 1   # start point

while num <= 10:   # Condition
    print(num,end=' ')   # statements   # 1 2 3 4 5 6 7 8 9 10
    num+=1   # num = num + 1  # Flow


print()

num1 = 25

while num1 <= 80 :
    if num1 % 5 == 0 and num1 % 7 == 0 and num1 % 10 == 0:
        print(num1,end= ' ')  # 70
    num1 += 1

num1 = 25

while num1 <= 80 :
    if num1 % 5 == 0 or num1 % 7 == 0 and num1 % 10 == 0:
        print(num1,end= ' ')  # 25 30 35 40 45 50 55 60 65 70 75 80
    num1 += 1

print()
print()



# Power  Base = 4, Power = 3

# base = int(input())
# power = int(input())
# arya = 1

# i = 1
# while i<= power:
#     arya = arya * base
#     i+=1

# print(arya)



# --------------------------


i = 1

while i<=10:
    print(i)
    if i == 5:
        break
        print("scsdcncsn")
    i+=1

# ---------------------------------

k = 25

while k<= 65:
    if k == 30:
        pass
        # continue
    print(k)
    k+=1

print(k)