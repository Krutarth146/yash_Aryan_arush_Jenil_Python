str1 = 'listenn' 
str2 = 'silnent' 

# list1,list2 = [],[]

# for i in str1:
#     list1.append(i)
# print(list1)    # ['l', 'i', 's', 't', 'e', 'n']


# for i in str2:
#     list2.append(i)
# print(list2)    # ['l', 'i', 's', 't', 'e', 'n']

# if sorted(list1) == sorted(list2):
#     print('Anagram')

dict1 = {i:str1.count(i) for i in str1}

list1 = [(i,str1.count(i)) for i in str1]
print(list1)  # ['l', 'i', 's', 't', 'e', 'n', 'n']
                # [1, 1, 1, 1, 1, 2, 2]
                # [('l', 1), ('i', 1), ('s', 1), ('t', 1), ('e', 1), ('n', 2), ('n', 2)]
dict2 = {i:str2.count(i) for i in str2}   # Dict Comprehension

print(dict1)
print(dict2)

if dict1 == dict2:
    print(True)