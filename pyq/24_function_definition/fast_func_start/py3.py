# 練習：引数について

def func(arg1, arg2=2, args3=3):
    print(arg1, arg2, args3)

func(10, 20, 30)  # 10 20 30
func(10, 20)  # 10 20 3
func(arg1=10)  # 10 2 3
func(10, args3=30)  # 10 2 30
