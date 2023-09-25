'''
Method : Typing Studying

title : Good PW

condition :

mini game : Y, F, O

solutions :

using dict to solve this problem.

'''

N, mini_game_type = input().split()

members_count = len(set([input() for i in range(int(N))]))

if mini_game_type == "Y":
    print(members_count)
elif mini_game_type == "F":
    print(members_count // 2)
else:
    print(members_count // 3)

