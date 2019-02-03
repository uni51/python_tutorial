# 演習：print関数のラッパーを作ろう

def print_with_prompt(*args, **kwargs):
    print('> ', end='') # '> 'を改行せずに出力するには、print('> ', end='')とします
    print(*args, **kwargs)

# sep=','をつけてprintすると、各実引数の間に,を出力します
print_with_prompt('hello', 'world', sep=',')  # > hello,world
