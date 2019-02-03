# 練習：タプルを使おう

items = ('art', 'box', 'cup')

print("items:")  # 各要素
for item in items:
    print('  -', item)

print("items:", items) # items: ('art', 'box', 'cup')

result1 = items[2]
print("items[2]:", result1)  # items[2]: cup

# 個数計測
result2 = items.count('box')
print("items.count('box'):", result2) # items.count('box'): 1

# 位置探索
result3 = items.index('cup')
print("items.index('cup'):", result3) # items.index('cup'): 2

# タプルの入れ子
items2 = (items, items)
print("items2:", items2) # items2: (('art', 'box', 'cup'), ('art', 'box', 'cup'))
