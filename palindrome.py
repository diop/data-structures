#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    # once implemented, change is_palindrome to call is_palindrome_iterative
    # to verify that your iterative implementation passes all tests
    # for i in xrange(0, len(text)/2):
    #   if text[i] != text[len(text)-i-1]:
    #       return False
    #   return True
    left_bound = 0
    right_bound = len(text) - 1

    while left_bound <= right_bound:
        while text[left_bound] not in string.ascii_lowercase:
            left_bound += 1
        while text[right_bound] not in string.ascii_lowercase:
            right_bound -= 1
            
        if text[left_bound] != text[right_bound]:
            return False
        
        index_one += 1
        index_two -= 1

    return True
    

def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if len(text) <= 1:
        return True
    
    if text[left] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left + 1, right)
    if text[right] not in string.ascii_lowercase:
        return is_palindrome_recursive(text, left, right -1)
    if text[left]

    if text[0] != text[-1]:
        return False
    
    return is_palindrome_recursive(text, left + 1, right -1)
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a spalindrome')


if __name__ == '__main__':
    main()
