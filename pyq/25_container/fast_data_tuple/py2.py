# 練習：アンパック
# タプルは1つのオブジェクトですが、複数の変数に同時に代入できます。
# これをアンパックといいます。

items = ('art', 'box', 'cup')
print("items:", items) # items: ('art', 'box', 'cup')

# アンパック
a, b, c = items
print("a, b, c = items")
print("(a, b, c):", (a, b, c)) # (a, b, c): ('art', 'box', 'cup')

# アンパック
a, *b = items
print("a, *b = items")
print("(a, b):", (a, b)) # (a, b): ('art', ['box', 'cup'])
