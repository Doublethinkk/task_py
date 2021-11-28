str = input("Enter string : ")
char = input("Enter char : ")
start = -1
cnt = 0
while True:
    start = str.find(char, start + 1)
    if start == -1:
        break
    cnt += 1
if cnt > 0:
   print(char, cnt)

