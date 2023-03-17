re = []
result = 0
sub = 0
for _ in range(20):
    re.append(input())
for i in range(20):
    if re[i][-2:] == 'A+':
        result += 4.5 * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == 'A0':
        result += 4.0  * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == 'B+':
        result += 3.5 * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == 'B0':
        result += 3.0 * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == 'C+':
        result += 2.5 * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == 'C0':
        result += 2.0 * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == 'D+':
        result += 1.5 * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == 'D0':
        result += 1.0 * float(re[i][-6:-4])
        sub += float(re[i][-6:-4])
    elif re[i][-2:] == ' F':
        sub += float(re[i][-6:-4])
if sub == 0:
    print('{:.6f}'.format(0))
else:
    print('{:.6f}'.format(result / sub))
'''
A+	4.5
A0	4.0
B+	3.5
B0	3.0
C+	2.5
C0	2.0
D+	1.5
D0	1.0
F	0.0
'''
