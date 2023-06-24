# Perfect

# 28 ---> 1,2,4,7,14
num = 28
sum = 0

for i in range(1,num):   # 1 to 1=27
    if num % i == 0:
        sum += i

print(sum)   # 28

if sum == num:   # 28 == 28
    print("Perfect Number")


# Print Reverse Numbers

num = 974  # ----> 479

# while num > 0:
while num != 0:
    remainder = num % 10   # rem = 9
    print(remainder,end='')  # 479
    num = num // 10  # 0

print()
# Sum of Digits

num = 974  # ----> 479
sum = 0
# while num > 0:
while num != 0:
    remainder = num % 10   # rem = 9
    if remainder % 2 != 0:
        sum = sum + remainder  # sum = 20
    num = num // 10

print(sum)  # 16


print()
# 

num = 122 
jenil = 0

xerox = num 
# while num > 0:
while num != 0:
    remainder = num % 10   # 9
    jenil = jenil * 10 + remainder   # 479
    num = num // 10   # num = 0

print(jenil)  # 121

list1 = []

list1.append(jenil)


# if xerox == list1[0]:   # 0 == 121
if xerox == jenil:   # 0 == 121
    print("Palindrome Number")


# Armstrong Number

print()
# 

num = 153   #  3*3*3 + 5*5*5 + 1*1*1 = 153  # 8208 ---> 8*8*8*8 + 0 + 2*2*2*2 + 8*8*8*8
jenil = 0

xerox = num 

while num != 0:
    remainder = num % 10   # 9
    jenil = jenil + remainder ** len(str())   # 479
    num = num // 10   # num = 0

print(jenil)
