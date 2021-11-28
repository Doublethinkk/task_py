num = int(input("enter num "))
for i in range(1, num):
    d = 10
    while i >= d:
        d = d*10
    if i*i %d == i:
        print("number", i, "^2", i*i)

