bloods = ['A', 'B', 'O', 'AB', 'A', 'B', 'A']

dc = dict.fromkeys(['A', 'B', 'O', 'AB'], 0)

for blood in bloods:
    dc[blood] += 1

for blood, num in dc.items():
    # f-stringsという書き方で、文字列中で変数を参照できます。また、{blood:2}は、変数bloodを2桁で出力することを指定しています。
    print(f'{blood:2}: {num}')
