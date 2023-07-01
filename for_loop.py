# for i in range(start, end, step)


for i in range(10):
    print(i,end=' ')  # 0 1 2 3 4 5 6 7 8 9 

print()

for j in range(1,11):
    print(j,end=' ')  # 1 2 3 4 5 6 7 8 9 10 

print()


for j in range(2,10,1):
    print(j,end=' ')  # 2 3 4 5 6 7 8 9
print()


for j in range(2,10,2):
    print(j,end=' ')  # 2 4 6 8
print()


for k in range(10,3,1):
    print(k)  # No O/p
print()

for w in range(-5):
    print(w,end=' ')  # blank

print()

for t in range(-9,-2,2):
    print(t,end=' ')  # -9 -7 -5 -3

print()

for w in range(10,1,-1):
    print(w,end=' ')   # 10 9 8 7 6 5 4 3 2

print()

for g in range(-3,5,2):
    print(g,end=' ')  # -3 -1 1 3

print()

for j in range(-10,-2,-3):
    print(j)   # No o/p

print()

for j in range(3,-5,-2):
    print(j,end=' ')  # 3 1 -1 -3
print()
print()
print()
print()
for j in range(4,5,-1):
    print(j,end=' ')  # no o/p


# ----------------------
# List --------------

list1 = []

print(list1)
print(type(list1))  # <class 'list'>
print(list1.__sizeof__())  # 40
print(len(list1))  # 0

l1 = [10,0,10,20,30, 90.89, "Str1", [10,20,30, (3040,50)], (30,30), {10,20,30,40,10,10}, {"Name" : "Aarush", 'Address' : [10,20,30,40]}]
print(l1)  # [10, 0, 10, 20, 30, 90.89, 'Str1', [10, 20, 30, (3040, 50)], (30, 30), {40, 10, 20, 30}, {'Name': 'Aarush', 'Address': [10, 20, 30, 40]}]

print(len(l1))  # 10
print(all(l1))  # False
print(any(l1))  # True

# Indexing

list1 = [10,20,30,40,50,60,90,80]
print(list1[-1])  # 80
print(list1[1])  # 20

# Slicing

# print(list1[start : end (n-1): step (n-1)])

print(list1[0:5])  # [10, 20, 30, 40, 50]
print(list1[3:8:1])  # [40, 50, 60, 90, 80]
print(list1[-3:4:2])  # []
print(list1[-3:4:-2])  # [60]