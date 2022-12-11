def pivot_index(nums):
    """
    This function checks the equality of the sum of the elements to the left of each
    element(if there is no element,the sum is 0) and the sum of the elements to the right,
    if equal,returns the index of the element,else returns -1
    """

    sum_of_nums = sum(nums)
    left_sum = 0

    for piv_ind, num in enumerate(nums):
        right_sum = sum_of_nums - left_sum - num
        if left_sum == right_sum:
            return piv_ind
        left_sum += num
    return -1


"""case1"""
# print(pivot_index([1, 7, 3, 6, 5, 6]))

"""case2"""
# print(pivot_index([1,2,3]))

"""case3"""
# print(pivot_index([2,1,-1]))
