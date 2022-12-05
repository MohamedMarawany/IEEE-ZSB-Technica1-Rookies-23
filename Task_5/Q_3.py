def sum_of_squares_of_digits(n):
    return sum(int(i) ** 2 for i in str(n))

n = int(input())
A = []
while True:
    n = sum_of_squares_of_digits(n)
    if n == 1:
        break
    A.append(n)

if n == 1:
    print("True")
else:
    print("False")
