# List Methods

list1 = [10,20,90,80,70,60]

# Indexing
print(list1[-2])  # 70
print(list1[4])  # 70
print(list1[1])  # 20
print(type(list1[1]))  # int

# Slicing
# print(list1[start : end(n-1) : step(n-1)])

list1 = [10,20,90,80,70,60,70,80,90]
print(list1[1:5])  # [20,90,80,70]
print(list1[4:5])  # [70]
print(type(list1[4:5]))  # list
print(list1[-2:-5])   # []
print(list1[-5:-2])   # [70,60,70]
print(list1[-1:-2])   # [70,60,70]
print(list1[::])   # [10, 20, 90, 80, 70, 60, 70, 80, 90]
print(list1[::2])   # [10, 90, 70, 70, 90]
print(list1[:5:])   # [10, 20, 90, 80, 70]
print(list1[-6::])   # [80, 70, 60, 70, 80, 90]
print(list1[-6:-1:])   # [80, 70, 60, 70, 80]
print(list1[-6:-1:1])   # [80, 70, 60, 70, 80]
print(list1[-6:-1:3])   # [80, 70]
print(list1[-1:-4:3])   # []
print(list1[-1:-4:-1])   # [90, 80, 70]
print(list1[-1::])   # [90]
print(list1[-1::-1])   # [90, 80, 70, 60, 70, 80, 90, 20, 10]
print(list1[-1:0:-1])   # [90, 80, 70, 60, 70, 80, 90, 20, 10]
print(list1[-1:0:1])   # []
print(list1[4:-4:])   # [70]
print(list1[4:-4:-1])   # []


list1 = [10,20,90,80,70,60,70,80,90]
print(list1[-3:3:2])    # []

for j in range(-3,3,2):
    print(j)   # -3 -1 1

print(list1[4:-3:1])   # [70, 60]
print(list1[-7:-2:])   # [90, 80, 70, 60, 70]
print(list1[4:-4:-1])   # [90, 80, 70, 60, 70]
print(list1[-2:-6:-1])   # [80, 70, 60, 70]
print(list1[-2:-6:-2])   # [80, 60]
print(list1[-2:-6:2])   # []
print(list1[::1])   # [10,20,90,80,70,60,70,80,90]
print(list1[::-1])   # [90, 80, 70, 60, 70, 80, 90, 20, 10]
print(list1[-3::-1])   # [70, 60, 70, 80, 90, 20, 10]
print(list1[-3:0:-1])   # [70, 60, 70, 80, 90, 20]