def first_unique_char(sstr):
    """
    Checks the count and then count equals 1 returns the index of element
    """
    if sstr == '':
        return -1

    for i in sstr:
        if sstr.count(i) == 1:
            return sstr.index(i)
            break

    return -1

"""case1"""
# print(first_unique_char("leetcode"))
"""case2"""
# print(first_unique_char("loveleetcode"))
"""case3"""
# print(first_unique_char("aabb"))
