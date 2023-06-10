
_ = 1

while  _ <= 10:
    if _ == 5:
        break
    print(_)
    _ += 1

# ---------------------

_ = 1

while  _ <= 10:
    # if _ == 5:
    #     continue
    #     print("dvnsdvbsdvbsdv")
    print(_)
    _ += 1

print(_) #  11

# -----------------------


p = 25
while p<=30:
    k = 25
    while k <= 30:
        if k == p:
            break
        print(k,end=' ')
        k+=1
    print(p,end=' ')
    p+=1


#  25 25 26 25 26 27 25 26 27 28 25 26 27 28 29 25 26 27 28 29 30
print()

i = 1
j = 1
while i<=5:
    while j<=5:
        if i == j:
            j+=1
            continue
        print(j,end=' ')
        j+=1
    print(i,end=' ')
    i+=1

# 2 3 4 5 1 2 3 4 5
# j = 2
# i = 1


for i in range(1,3):
    for j in range(2,4):
        if i == j:
            break
        print(j)
    else:
        print("Else Excuted")
    print(i)

else:
    print("External Else")