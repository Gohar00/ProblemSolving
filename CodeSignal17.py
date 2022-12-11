def solution(n, k):
    """
    This function converts the number to binary code as a string, the element at
    position k is replaced by 0 and then converted back to decimal
    """

    bin_number = bin(n).replace("0b", "")
    new_bin_number = (bin_number[:-k] + '0' + bin_number[-k + 1:])
    dec_number = int(new_bin_number, 2)

    return dec_number


"""case1"""
# print(solution(374823748, 13))

"""case2"""
# print(solution(37, 4))

"""case3"""
# print(solution(2734827, 4))
