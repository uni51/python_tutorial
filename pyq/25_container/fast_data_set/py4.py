# 演習：日付の集合計算

a = {'1/1', '1/2', '1/4'}
b = {'1/2', '1/4', '1/7', '1/8'}
c = {'1/3', '1/4', '1/7', '1/8'}

# 3人とも出席できる日付
result1 = set.intersection(a, b, c) # result1 = a & b & c
print('3人とも出席できる日付:', result1)

# AさんとBさんが出席できて、Cさんが出席できない日付
result2 = a.intersection(b).difference(c) # result2 = a & b - c
print('AさんとBさんが出席できて、Cさんが出席できない日付:', result2)
