def single_number(nums):
    """
    The way to find the unique element is by using the XOR bitwise
    operator which returns 1 only if one of the element is 1 and false otherwise.
    In the loop, each of the integers in the array are XORed with uniqueId starting at 0.
    """
    for i in range(1, len(nums)):
        nums[0] ^= nums[i]
    return nums[0]

"""case"""
# print(single_number([1, 1, 2, 3, 3, 4, 4, 8, 8]))

