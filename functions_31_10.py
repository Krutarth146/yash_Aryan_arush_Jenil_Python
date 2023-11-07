# def Dhrav():  # User Deifned Function   # Func. Defination
#     print("Dhrav Function")


# print("sdvsfvfd")
# print("sdvsfvfd")
# print("sdvsfvfd")
# print("sdvsfvfd")
# print("sdvsfvfd")

# Dhrav()   # Func. Calling
# Dhrav()   # Func. Calling
# Dhrav()   # Func. Calling



# print(), len(), max(), input() ----> Python inbuilt

# ----------------------------------


# without Return Type and without Arguments
def Aaryan():
    a,b = 10,2

    print(a**b)  # 10 * 10


Aaryan()   # 100

# ----------------------------------------


# without Return Type and without Arguments
def Aaryan(a,b):

    print(a**b)  # 10 * 10
    return 106


x = 90
y = 3
Aaryan(x, y)   # 729000
print(Aaryan(x, y))   # 729000 106

g = Aaryan(x,y)
print(g)  # # 729000 106
 

# ---------------------------------------------------


def royal(n1 = 34, n2 = 0):   # Default Function
    print(n1+n2)


royal(10,20)  # 30
royal(45)   # 45
royal()   # 34
royal(3,9)   # 12


def techno(a1, *args, a3= None):
    print(args)   # (10, 20, 30, 40, 506, [10, 20])  Tuple  6

    for i in args:
        print(i)

    print(args[-1][-1])   # 20

techno(10,20,30,40,506,[10,20])   # (10, 20, 30, 40, 506, [10, 20])