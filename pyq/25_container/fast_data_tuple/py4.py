# 演習：販売データの検索
# 要素は、(顧客ID, 販売額)を表しています。
# 顧客IDが10以下で、販売額が100円以上のデータを出力してください。

sales = ((1, 100), (2, 30), (7, 150), (11, 120), (10, 100))

for sale in sales:
    if sale[0] <= 10 and sale[1] >= 100:
        print(sale)