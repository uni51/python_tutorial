# 辞書とは
#
# キーと値のペアの集合です。キーに対応する値を取得できます。
# リテラルは、{'art': 1, 'box': 2}のように{キー1: 値1, キー2: 値2, ...}のように記述します。
# キーは、イミュータブル（変更不可）なものしか指定できません。値は何でも指定できます。
# 同じキーは1つだけ持てます。複数追加すると上書きします。
# 順序がありませんが、イテラブルとして取得するときの順番は不変です。
# マップや連想配列と呼ぶこともあります。


d = {'art': 1, 'box': 2}

# 追加
d['cup'] = 3

# 参照
print("d['art']:", d['art']) # d['art']: 1
print("d['cup']:", d['cup']) # d['cup']: 3

# 削除
del d['art']
print("d:", d) # d: {'box': 2, 'cup': 3}
