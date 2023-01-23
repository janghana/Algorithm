h, m, s = map(int, input().split())
plus = int(input())

s += plus % 60
plus //= 60
if s >= 60:
    tmp = s // 60
    s -= 60 * tmp
    m += tmp

m += plus
plus //= 60
if m >= 60:
    tmp = m // 60
    m -= 60 * tmp
    h += tmp
if h >= 24:
    tmp = h // 24
    h -= 24 * tmp

print(h, m, s)
