# String  -----> Immutable (Not Changeble), Ordered (Indexed)


str1 = "Aman"
str2 = 'n'
str3 = '''Amano'''

print(type(str1), type(str2), type(str3))   # <class 'str'> <class 'str'>

list1 = [10,20,340]
list1[2] = 900


print(list1)   # [10, 20, 900]


str1 = "Jenil"

# str1[2] = 'm'
# print(str1)   # TypeError: 'str' object does not support item assignment

print(str1[-2])   # i

# print(str1.replace('n', 'm'))   # Jemil


print(id(str1))
str1 = str1.replace('n','m')

print(id(str1))
print(str1)


# Ordered (Indexed)

str1 = "Royal_Techno123."

# Indexing
print(str1[3])  # a
print(str1[-3])  # 2

# Slicing

print(str1[2], [5], {"Name" : 90}, 90, "str1",sep="_-_",end=', ')   # y [5] {'Name': 90} 90 str1

print("Aman")

print(str1[3:6])   # al_
print(str1[-6:-9])   # blank
# print(str1[start: End (n-1) : step(n-1)])   # blank
print(str1[-6::-1])   # nhceT_layoR
print(str1[-6::1])   # no123.

tr1 = "Royal_Techno123."
print(str1[-6:-1:-1])   # 
print(str1[-6:1:-1])   # nhceT_lay


for i in range(-6,1,-1):
    print(i)


tr1 = "Royal_Techno123."
print(tr1[6:-9:-1])   # blank


print(tr1[::-1])   # .321onhceT_layoR
print(tr1[:0:-1])   # .321onhceT_layo



str3 = 'the lion is the king the the the of the Jungle.'

ans = 'a lion is the king of a Jungle'

# i = 1

# for j in range(1,11,1):
#     print(j)

# print(str3.replace('the','a'))      # a lion is a king of a Jungle.
# print(str3.replace('the','a',1))    # a lion is the king of the Jungle.
# print(str3.replace('the','a',-1))   # a lion is a king of a Jungle.



str3 = 'the lion is the king the the the of the Jungle.'

list1 = str3.split(' ')

print(list1)   # ['the', 'lion', 'is', 'the', 'king', 'the', 'the', 'the', 'of', 'the', 'Jungle.']

for i in range(len(list1)):
    if list1[i] == 'the':
        list1[i] = 'a'
        break

for i in range(len(list1)):
    if list1[i] == 'the':
        list1[i] = 'a'
        break


for i in range(len(list1)-1 , -1 , -1):
    # print(list1[i])
    if list1[i] == 'the':
        list1[i] = 'a'
        break

print(list1)   # ['a', 'lion', 'is', 'the', 'king', 'the', 'the', 'the', 'of', 'a', 'Jungle.']


str1 = ' '.join(list1)

print(str1)   # a lion is the king the the the of a Jungle.