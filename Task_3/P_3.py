N = int(input())

bot_vol = []
bot_cap =[]

for i in range(N):
    '''A = int(input().split())
    bot_cap.append(A)
    B = int(input().split())
    bot_vol.append(B)'''
    A, B = map(int, input().split())
    bot_vol.append(A)
    bot_cap.append(B)

sum_vol = sum(bot_vol)
C = sorted(bot_cap)
sum_cap = sum(C[-2:])

if sum_cap > sum_vol:
    print("YES")
else: print("NO")
