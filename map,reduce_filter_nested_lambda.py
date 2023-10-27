# Nested Lambda

jenil = lambda x,y = 20 : lambda a,b : (x+a) * (y+b)

aarush = jenil(10,20)

print(aarush(90,80))  # 10000

print(jenil(10)(40,50))   # 3500

# ----------------------------------------------------


# jenil = lambda x,y = 20 : lambda a,b : (x+a) * (y+b)

# ----------------------------------------------------------------

# Map :--------------------

num = 90

def square(num11):
    return num11 ** 2

def square1(num11):
    return num11 ** 2

print(square(num))  # 8100


list1 = [10,90,45,32,566,78]

for i in list1:
    print(square(i))


x = map(square, list1)
print(x)

sq = list(map(square1, list1))
print(sq)   # [100, 8100, 2025, 1024, 320356, 6084]

cube = list(map(lambda x:x**3, list1))
cube = list(map(lambda x:(x**3) + 500, list1))
print(cube)   # [1000, 729000, 91125, 32768, 181321496, 474552]


list1 = ['12', '23', '12', '90']

aarush = list(map(int, list1))
print(aarush)   # [12, 23, 12, 90]


# total_inputs = int(input())

# for i in range(total_inputs):
#     x = int(input())
#     print(x)

# x1 = list(map(int, input().strip().split('_')))

# print(x1)   # [10, 23, 24, 77]


# Filter -------------------------

list1 = [213,732,90,32,78.67]

aarush = list(filter(lambda x: x % 2 ,list1))
print(aarush)   # [213, 78.9]  # Truth Values


aarush = list(map(lambda x: int(x) % 2 == 0 ,list1)) 

print(aarush)   # [213, 78.9]


op = list(filter(lambda x : x> 500 , list1))
print(op)  # [732]


# Reduce :---------------------

list1 = [10,20,30,44,55]


from functools import reduce

list1 = [102,34,22,21,31]

addition = reduce(lambda a,b : a+b, list1)
print(addition)   # 210


from itertools import accumulate

x1 = list(accumulate(list1, lambda a,b : a+b))
print(x1)   # [102, 136, 158, 179, 210]