# 練習：変数のアンパック

# *argsで受けたものを*argsとして使うと、「任意個数の引数を、任意個数の引数のまま」扱えるようになります。
def func(*args):
    print(*args) # 実引数にアスタリスクをつけると、中味を展開してくれる。これをアンパックという。

func('hello', 'world') # hello world
