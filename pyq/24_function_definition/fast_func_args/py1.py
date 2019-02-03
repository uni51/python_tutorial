# 練習：任意個数の位置引数の定義

# 仮引数に*argsのように書くと、任意の個数の位置引数をタプルで受け取れます
# def func(*args)のようなargsを可変長位置引数といいます。
def func(*args):
    print(args)  # ('hello', 'world')
    for arg in args:
        print(arg, end=' ') # hello world
    print() # 改行を出力


func('hello', 'world')
