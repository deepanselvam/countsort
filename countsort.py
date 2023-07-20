import sys

n = int(input())
ar = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(i + 1, n):
        if ar[i] > ar[j]:
            temp = ar[i]
            ar[i] = ar[j]
            ar[j] = temp

print()
for i in range(n):
    print(ar[i], end=" ")
