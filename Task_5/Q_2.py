A = []
B = list(input())

for i in B:
    
    if i in ['(', '{', '[']:
        A.append(i)
    elif i == ')' and len(A) != 0 and A[-1] == '(':
        A.pop()
    elif i == '}' and len(A) != 0 and A[-1] == '{':
        A.pop()
    elif i == ']' and len(A) != 0 and A[-1] == '[':
        A.pop()
    else:
        A.append(i)

if len(A) == 0:
    print("True")
else: print("False") 
