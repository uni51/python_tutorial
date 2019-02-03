# 演習：ログの整理

from pprint import pprint

log = """\
1/1 晴れ
1/2 晴れ
1/3 曇り
1/4 雨
1/5 雨
1/6 曇り
1/7 晴れ
"""

loglist = [s.split() for s in log.splitlines()]
print('loglist:')
pprint(loglist) # pprintは見やすいように整形して出力する関数

# 条件を満たすリストは、[変数 for 変数 in リスト if 条件]
# リストに要素が含まれるかどうかは、要素 in リストで判断する
loglist2 = [it for it in loglist if '晴れ' in it]
# loglist2 = [it.split() for it in log.splitlines() if '晴れ' in it]
print('loglist2:', loglist2)
