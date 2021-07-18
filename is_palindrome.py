def reverse(string):
    """ Reverse a string
            Atts:
                string (str)
            Rtn:
                reversed_string (str)
    >>> print(reversed('hello'))
    olleh
    """
    reversed = ''
    for i in string:
        reversed = i + reversed
    return reversed

def is_palindrome_v1(string):
    """ Return true if string is a palindrome. Reversed string method
            Atts: 
                string (str)
            Rtn:
                (bool)

    >>> is_palindrome_v1('racecar')
    True
    >>> is_palindrome_v1('hello')
    False
    >>> is_palindrome_v1('noon')
    True
    """
    return string == reverse(string)

def is_palindrome_v2(string):
    """ Slicing method
    """
    return string == string[::-1]

def is_palindrome_v3(string):
    """ Half of string reversed method
    """
    half_of_string = len(string) // 2
    first_half_of_string = string[:half_of_string]
    last_half_of_string  = string[-half_of_string:] 
    return first_half_of_string == reverse(last_half_of_string)

def is_palindrome_v4(string):
    """ Extreme method
    """
    i = 0; j = len(string) - 1
    while string[i] == string[j] and i <= j:
        i += 1
        j -= 1
    if i >= j:
        return True
    return False