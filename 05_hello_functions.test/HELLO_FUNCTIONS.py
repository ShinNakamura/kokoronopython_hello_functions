# -*- coding:utf-8 -*-
# このスクリプトは自作モジュールとして import されることを意図しています。
# 公開関数は print_hello_world です。
# print_hello_world が使用するその他の関数は非公開関数なので、先頭に _ を補います。

def _get_hello_str():
    '''
    文字列 "hello" を返す関数
    '''
    return "hello"

def _get_world_str():
    '''
    文字列 " world" を返す関数
    '''
    return " world"

def _get_hello_world_str():
    '''
    文字列 "hello world" を返す関数
    '''
    return _get_hello_str() + _get_world_str()

def print_hello_world():
    '''
    文字列 "hello world" を印字する関数
    '''
    print(_get_hello_world_str())

def main():
    print_hello_world()

# このスクリプトがPythonから直接実行されたときだけ main 関数を Call する
if __name__ == '__main__':
    main()
# ----------------------------------- #
