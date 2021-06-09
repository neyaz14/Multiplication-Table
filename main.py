n = int(input('Give us a number :'))
m = int(input('Up to how many digits you want this multiplication table :'))
for m in range(1, m + 1):
    mn = n * m
    print(n, 'X', m, "=", mn)



