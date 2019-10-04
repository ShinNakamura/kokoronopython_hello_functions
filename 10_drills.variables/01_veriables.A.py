# -*- coding: utf-8 -*-
###### ANSWERS ######

# Q1. 変数aに値10を代入してください。
a = 10

# Q2. 変数bに値20を代入してください。
b = 20

# Q3. 変数arrに空の配列を代入してください。
arr = []

# Q4. 変数arrに変数aの値を追加してください。(ヒント：appendを使います。)
arr.append(a)

# Q5. 変数arrに変数bの値を追加してください。(ヒント：appendを使います。)
arr.append(b)

# Q6. 変数len_of_arrに変数arrに割り当てられている配列の長さを代入してください。
#     (ヒント：len関数を使います。)
len_of_arr = len(arr)


# 答え合わせ
# これは問題ではありません。
# 全てのQが正解ならば下記の check_answers 関数はエラーなく実行されるはずです。
def check_answers():
    assert a == 10
    assert b == 20
    assert arr == [10, 20,]
    assert len_of_arr == 2

check_answers()

