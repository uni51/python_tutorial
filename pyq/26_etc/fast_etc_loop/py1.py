# 色々なループ用の関数

items = ('cup', 'art', 'box')
print('items:', items) # items: ('cup', 'art', 'box')


# startからの通し番号とiterableで繰り返される値のタプルを要素とするイテレーターを返す
print('enumerate:')
print(list(enumerate(items))) # [(0, 'cup'), (1, 'art'), (2, 'box')]


# それぞれのイテラブルから要素を集めたイテレータを返します。
print('zip:')
print(list(zip(items))) #[('cup'), ('art'), ('box')]
print(list(zip(range(3), items))) #[(0, 'cup'), (1, 'art'), (2, 'box')]


# iterableを小さい順にソートしたリストを返します。
print('sorted:')
print(sorted(items)) # ['art', 'box', 'cup']


# seqを逆順にしたイテレーターを返します
print('reversed:')
print(list(reversed(items))) # ['box', 'art', 'cup']
