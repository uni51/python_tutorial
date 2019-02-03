# リストのメソッド - その2

items = [1]
print("items:", items)

# 末尾にリストを追加
items.extend([2, 5, 3, 4])
print("items.extend([2, 5, 3, 4])")
print("items:", items)

# 要素を削除
items.remove(3)
print("items.remove(3)")
print("items:", items)

# 末尾を削除して取得
result = items.pop()
print("items.pop():", result)
print("items:", items)

# 5の位置を探索
result = items.index(5)
print("items.index(5):", result)

# コピー
items2 = items.copy()
print("items2 = items.copy()")

# 逆順でソート
items.sort(reverse=True)
print("items.sort(reverse=True)")
print("items:", items)
print("items2:", items2)
