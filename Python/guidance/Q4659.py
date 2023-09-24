'''
Method : Typing Studying

title : Good PW

condition

1. PW MUST contain at least one of following vowels : 'a, e, i, o, u'.

2. No vowel or consonant should appear in a sequence of 3 consecutive letters.

3. Alphabets should not appear in continuous sequences, with the exceptions of 'ee', and 'oo'.

'''


def vowel_or_consonant(alpha):
    if alpha in 'a' or alpha in 'i' or alpha in 'e' or alpha in 'o' or alpha in 'u':
        return 1
    else:
        return -1


while True:
    S = input()
    if S == 'end':
        break
    check = True
    ckp_vowel = 0
    ckp_consonant = 0
    for index, alpha in enumerate(S):
        if alpha in 'a' or alpha in 'i' or alpha in 'e' or alpha in 'o' or alpha in 'u':
            ckp_vowel += 1

        if index + 2 < len(S):
            ckp_consonant = vowel_or_consonant(S[index]) + vowel_or_consonant(S[index + 1]) + vowel_or_consonant(S[index + 2])
            if ckp_consonant == 3 or ckp_consonant == -3:
                check = False
                break
        if index + 1 != len(S):
            if S[index] == S[index + 1]:
                if S[index] == 'e' or S[index] == 'o':
                    continue
                else:
                    check = False
                    break
    if ckp_vowel == 0:
        check = False
    result = 'acceptable.' if check is True else 'not acceptable.'
    print('<{0}> is {1}'.format(S, result))
