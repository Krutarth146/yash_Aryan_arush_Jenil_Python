str1 = "Aarush is Good"

print(str1.casefold())   # aarush is good

str2 = 'Navrang is\tGood'
print(str2.expandtabs(32))


name = 'Aarush'
surname = 'Patel'

print("{} {} is Good Student".format(name, surname))
print("{1} {0} is Good Student".format(name, surname))
print("{name} {surname} is Good Student".format(name = 'Manoj', surname = 'Patel'))


s = 'MyArmy'
print(s[3] + s[-1])  # ry


import math

print(math.ceil(100.78))  # 101
print(math.floor(100.78))  # 100

# -----------------------------------------------------

# UDF

# def Jenil(x,y,z):
#     print(x+y * z)

# num1, num2 = 90, 80

# Jenil(num1, num2, 90)   # 170


x = 90   # Global Variable


def Aarush():  # Aarush(90)
    # x = 80   # Local Variable
    global x   # Global Variable
    x += 10  # y = 90 ----> x = 100
    print(x)  # 100

Aarush()   # Aarush(90)   # 100
x+=120   # 220
print(x)  # 220



p = 5   # Global
def sum(q,r=2):  # sum(1,5)   
    global p      # p = 105
    p = r+q**2    # p = 6
    print(p,end='#')   # 105#6#


a = 10
b = 5
sum(a,b)  # sum(10,5) 
sum(r=5,q=1)     # 105#6#




# -----------------------------
a = "Hello"

