# 演習：正負を確認する関数を作ろう

def func(x=None): # 「実引数なし」に対応するためには、デフォルト値を指定します。
    if x is None:
        print('引数を指定してください')
    elif x < 0:
        print('負の値です')
    elif x == 0:
        print('0です')
    else:
        print('正の値です')


func()  # 引数を指定してください
func(0)  # 0です
func(-1)  # 負の値です
func(99)  # 正の値です
