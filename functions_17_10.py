
b = 10

def greet(msg1, msg2):
    # global b
    a = 20
    print(a+b)  # 30

    c = 20
    b = a+c   # 40
    return b
    # print(msg1, msg2)
    

# greet(msg2 = "Hello", msg1 = ("Ram","Ashok"))
print(greet(10,20))   # 40
print(b)  # 40