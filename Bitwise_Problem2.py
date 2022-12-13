def count_of_bits(num):
    """Converts the decimal number to binary and check the count of '1'"""
    bin_num = bin(num)
    return bin_num.count("1")


def odd_or_even(num):
    """count is even or odd?"""
    if count_of_bits(num) % 2 != 0:
        answer = f"The count is {count_of_bits(num)} and it is odd"
    else:
        answer = f"The count is {count_of_bits(num)} and it is even"
    return answer


"""case1"""
# print(odd_or_even(21))
"""case2"""
# print(odd_or_even(34))
