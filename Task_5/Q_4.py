def primeFactors(n):

	A = 2
	while(n > 1):
		
		if(n % A == 0):
			print(A, end=" ")
			n = n / A
		else:
			A = A + 1

n = int(input())
primeFactors(n)
