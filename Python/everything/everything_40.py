from collections import Counter
V = int(input())
S = Counter(input())
if S['A'] > S['B']:
    print('A')
elif S['A'] < S['B']:
    print('B')
else:
    print("Tie")
