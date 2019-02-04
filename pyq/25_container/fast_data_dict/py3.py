# イテラブルを返すメソッド

d = {'art': 1, 'box': 2, 'cup': 3}

# keys() : キーを要素とするイテラブルを返します。
print('keys:')
for k in d.keys():
    print(k)
print()

# values() : 値を要素とするイテラブルを返します。
print('values:')
for v in d.values():
    print(v)
print()

# itms() : キーと値のタプルを要素とするイテラブルを返します。
print('items:')
for k, v in d.items():
    print(k, v)
