from collections import Counter
book_str = [input() for _ in range(int(input()))]

# Iterate through counted values through Counter library.
most_sold_book_list = []
most_sold_count = Counter(book_str).most_common(n=1)[0][1]
for book_name in Counter(book_str):
    if most_sold_count == Counter(book_str)[book_name]:
        most_sold_book_list.append(book_name)
        most_sold_count = Counter(book_str)[book_name]
print(sorted(most_sold_book_list)[0])

s = list(input())
a_cnt = s.count('a')
answer = 999999999999999
left = 0

while left < len(s):
  right = left + a_cnt
  if right > len(s):
    temp = s[left:len(s)] + s[:right-len(s)]
  else:
    temp = s[left:right]
  answer = min(answer, temp.count('b'))
  left += 1

print(answer)