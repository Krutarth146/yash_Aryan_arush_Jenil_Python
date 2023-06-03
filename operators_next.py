# Bitwise O/p  & | ^ << >>

print(45 & 90)  # 8
print(45 | 90)  # 127
print(45 ^ 90)  # 119
print(45 << 2)  # 119
print(45 >> 3)  # 5

# Membership O/p  --> in, not in

# Loops::

# 1. Entry Control Loops  -----> 1. For Loop 2. while Loop

list1 = [10,20,30,40,50,50,90.990,"STr1",'P',True,90+8j,[10,20,30,40], (90,67,12,34), {10,10,10,20}, {"Name" : "Krutarth", 'Roll'  : 900}]

print(list1)


# Linear Search

user_need = True
flag = 0
for w in list1:
    # print(w,end=' ')
    if w == user_need:   # 10 == "True"
        flag=1
        break
    else:
        flag=0

if flag == 1:
    print("Element is Found")


if user_need not in list1:
    print("Element is Found")


# Comparison O/p   == != < > <= >=

num1 = int(input("ENter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num1 > num2:
    if num1 > num3:
        print(f"{num1} is Max")
    else:
        print(f"{num3} is Max")
else:
    if num2 > num3:
        print(f"{num2} is Max")
    else:
        print(f"{num3} is Max")


# Ternary O/p in C (Exp1 ? Exp2 : Exp3)   (a>b ? (a>c ? a : c) : (b > c ? b : c))


print(num1 if num1 > num2 else num2)    # HW  Compare with 3 Numbers
 

# Take 3 Subjects Marks As Input From user and Calc Total, Avg, Grade also  100 to 80 -> A Grade, 80 to 60 -> B Grade, 40 to 60 -> C Grade, Under 40 -> Fail