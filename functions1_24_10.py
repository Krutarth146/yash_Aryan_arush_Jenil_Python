
# # User Defined Function  ---> Code Reusability

# def play():    # Func. Defination
#     print('Hello')
#     print('Arush')
#     print('Patel')


# print("Manish Sisodhiya")


# play()   # FUnc. Calling


# print("Manish Sisodhiya")

# play()

# # Inbuilt Functions
# # print()
# # input()
# # len()
# # max()
# # sum()




# def print_series(num):
#     list1 = []
#     for k in range(1,num+1):
#         # print(k,end=' ')
#         return k
#         # list1.append(k)
#     # return list1


# print(print_series(30))    # Patel
# # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]



# Generator

def Aman(num):
    for i in range(1,num+1):
        yield i
    
# print(Aman(10))

# print(Aman(10).__next__())   # 1
# print(Aman(10).__next__())   # 1

x = Aman(10)
print(x)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x)
# print(x.__next__())

for k in Aman(10):
    print(k)


# Lambda Function (Anounomous Function)

def square(num):
    return num ** 2


sq1 = lambda num : num ** 2
print(sq1(10))

m4 = lambda x,y,z : x+y*z

print(m4("Aman", ' Ashok', 2))


sqaure = lambda num : num ** 2
cube = lambda num : num ** 3

print(square(15), cube(13))   # 225   2197

x = lambda n1,n2,num = 20 : num ** 2
# x = lambda num = 20 : num ** 2
print(x(10,90))
print(x(10,20,30))

# ---------------------------------------------

# Quadratic Function

# a * x ** 2  +  b*x   +   c 

def quadratic_fun(a,b,c):
    return lambda x : (a * x ** 2)  +  (b*x)   +   c 

# jenil = quadratic_fun(10,20,90)
# print(jenil(5))  # 440

print(quadratic_fun(10,20,30)(5))   # 380