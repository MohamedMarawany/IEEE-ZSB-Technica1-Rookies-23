def heapify(arr, N, i):

	largest = i 
	l = 2 * i + 1 
	r = 2 * i + 2 

	if l < N and arr[l] > arr[largest]:
		largest = l

	if r < N and arr[r] > arr[largest]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i]

		heapify(arr, N, largest)

arr = list(map(int, input().split()))

N = len(arr)

while N >= 0:
    heapify(arr, len(arr), N)
    N -= 1

for i in arr:
    print(i, end=" ")
