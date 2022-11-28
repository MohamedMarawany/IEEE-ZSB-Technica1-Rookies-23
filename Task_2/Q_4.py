A = list(map(int, input().split()))

B = [*set(A)]
B.sort()
print(B)
