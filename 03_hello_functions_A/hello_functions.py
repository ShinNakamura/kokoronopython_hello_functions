# -*- coding:utf-8 -*-
# ----------------------------------- #
# 課題全体に共通することをまず書きます。
# ・コードをスクリプトファイルに書いて保存してくださ
# ・課題ひとつに対して1つの関数を定義してください
# ・関数の名前は指定されない限りはご自身で考えみてください
# ・「○○を返すと」言われたらreturn を使いましょう

# では、以下の課題に取り組んでみてください!

# Q1.文字列 "hello" を返す関数を定義してください
def get_hello_str():
    return "hello"

# Q2.文字列 " world" を返す関数を定義してください
def get_world_str():
    return " world"

# Q3.文字列 "hello world" を返す関数を定義してください
# 関数内のコードにてQ1とQ2で定義した関数を使用してください
def get_hello_world_str():
    return get_hello_str() + get_world_str()

# Q4.文字列 "hello world" を印字する関数を定義してください
# 関数内のコードにてQ3で定義した関数を使用してください
def print_hello_world():
    print(get_hello_world_str())

# Q5.main という名前の関数を定義し、その中からQ4で作成した関数を呼んでください
def main():
    print_hello_world()

# このスクリプトがPythonから直接実行されたときだけ main 関数を Call する
if __name__ == '__main__':
    main()
# ----------------------------------- #
