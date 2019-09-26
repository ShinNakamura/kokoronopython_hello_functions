# -*- coding:utf-8 -*-
from HELLO_FUNCTIONS import _get_hello_world_str

def test_get_hello_world_str():
    '''
    print_hello_world 関数は副作用しかないのでテストが難しい
    なので、_get_hello_world_str 関数のほうをテストする
    '''
    assert _get_hello_world_str() == "hello world"
    
def main():
    test_get_hello_world_str()

if __name__ == '__main__':
    main()
