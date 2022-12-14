#հաշվել թվի 1 արժեքով բիթերի քանակը
"""time comp. O(logn)
   space comp. O(1)"""
def count_of_bits(num):
    """Checks the count of '1'"""
    count = 0
    while num:
        count += num & 1
        num = num >> 1
    return count


"""case1"""
print(count_of_bits(34))
