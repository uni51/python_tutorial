# 練習：スコープの話

i = 123  # グローバル変数

# グローバル変数を利用
def func1():
    print(i)

# ローカル変数を利用
def func2():
    i = 456  # ローカル変数
    print(i)

# グローバル変数を利用
def func3():
    print(i)


func1() # 123と出力
func2() # 456と出力
func3() # 123と出力
print(i) # 123と出力
