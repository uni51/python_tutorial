# 集合のメソッド（追加等）

items = {'art'}
print("items:", items) # items: {'art'}

# 1要素を削除
result = items.pop() # popでは、位置を指定して削除ができません
print("items.pop():", result) # items.pop(): art
print("items:", items) # items: set()

# リストを追加  複数の要素の追加は、extendではなくupdateです。
items.update(['egg', 'fog'])
print("items.update(['egg', 'fog'])") #items.update(['egg', 'fog'])
print("items:", items) # items: {'fog', 'egg'}

# 全削除
items.clear()
print("items.clear()") # items.clear()
print("items:", items) # items: set()

# 追加  要素の追加は、appendではなくaddです。
items.add('doll')
print("items.add('doll')") # items.add('doll')
print("items:", items) # items: {'doll'}

# 削除
items.remove('doll')
print("items.remove('doll')") # items.remove('doll')
print("items:", items) # items: set()
