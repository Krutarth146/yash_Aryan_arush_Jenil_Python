# Python is Dynamic Lang.

x = 90  # int
print(x)  # 90

y = 80


# Operators

# 1. Arithmetic Operators  + - * / // % **

x = 25
y = 2

print(x+y) # 170
print(f"{x} + {y} = {x+y}") # 90 + 80 = 27
print(f"{x} - {y} = {x-y}") # 90 + 80 = 23
print(f"{x} * {y} = {x*y}") # 90 + 80 = 50
print(f"{x} / {y} = {x/y}") # 90 + 80 = 12.5  (float)
print(f"{x} // {y} = {x//y}") # 90 + 80 = 12 (floor)
print(f"{x} % {y} = {x%y}") # 90 + 80 = 1
print(f"{x} ** {y} = {x**y}") # 90 + 80 = 625
# print(x,'+',y,'=',x+y) # 90 + 80 = 170


print('Hello',end=' ')
print("Arya")


x = 90
y = 70
z = 73

print(x,y,z,sep='\n')   # 90 70 73


print(-18 // 4)  # -5

# 2. Assignment O/p   =  += -= *= /= //= %= <<= >>= &= |= ^=  (Low Priority)

x = 90
x += 10   # x = x + 10   # 100
x /= 10   # 10.0 
x += 123  # 133.0
x %= 2    # 1.0
x -= 10   # -9.0
print(x)  # -9.0

print(2**3**2)   # 512


# Bitwise O/p   & | ^ << >>

# AND Table (A*B*C)

# i/p  i/p  o/p
#  0    0    0
#  0    1    0
#  1    0    0
#  1    1    1

# OR Table (A+B+C)

# i/p  i/p  o/p
#  0    0    0
#  0    1    1
#  1    0    1
#  1    1    1

# XOR Table (Same = 0)

# i/p  i/p  o/p
#  0    0    0
#  0    1    1
#  1    0    1
#  1    1    0


# 390  ---> 0101010101
# A    ---> Ascii (65) -----> 01010101

print(ord('A')) # 65
print(chr(97)) # 65


# Dec  ----> bin

# 4508 , 34011,  7771, 707, 11


# Bin to Dec

# 10101111   10001  111101  101  1010  1000


# Matplotlib