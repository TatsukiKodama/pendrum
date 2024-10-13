def is_same_length(A: list, B: list) -> bool:
    return True if len(A) == len(B) else False

def combine(A: list, B: list) -> list:
    '''
    2つのリストを合わせる関数

    例）
    A = [1, 2, 3]
    B = ['a', 'b', 'c']

    >>> combine_lists(A, B)
    >>> [1, 'a', 2, 'b', 3, 'c']
    '''
    if (not is_same_length):
        print('リストの長さが一致しません。')
        return []
    
    return [item for pair in zip(A, B) for item in pair]