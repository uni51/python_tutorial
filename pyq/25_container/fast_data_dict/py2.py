# 辞書の主なメソッド

print("d = dict.fromkeys(['box', 'cup'], 3)")
# 第1引数のリストをキーとして辞書を作成します。値は全て第2引数（なければNone）になります。
d = dict.fromkeys(['box', 'cup'], 3)
print("d:", d) # d: {'box': 3, 'cup': 3}

# 参照
print("d.get('art', -1):", d.get('art', -1)) # 辞書dにキー'art'は存在しないので、-1が返ります。
print("d:", d) # d: {'box': 3, 'cup': 3}
# d.setdefault('art', 1) ： こちらは辞書に、キー'art'の値として1を追加した上で、1を返します
print("d.setdefault('art', 1):", d.setdefault('art', 1))
print("d:", d) # d: {'box': 3, 'cup': 3, 'art': 1}

# 更新
d.update({'box': 2})
print("d.update({'box': 2})")
print("d:", d) # d: {'box': 2, 'cup': 3, 'art': 1}

# 削除
print("d.pop('art'):", d.pop('art')) # d.pop('art'): 1
print("d.pop('cup'):", d.pop('cup')) # d.pop('cup'): 3
print("d.popitem():", d.popitem()) # d.popitem(): ('box', 2)

# 全削除
d.clear()
print("d.clear()")
print("d:", d) # d: {}
