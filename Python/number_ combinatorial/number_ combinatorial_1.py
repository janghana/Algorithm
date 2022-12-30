while True:
    a, b = map(int ,input().split())
    TF_factor = True
    TF_multiple = True
    if a == 0 and b == 0:
        break
    if b % a != 0 or a >=  b:
        TF_factor = False
    if a % b != 0 or b >= a or a // b == 0:
        TF_multiple = False
    if TF_factor and not TF_multiple:
        print("factor")
    elif not TF_factor and TF_multiple:
        print("multiple")
    elif not TF_factor and not TF_multiple:
        print("neither")
