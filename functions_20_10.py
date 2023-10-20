# # # in C ---> 1. Func. Defination  2. Func. Calling   3. Func. Defination

# # void play();  // Func. Declaration

# # void play()   // Func. Defination
# # {
# #     // Statements
# # }


# # main()
# # {
# #     printf();  // Inbuilt
# #     play(); // Func. Calling
# # }


# # 1. Func. Defination
# # 2. Func. calling

# # Truthy Values ----> 10, -10, 1, True, [10,20], "Manoj"
# # Falsy Values  ----> [] , '', 0, False

# x = 45   # Global

# def jenil(age):
#     a,b = 90, 80
#     global x
#     # x = 30
#     x-=1   #   44
#     print(x)  # 44
#     return x 
#     # return [10,20,30] if age >= 18 else ''
# print(x)  # 45

# def Give_money(money, birthyears):
#     if jenil(birthyears):
#         print(money)
#     else:
#         print(money-50)


# print(x)   # 44
# # jenil()   # 170
# # print(jenil())   # 170  None

# Give_money(100, int(input()))



def Example(a1=78,a2=12,a3=21, a4 = None, *args):   # Default Function
    print(a1+a2+a3)

# Example(10)   # 43
# Example(45,90)  # 156

def kru(n1,n2,*args,n4=None):
    print(args)
    print(type(args))  # Tuple
    print(args[-1][-1])  # 20

    sum = 0
    for i in args[:-1]:
        sum += i
    return sum
 
x = kru(10,20,30,40,50,60,True,[10,20])

print(x)   # 181


# kwargs

def royal(*kru, **kwargs):
    print(kwargs)   # {'name': 'Jainil', 'address': {'City': ['AHm', 'Gnr']}}
    # Type ---> Dict

    for i in kwargs:
        print(i)

    for i in kwargs.keys():
        print(i)

    for i in kwargs.values():
        print(i)

    for i in kwargs.items():
        print(i)

    for key,val in kwargs.items():
        print(key,'-----> ',val)

    print(kwargs['address'])
    print(kwargs['address']['City'])   # ['AHm', 'Gnr']
    print(kwargs['address']['City'][1])   # Gnr
    print(kwargs['address']['City'][1][1:3])   # nr


royal(10,20,30,40,name = "Jainil", address = {'City' : ['AHm', 'Gnr']})

# Dict ----> key - Value


# dict1 = {'Name' : "Krutarth", 'Roll' : 90, 'address' : {'City' : ['Ahm', 'Gnr']}}
# keys ----> Name, Roll, address
# values -----> Krutarth, 90, {'City' : ['Ahm', 'Gnr']}

# Generator, Lambda