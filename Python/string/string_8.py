S = input()

if 'c=' in S:
    S = S.replace('c=', '|')
if 'c-' in S:
    S = S.replace('c-', '|')
if 'dz=' in S:
    S = S.replace('dz=', '|')
if 'd-' in S:
    S = S.replace('d-', '|')
if 'lj' in S:
    S = S.replace('lj', '|')
if 'nj' in S:
    S = S.replace('nj', '|')
if 's=' in S:
    S = S.replace('s=', '|')
if 'z=' in S:
    S = S.replace('z=', '|')
print(len(S))
