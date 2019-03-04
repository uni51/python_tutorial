# 色々なインポート

# import モジュール as 別名
import module2 as mod

result1 = mod.add(5, 3)
result2 = mod.sub(5, 3)
print(result1, result2)


# from モジュール import 名前, ...
from module2 import add, sub

result3 = add(5, 3)
result4 = sub(5, 3)
print(result3, result4)


# from モジュール import 名前 as 別名
from module2 import add as mod_add

result5 = mod_add(5, 3)
print(result5)
