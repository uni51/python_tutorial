s = 'pine' 'apple'
print(s)
#pineapple

# この記述でも改行は無視される
s = """\
pine\
apple"""

# 丸括弧でくくると、行をまたいで記述できます（改行されない）
s = ('pine'
	 'apple')

print(s)

print('Yes' * 3) # YesYesYes

print('is' in 'this') # True
