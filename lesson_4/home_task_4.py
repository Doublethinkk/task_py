cnt = 0
d = " "

while cnt <= 0:
    string = str(input("Enter text : "))
    for i in string:
        if i == d:
            cnt += 1

    if cnt == 0:
        print("Write two words")

print(cnt)
x = string[::-1]
print(x.title())

