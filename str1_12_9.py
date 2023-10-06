str1 = "Jenil is Good_Boy123."

print(str1.partition(' '))  #  ('Jenil', ' ', 'is Good_Boy123.')
print(str1.split('_'))  # ['Jenil is Good', 'Boy123.']


print(str1.partition('J'))   # ('', 'J', 'enil is Good_Boy123.')
print(str1.split('J'))   # ['', 'enil is Good_Boy123.']


print(len(str1))   # 21
print(str1.ljust(30,'*'))
print(str1.rjust(30,'*'))


str2 = '       Aarush is Good.         '
print(len(str2))   # 31
print(len(str2.rstrip()))     #        Aarush is Good.   # 22
print(len(str2.lstrip()))   # Aarush is Good.   # 24
print(len(str2.strip()))   # Aarush is Good.   # 15



str3 = 'Hello Sam'
table = str3.maketrans('S', 'R', 'o')
print(table)   # {83: 82, 111: None}

print(str3.translate(table))   # Hell Ram

print(str3)   # Hello Sam
print(str3.replace("Sam", "Sita Ram",1))   # Hello Sita Ram

