str4 = "Yash is Good Boy123."

# Indexing
print(str4[2])   # s
print(str4[-2])  # 3

# Slicing

print(str4[3:8])  # h is 
print(str4[8:3:1])  # No ans
print(str4[-8:-2:2])  #  o1

str4 = "Yash is."
print(str4[3:-4:-1])  # 
print(str4[::])  # Yash is.
print(str4[::-1])  # .si hsaY
print(str4[:-5:-2])  # .i
print(str4[:-5:2])  # .i


# str1 = input().strip()[::-1]
# str1 = input()

# str6 = ""


# for i in str1[::-1]:
#     str6+=i

# print(str6)

# print(str1)   # letaP lineJ

# print(str1 + "Hello")

# str1 = str1 + "Hello"

# str1 += " Manoj Hello"
# print(str1)


# List Methods

str4 = "Yash_is good Boy123."

print(str4.capitalize())   # Yash_is good boy123.
print(str4.title())   # Yash_Is Good Boy123.
print(str4.upper())   # YASH_IS GOOD BOY123.
print(str4.lower())   # yash_is good boy123.
print(str4.swapcase())   # yASH_IS GOOD bOY123.
print(str4.casefold())   # yash_is good boy123.
print(str4.istitle())   # False
print(str4.isupper())   # False
print(str4.islower())   # False

# print(str4[:8]+str4[8:11].upper()+str4[11:])

# res = ""

# for i in range(len(str4)):
#     if i % 2 == 0:
#         res+=(str4[i].upper())
#     else:
#         res+=(str4[i].lower())

# print(res)
# str1 = "123"
# str1 = "234"

# print(str1)


str4 = "Yash_is good Boy123."

print(len(str4))   # 20
print(min(str4))   # space (32)
print(max(str4))   # y (121)
print(str4.center(26,'*'))   #    Yash_is good Boy123.

print(str4.count("o"))    # 3
print(str4.count("o",11,13))    # 0

# print(str4.find("z"))    # -1
print(str4.find("o"))    # 9
print(str4.rfind("o"))    # 14
# print(str4.index("z"))    # Generates an Error