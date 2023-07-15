# Armstrong

# 153 --->  3*3*3   +   5*5*5   +  1*1*1  ===  153 (Armstrong)
# 8208 ---> 8*8*8*8

# 9



num = 371  # ---> 3*3*3
sum = 0
xerox = num

print(id(num))  # 1550812225264
print(id(xerox))  # 1550812225264

# while num != 0:
while num > 0:
    remainder = num % 10   # remainder = 1   
    sum = sum + remainder ** len(str(xerox))  # 27 + 125 + 1 = 153  # 
    num = num // 10   # num = 0


if sum == xerox:
    print("Armstrong")


# Power()

num= 2
power = 90

# Ans. 32---->   2*2*2*2*2
mul = 1

k=1
while k<=power:
    mul = mul * num   # 4 * 2
    k+=1

print(mul)   # 32


# Armstrong --- > 1 to 10000, Factorial, Fibonnacci