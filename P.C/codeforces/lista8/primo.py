n = int(input())

while True:
    n += 1
    primo = True
    for x in range(2,n):
        if n%x==0:
            primo = False

    if primo:
        break

print(n)