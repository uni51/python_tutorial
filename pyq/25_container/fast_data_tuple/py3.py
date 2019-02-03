# 練習：allとany
# all（イテラブル）：イテラブルの全ての要素が真ならば、Trueを返します。
# any（イテラブル）：イテラブルの何れかの要素が真ならば、Trueを返します。

items1 = (True, False, True)
print("items1:", items1)
items2 = (True, True, True)
print("items2:", items2)

# 全ての要素が真かどうか
result_all1 = all(items1)
print("all(items1):", result_all1) # all(items1): False

# 全ての要素が真かどうか
result_all2 = all(items2)
print("all(items2):", result_all2) # all(items2): True

# 何れかの要素が真かどうか
result_any1 = any(items1)
print("any(items1):", result_any1) # any(items1): True
