x, y, w, h = map(int, input().split())
min_val_list = []
min_val_list.append(x)
min_val_list.append(y)
min_val_list.append(abs(x-w))
min_val_list.append(abs(y-h))
min_val_list.append(((x)**2+(y)**2)**0.5)
min_val_list.append(((abs(w-x))**2+(abs(h-y))**2)**0.5)

print(min(min_val_list))
