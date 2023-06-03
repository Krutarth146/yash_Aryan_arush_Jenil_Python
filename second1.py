# x = int(input("Enter first Number: "))
# y = int(input("ENter Second Number: "))
# print(f"{x} + {y} = {x+y}")   # fstring
# print(f"{x} - {y} = {x-y}")
# print(f"{x} * {y} = {x*y}")
# print(f"{x} / {y} = {x/y}")   # return in float  # 12.5
# print(f"{x} // {y} = {x//y}")  # retrun floor    # 12
# print(f"{x} % {y} = {x%y}")   # Remainder 1
# print(f"{x} ** {y} = {x**y}")   # 625


# Typecasting -> one datatype to another Datatype

# 1. IMplicit Typecasting
# 2. Explicit Typecasting


x = True  # 1
y = 234  

print(x+y)   # 235   # Implicit Typecasting

x = '34'
print(int(x))   # 34

f = "21.90"
print(int(float(f)))   # 21   # Explicit Typecasting

e = 90.01
import math

print(math.floor(e))  # 90
print(math.ceil(e))   # 91