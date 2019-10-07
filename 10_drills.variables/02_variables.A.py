# -*- coding: utf-8 -*-

# Q1. 変数aに、10を3で割った余りを代入してください。
a = 10 % 3

# Q2. 変数bに、変数aが0だったら1を、それ以外だったら3を代入してください。
#     ヒント：ifを使います。
#     チャレンジ：可能であれば1行で書いてください。`
b = 1 if a == 0 else 3

# Q3. 変数arrに空の配列を代入してください。
arr = []

# Q4. 変数arrに変数bに代入されている数値の個数分だけ
#     変数aの値を追加してください。
#     ヒント：rangeとappendを使います。
for _ in range(b):
    arr.append(a)

# 答え合わせ
# これは問題ではありません。
# 全てのQが正解ならば下記の check_answers 関数はエラーなく実行されるはずです。
def check_answers():
    assert a == 1
    assert b == 3
    assert arr == [1, 1, 1,]

check_answers()

