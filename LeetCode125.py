def is_symbols(sentence):
    """Removes unnecessary elements"""
    mstr = sentence
    for i in mstr:
        if not i.isalnum():
            mstr = mstr.replace(i, '')
            print(mstr)

    return mstr


def is_palindrome(sentence):
    """Checks is Palindrome comparing a string to its reversed version"""
    string = is_symbols(sentence).lower()
    rev_string = string[::-1]

    if string == rev_string:
        return "the string is Palindrome"
    return "the string is not Palindrome"


"""case1"""
# print(is_palindrome("A man, a plan, a canal: Panama"))
"""case2"""
# print(is_palindrome("race a car"))
"""case3"""
# print(is_palindrome(" "))

