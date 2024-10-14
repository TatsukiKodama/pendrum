def is_list(*args: list):
    '''
    可変長で入力される引数がリストかどうか？
    '''
    for list_ in args:
        if not isinstance(list_, list):
            return False
    print("すべての入力はlistオブジェクトです。")
            

def is_same_length(list_A: list, list_B: list) -> bool:
    '''
    2つのリストが同じ関数かどうかを判定する関数
    '''
    if len(list_A) == len(list_B):
        print(f'{list_A}と{list_B}は同じ長さです。')
        True
    else:
        print(f'{list_A}と{list_B}は異なる長さです。')
        False

def check_list_length(length: int, list_: list):
    '''
    単一のリストの長さが想定の長さかどうか判定する関数
    '''
    if len(list_) == length:
        return True
    else:
        return False
    
def check_lists_length(length: int, *args: list):
    '''
    可変長で入力されるリスト群が、それぞれlengthと同じ長さかどうかを
    判定する関数
    '''
    for list_ in args:
        result = check_list_length(length, list_)
        if (result == False):
            return False
    print(f'すべてのリストの長さは{length}です。')
    return True

def combine(A: list, B: list) -> list:
    '''
    2つのリストを合わせる関数

    例）
    A = [1, 2, 3]
    B = ['a', 'b', 'c']

    >>> combine_lists(A, B)
    >>> [1, 'a', 2, 'b', 3, 'c']
    '''
    result = is_same_length(A, B)
    if (result == False):
        print('リストの長さが一致しません。')
        return []
    
    return [item for pair in zip(A, B) for item in pair]