N, standard = map(int, input().split())
num_list = list(map(int, input().split()))
print(sorted(num_list)[N - standard])