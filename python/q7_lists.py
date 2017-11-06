# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def main():
    print("\nTesting match_ends():")
    print("=====================")
    test_match_ends()

    print("\nTesting front_x():")
    print("==================")
    test_front_x()

    print("\nTesting sort_last():")
    print("====================")
    test_sort_last()

    print("\nTesting remove_adjacent():")
    print("==========================")
    test_remove_adjacent()

    print("\nTesting linear_merge():")
    print("=======================")
    test_linear_merge()

def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    
    cnt = 0
    for w in words:
        if len(w) > 1:
            if w[0] == w[-1]:
                cnt += 1

    return cnt


def test_match_ends():
    inputs = [['aba', 'xyz', 'aa', 'x', 'bbb'], 
              ['', 'x', 'xy', 'xyx', 'xx'],
              ['aaa', 'be', 'abc', 'hello']]
    for l in inputs:
        print("match_ends({0}) => {1}".format(str(l), match_ends(l)))

def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """

    x_list = []
    gen_list = []
    for w in words:
        if w[0] is 'x':
            x_list.append(w)
        else:
            gen_list.append(w)

    return sorted(x_list) + sorted(gen_list)
    

def test_front_x():
    inputs = [['bbb', 'ccc', 'axx', 'xzz', 'xaa'],
              ['ccc', 'bbb', 'aaa', 'xcc', 'xaa'],
              ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']]
    for l in inputs:
        print("front_x({0}) => {1}".format(str(l), front_x(l)))


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    
    from operator import itemgetter
    
    return sorted(tuples, key=itemgetter(-1))
                

def test_sort_last():
    inputs = [[(1, 3), (3, 2), (2, 1)],
              [(2, 3), (1, 2), (3, 1)], 
              [(1, 7), (1, 3), (3, 4, 5), (2, 2)]]
    for l in inputs:
        print("sort_last({0}) => {1}".format(str(l), sort_last(l)))


def remove_adjacent(nums):
    """
    Given a list of numbers, return a list where all adjacent equal
    elements have been reduced to a single element, so [1, 2, 2, 3]
    returns [1, 2, 3]. You may create a new list or modify the passed
    in list.

    >>> remove_adjacent([1, 2, 2, 3])
    [1, 2, 3]
    >>> remove_adjacent([2, 2, 3, 3, 3])
    [2, 3]
    >>> remove_adjacent([3, 2, 3, 3, 3])
    [3, 2, 3]
    >>> remove_adjacent([])
    []
    """
    
    idx = 1
    n = len(nums)
    while idx < n:
        if nums[idx] == nums[idx-1]:
            del nums[idx]
            n -= 1
        else:
            idx += 1

    return nums


def test_remove_adjacent():
    inputs = [[1, 2, 2, 3], 
              [2, 2, 3, 3, 3], 
              [3, 2, 3, 3, 3]]
    for l in inputs:
        print("remove_adjacent({0}) => {1}".format(str(l), remove_adjacent(l)))


def linear_merge(list1, list2):
    """
    Given two lists sorted in increasing order, create and return a
    merged list of all the elements inl sorted order. You may modify
    the passed in lists. Ideally, the solution should work in "linear"
    time, making a single pass of both lists.

    >>> linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])
    ['aa', 'bb', 'cc', 'xx', 'zz']
    >>> linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])
    ['aa', 'aa', 'aa', 'bb', 'bb']
    """    
 
    return sorted(list1 + list2)


def test_linear_merge():
    inputs = [(['aa', 'xx', 'zz'], ['bb', 'cc']),
              (['aa', 'xx'], ['bb', 'cc', 'zz']),
              (['aa', 'aa'], ['aa', 'bb', 'bb'])]
    for l in inputs:
        print("linear_merge({0}, {1}) => {2}".format(str(l[0]), str(l[1]), linear_merge(l[0], l[1])))


if __name__ == "__main__":
    main()
