# 練習：任意の個数のキーワード引数

# 仮引数に**をつけると、任意の個数のキーワード引数を受け取れる
def func(*args, **kwargs):
    print(args, kwargs)

# abc=1, xyz='xyz'は、キーワード引数
func(1, 2, 3, abc=1, xyz='xyz')

# (1, 2, 3) {'abc': 1, 'xyz': 'xyz'}
# (1, 2, 3)はタプル、 {'abc': 1, 'xyz': 'xyz'}は辞書
