## 23-2.文字列の主なメソッド


# 全ての文字がalphabeticかどうか
print("'abc'.isalpha():", 'abc'.isalpha()) # True

# 全ての文字がalphabeticかどうか
print("'ab3'.isalpha():", 'ab3'.isalpha()) # False

# 全ての文字が数字かどうか
print("'12'.isdigit():", '12'.isdigit()) # True

# 全ての文字が小文字かどうか
print("'abc'.islower():", 'abc'.islower()) # True

# 全ての文字が大文字かどうか
print("'ABC'.isupper():", 'ABC'.isupper()) # True

# 全ての文字が大文字かどうか
print("'Abc'.isupper():", 'Abc'.isupper()) # False

# 全ての文字を小文字に変換する
print("'Abc'.lower():", 'Abc'.lower()) # abc

# 全ての文字を大文字に変換する
print("'Abc'.upper():", 'Abc'.upper()) # ABC
