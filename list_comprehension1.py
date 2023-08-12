# List Comprehension

list1 = [10,90,67,43,21,89]
square = []

for i in list1:
    # square.append(i*i)
    square.append(i**2)

print(square)  # [100, 8100, 4489, 1849, 441, 7921]

# list1[0] = list1[0] * list1[0]
# print(list1)

res = [i for i in list1]
print(res)   # [10, 90, 67, 43, 21, 89]

res = [i*10 for i in list1]
print(res)   # [10, 90, 67, 43, 21, 89]

res = [i*i for i in list1]
cube = [i**3 for i in list1]
print(cube)   # [100, 8100, 4489, 1849, 441, 7921]


# list1 = [21,90,44,55,33,42,32]

# for i in range(len(list1)):
#     if list1[i] % 2 != 0:
#         print(i)   # 0 3 4

# l1 = [list1.index(i) for i in list1 if i % 2 != 0]


# list1 = [10,90,67,43,21,89]


# print(l1)   # [(0, 10), (1, 90), (2, 67), (3, 43), (4, 21), (5, 89)]


jenil = [[x,b] for x in list1 for b in list1]

print(jenil)


for x in list1:   # x = 10
    for b in list1:   # b = 67
        print([x,b])  # [10,67]


l2 = [40,90,566,43,21]
l6 = [11,90,22,3121,23]


# [(40,11), (90,90), (566,22)]
res= []

for i in range(len(l2)):
    res.append((l2[i], l6[i]))

print(res)  # [(40, 11), (90, 90), (566, 22), (43, 3121), (21, 23)]

l2 = [40,90,566,43,21]
l6 = [11,90,22,3121,23]


for i,j in zip(l2,l6):
    print(i)