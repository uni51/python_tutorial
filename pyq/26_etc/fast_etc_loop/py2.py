# 色々な条件の書き方

# not条件
result1 = 'is' not in 'this'
print("'is' not in 'this':", result1) # False

# 条件1 and 条件2
# 条件1が偽のとき条件1そのものになり、そうでないとき条件2そのものになります。True/Falseを返すとは限りません。
result2 = 'OK' and None
print("'OK' and None:", result2) # None

# 条件1 or 条件2
# 条件1が真のとき条件1そのものになり、そうでないとき条件2そのものになります。True/Falseを返すとは限りません。
result3 = 'OK' or None
print("'OK' or None:", result3) # OK

# 式1 is 式2
# 式1と式2が同一のオブジェクトかどうかを返します。
result4 = 'OK' is 'OK'
print("'OK' is 'OK':", result4) # True

# 式1 if 条件 else 式2
# 条件が真のとき式1になり、そうでないとき式2になります。条件式あるいは三項演算子とよばれます。
result5 = 'OK' if 'OK' else 'NG'
print("'OK' if 'OK' else 'NG':", result5) # OK

x = 1
result6 = 0 <= x <= 1
print("0 <= x <= 1:", result6) # True
