#ստուգել թվի 1 արժեքով բիթերի քանակը կենտ է, թե զույգ
def count_of_bits(num):
    """checks the count of '1'"""
    count = 0
    while num:
        count += num & 1
        num = num >> 1
    return count


def odd_or_even(num):
    """count is even or odd?"""
    if count_of_bits(num) & 1:
        answer = f"The count is {count_of_bits(num)} and it is odd"
    else:
        answer = f"The count is {count_of_bits(num)} and it is even"
    return answer

"""case1"""
# print(odd_or_even(21))
"""case2"""
# print(odd_or_even(34))
