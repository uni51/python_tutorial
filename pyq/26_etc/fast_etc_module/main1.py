# モジュールとは

import module1

print('__name__:', __name__)
result1 = module1.add(1, 2)
print('module1.add(1, 2):', result1)

# 変数に代入して実行
add = module1.add
print('add = module1.add')
result2 = add(1, 2)
print('add(1, 2):', result2)
