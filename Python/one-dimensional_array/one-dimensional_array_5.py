num_li = []
for i in range(10):
    num_li.append(int(input()) % 42)
num_li = set(num_li)
print(len(num_li))