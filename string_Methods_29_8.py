str2  = "AaRush_is Good Boy123."

print(len(str2))  # 22
print(str2.center(30))   #     AaRush_is Good Boy123.    
print(str2.center(30,'*'))   # ****AaRush_is Good Boy123.****


print(str2.encode())   # b'AaRush_is Good Boy123.'


str5 = "Ståle"

print(str5.encode())   # b'St\xc3\xa5le'

print(str5.encode(encoding="ASCII", errors="replace"))   # b'St?le'
print(str5.encode(encoding="ASCII", errors="backslashreplace"))   # b'St\\xe5le'
print(str5.encode(encoding="ASCII", errors="ignore"))   # b'Stle'
print(str5.encode(encoding="ASCII", errors="xmlcharrefreplace"))   # b'St&#229;le'
print(str5.encode(encoding="ASCII", errors="namereplace"))   # b'St\\N{LATIN SMALL LETTER A WITH RING ABOVE}le'


str2  = "AaRush_is Good Boy123."
print(str2.endswith('23.'))   # True
print(str2.endswith('23'))   # False


str2  = "AaRush_is\tGood Boy123."
print(str2.expandtabs(32))   # AaRush_is                       Good Boy123.


name = 'Manoj'
gender = "Male"


# print("{} is {}.")

num1 = 90
num2 = 80
# print(num1 + num2 = ans)
print("{} + {} = {}".format(num1,num2,num1 + num2))        # 90 + 80 = 170
print("{1} + {0} = {2}".format(num1, num2, num1 + num2))   # 80 + 90 = 170
ans = num1 + num2
print("{num1} + {num2} = {num1}".format(num1 = 30, num2 = 90))   # 80 + 90 = 170

print(f"{num1} + {num2} = {num1 + num2}")   # 90 + 80 = 170


# --------------------


x = '10101'
print(int(x,2))   # 21

print(x.format('b'))   # 10101

print(bin(32))   # 0b100000


# format_map()


dict1 = {"name" : "Aarush", 'mode' : "Good"}

str1 = "{name} is {mode} Boy.".format_map(dict1)

print(str1)   # Aarush is Good Boy.