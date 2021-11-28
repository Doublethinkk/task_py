num = int(input("number = "))

a = num % 10
b = num // 10
cnt = 0
while b > 0:
    a2 = b % 10
    if a == a2:
        cnt += 1
    b = b // 10
if cnt > 0:
    print("yes")
else:
    print("no")

