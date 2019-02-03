# 演習：ラムダ式とdocstring

def sub(a, b):
    """Subtract b from a."""
    return a - b


f = lambda a, b: a - b

print(sub.__doc__) # Subtract b from a.
print(f(3, 1))  # 2
