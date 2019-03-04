# シーケンス同士の比較

result1 = [0, 1, 2] < [0, 1, 3] # True
print("[0, 1, 2] < [0, 1, 3]:", result1)

result2 = [0, [0, 1, 2]] < [0.0, [0, 1, 3]] #True
print("[0, [0, 1, 2]] < [0.0, [0, 1, 3]]:", result2)

result3 = 'abc' < 'abd' #True
print("'abc' < 'abd':", result3)
