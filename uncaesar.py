#!/usr/bin/env python3
from argparse import ArgumentParser

# ["A", "B", ... "Z"]
c=[chr(i) for i in range(ord('A'), ord('Z')+1)]

# 引数を取得
parser = ArgumentParser()
parser.add_argument('file', help='ファイル')
parser.add_argument('num',  type=int, help='シフト数')

args = parser.parse_args()

with open(args.file, mode = 'r') as f:
    data = f.read()
    print(f"===orig===\n{data}")
    work = list(data) # リストに変換
    def s(x, n):
        if x in c:
            return c[ (c.index(x)+n) % 26 ]
        else:
            return x
    result = list(map(lambda x: s(x, args.num), work))
    print(f"===result===\n{''.join(result)}")