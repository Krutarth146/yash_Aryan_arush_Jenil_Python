# x = '90'   # Dynamic Lang.  (Runt time Allocation)
# y = 80  # Int
# print(type(x))   # <class 'int'>


# y = input()   # Str

# print(x+y)  # Error


# Typecasting

# x = int(input())   # Explicit T.c
# y = int(input())

# print(x+int(y))   # 90


r = True  # bool
s = 78   # int
print(r+s)  # bool + int   # 79  # Implicit T.C

x = 43.90
print(int(x))  # 43  # Explicit

v = '56'
print(42 + int(v))   # 98

print(chr(32 + ord('A')))  # a 
# print(42 + v)  # Error 


f = '90.98'
print(int(float(f)))  # 90

import math
print(math.floor(90.999999999999999999999))  # 90
print(math.ceil(90.0001))  # 91
print(math.ceil(90.0000))  # 90


print(round(90.90))   # 91
print(round(90.50000000000000000000000000000))   # 90
print(round(90.50, 2))   # 90.5
print(round(90.54, 1))   # 90.5
print(round(90.54, 0))   # 91.0
print(round(90.54, -1))   # 90.0
print(round(90.54, -2))   # 100.0
print(round(4982.54, -2))   # 5000.0

print(34 + 90.42)   # 124.42

# int, float, complex, bool, string, list, tuple, Dict, Set

g = 90 + 4j  # 90 is Real Part, 4j is Imaginary Part

f = 89j

print(g+f)  #  (90+93j)


# if 1:
#     print(True)
# elif 45 > 90:
#     print(False)
#     if []:
#         pass
#     else:
#         pass


num1 = 90
num2 = 670
num3 = 4444

# Maximum

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)

else:
    if num2  > num3:
        print(num2)
    else:
        print(num3)


print(num1 if num1 > num2 else num2)   # 670

print((num1 if num1 > num3 else num3) if num1 > num2 else (num2 if num2  > num3 else num3))  # 4444