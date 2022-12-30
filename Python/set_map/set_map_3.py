N, M = map(int ,input().split())
pokemon_encyclopedia_id = {}
pokemon_encyclopedia_name = {}
for i in range(N):
    pokemon_encyclopedia_id[i] = input()
    pokemon_encyclopedia_name[pokemon_encyclopedia_id[i]] = i
for i in range(M):
    problem = input()
    if problem.isdigit():
        print(pokemon_encyclopedia_id[int(problem)-1])
    else:
        print(pokemon_encyclopedia_name[problem]+1)
