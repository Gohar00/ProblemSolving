#հաշվել թվի 1 արժեքով բիթերի քանակը
"""time comp O(logn)"""
def count_of_bits(num):
    """Converts the decimal number to binary and check the count of '1'"""
    bin_num = bin(num)
    return bin_num.count("1")


number = int(input("Enter the number"))
print(count_of_bits(number))
