# 集合のメソッド（演算）

s1 = set('ab')
s2 = set('bc')
print("s1:", s1) # s1: {'b', 'a'}
print("s2:", s2) # s2: {'b', 'c'}

# 差集合
result1 = s1.difference(s2) # s2の要素を削除した集合を返す
print("s1.difference(s2):", result1) # s1.difference(s2): {'a'}

# 積集合（共通の集合）
result2 = s1.intersection(s2) # s2と共通の集合を返す
print("s1.intersection(s2):", result2) # s1.intersection(s2): {'b'}

# 対称差（片方にしか含まれない要素の集合）
result3 = s1.symmetric_difference(s2)
print("s1.symmetric_difference(s2):", result3) # s1.symmetric_difference(s2): {'a', 'c'}

# 和集合
result4 = s1.union(s2) # s2の要素を追加した集合を返す
print("s1.union(s2):", result4) # s1.union(s2): {'b', 'a', 'c'}
