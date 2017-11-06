# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

def main():
    print("\nTesting donuts():")
    print("=================")
    test_donuts()

    print("\nTesting both_ends():")
    print("====================")
    test_both_ends()

    print("\nTesting fix_start():")
    print("====================")
    test_fix_start()

    print("\nTesting mix_up():")
    print("===================")
    test_mix_up()

    print("\nTesting verbing():")
    print("==================")
    test_verbing()

    print("\nTesting not_bad:")
    print("================")
    test_not_bad()

    print("\nTesting front_back():")
    print("=====================")
    test_front_back()

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """

    if count > 9:
        count = 'many'

    return "Number of donuts: {}".format(count)


def test_donuts():
    counts = [4, 9, 10, 99]
    for count in counts:
        print("donuts({0}) => {1}".format(count, donuts(count)))


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    
    if len(s) >= 2:
        return s[:2] + s[-2:]
    else:
        return ''


def test_both_ends():
    strings = ['spring', 'Hello', '', 'xyz']
    for s in strings:
        print("both_ends({0}) => {1}".format(s, both_ends(s)))


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    
    s_new = s[0]
    for char in s[1:]:
        if char is s[0]:
            s_new += '*' 
        else:
            s_new += char

    return s_new


def test_fix_start():
    strings = ['babble', 'aardvark', 'google', 'donut']
    for s in strings:
        print("fix_start({0}) => {1}".format(s, fix_start(s)))


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    
    new_a = b[:2] + a[2:]
    new_b = a[:2] + b[2:]

    return "{0} {1}".format(new_a, new_b)


def test_mix_up():
    strings = [('mix', 'pod'), ('dog', 'dinner'), ('gnash', 'sport'), ('pezzy', 'firm')]
    for s in strings:
        print("mix_up({0}, {1}) => {2}".format(s[0], s[1], mix_up(s[0], s[1])))


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    
    if len(s) > 2:
        last3 = s[-3:]
        if last3 == 'ing':
            s = s + 'ly'
        else:
            s = s + 'ing'

    return s


def test_verbing():
    strings = ['hail', 'swimming', 'do']
    for s in strings:
        print("verbing({0}) => {1}".format(s, verbing(s)))           


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """

    import string

    end_char = ''
    if s[-1] in string.punctuation:
        end_char = s[-1]
        s = s[:-1]
    words = s.split()

    try:
        not_idx = words.index('not')
        bad_idx = words.index('bad')
    except:
        return s

    if not_idx < bad_idx:
        return " ".join(words[:not_idx] + ['good'] + words[bad_idx+1:]) + end_char
    else:
        return s


def test_not_bad():
    strings = ['This movie is not so bad', 
               'This dinner is not that bad!', 
               'This tea is not hot', 
               "It's bad yet not"]
    for s in strings:
        print("not_bad({0}) => {1}".format(s, not_bad(s)))


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """

    from math import ceil    

    a_div_pt = ceil(len(a) / 2)
    b_div_pt = ceil(len(b) / 2)

    return a[:a_div_pt] + b[:b_div_pt] + a[a_div_pt:] + b[b_div_pt:]
    

def test_front_back():
    strings = [('abcd', 'xy'), ('abcde', 'xyz'), ('Kitten', 'Donut')]
    for s in strings:
        print("front_back({0}, {1}) => {2}".format(s[0], s[1], front_back(s[0], s[1])))    


if __name__ == "__main__":
    main()
