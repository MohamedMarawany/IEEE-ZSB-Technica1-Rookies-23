a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
    ]

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

print(list(rotated(a)))
