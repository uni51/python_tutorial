## 23-2.文字列の主なメソッド

# 「AB」の出現回数を求める
print("'ABCAB'.count('AB'):", 'ABCAB'.count('AB')) # 2

# 「X」の出現位置を求める（見つからない場合は、-1を返す）
print("'ABC'.find('X'):", 'ABC'.find('X')) # -1

# 「B」の出現位置を求める（見つからない場合は、-1を返す）
print("'ABC'.index('B'):", 'ABC'.index('B')) # 1

# 対象文字列の末尾が文字列「BC」で終わっているか
print("'ABC'.endswith('BC'):", 'ABC'.endswith('BC')) # True

# 対象文字列の先頭が文字列「AB」で始まっているか
print("'ABC'.startswith('AB'):", 'ABC'.startswith('AB')) # True

# 対象文字列の先頭が文字列「BA」で始まっているか
print("'ABC'.startswith('BA'):", 'ABC'.startswith('BA')) # False

# 対象文字列の先頭が文字列「AB」か「BA」のいずれかで始まっているか
print("'ABC'.startswith(('AB', 'BA')):", 'ABC'.startswith(('AB', 'BA'))) # True
