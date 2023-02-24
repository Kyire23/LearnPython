from random import randint
n = 100
a = [[randint(1,100) for i in range(n)] for j in range(n)]
total = 0
for i in range(n):
    for j in range(n):
        total += a[i][j]
print(total)
