## 23-3.リストを使おう

lst = ['A', 'B', 'C', 'D', 'E']

# lstの先頭の要素を出力
print('lstの先頭:', lst[0])  # A

# lstの最後の要素を出力
print('lstの最後:', lst[-1])  # E

# lstの2番目から3番目を出力
print('lstの2番目から3番目:', lst[1:3]) # ['B', 'C']

# lstの先頭から最後までを1つ飛ばしで出力
print('lstの先頭から最後までを1つ飛ばしで:', lst[::2]) # ['A', 'C', 'E']

# lstを逆順に出力
print('lstの逆順:', lst[::-1]) #  ['E', 'D', 'C', 'B', 'A']

# lstと['F', 'G']を連結したリストを出力
print("lstに['F', 'G']を連結:", lst + ['F', 'G']) # : ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# lstの出力が、['A', 'B', 'C', 'D', 'E', 'F']になるようにlstに'F'を追加
lst.append('F')
print('lst:', lst) #  ['A', 'B', 'C', 'D', 'E', 'F']

# lstの出力が、['A', 'C', 'E', 'F']になるように、代入文でlstを修正
lst[1:4] = ['C']
print('lst:', lst) #  ['A', 'C', 'E', 'F']
