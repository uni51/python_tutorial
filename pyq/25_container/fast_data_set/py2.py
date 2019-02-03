# 集合のメソッド（判定等）

items = {3, 4}
print("items:", items) # items: {3, 4}

# 共通する要素がないか（otherと共通する要素がなければTrue）
result1 = items.isdisjoint({1, 2})
print("items.isdisjoint({1, 2}):", result1) # 共通する要素がないので、True

# 部分集合か（otherの部分集合であればTrue）
result2 = items.issubset({1, 3, 4})
print("items.issubset({1, 3, 4}):", result2) # True

# 引数の部分集合か（otherが部分集合であればTrue）
result3 = items.issuperset({4})
print("items.issuperset({4}):", result3) # True
