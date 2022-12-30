N = int(input())
six_number = 666
count = 0
result = 0
while True:
    if '666' in str(six_number):
        count += 1
    if count == N:
        result = six_number
        break
    six_number += 1
print(result)
