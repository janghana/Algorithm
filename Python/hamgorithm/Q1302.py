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
