import math

if __name__=="__main__":
    n = int(input().strip())
    tree = ["."]* int(math.pow(2,n))
    print(tree)
    for i in range(n):
        info = input().strip().split(' ')
        if tree[0] == ".":
            tree[0], tree[1], tree[2] = info[0], info[1], info[2]
            continue


        parent = info[0]
        p_index = tree.index(str(parent))
        tree[2*p_index + 1] = info[1]
        tree[2*p_index + 2] = info[2]
    print(tree)
    tree = ''.join(tree)


'''
6
A B C
B D E
D . .
C F .
E . .
F . .


'''