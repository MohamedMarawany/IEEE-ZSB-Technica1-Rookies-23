Result =[]
scorelist = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Result += [[name,score]]
        scorelist += [score] 
    b = sorted(list(set(scorelist)))[1]
    
    for a, c in sorted(Result):
        if c == b :
            print(a)

            
# Another Soultion
'''
N = int(input())

s_info = []
s_grades = []

for i in range(N):
    name = input()
    grade = float(input())
    s_info += [[name, grade]]
    s_grades += [grade]

#print(s_info)
#print(s_grades)

A = sorted(list(set(s_grades)))[1]
B = sorted(s_info)

for C, D in B:
    if D == A:
        print(C)
'''
