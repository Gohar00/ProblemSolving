def product_except(nums):
    """
    This function generate an answer_list,which is the product of two lists,which is the product of two arrays,
    which in turn represent the product of the elements to the right and left of each element
    """
    ans_1 = [1] * len(nums)
    ans_2 = [1] * len(nums)

    for i in range(1, len(nums)):
        ans_1[i] = nums[i - 1] * ans_1[i - 1]
        print(ans_1)

    for i in reversed(range(len(nums) - 1)):
        ans_2[i] = nums[i + 1] * ans_2[i + 1]
        print(ans_2)

    return [ans_1[i] * ans_2[i] for i in range(len(nums))]


"""case1"""
# print(product_except([-1, 1, 0, -3, 3]))

"""case2"""
# print(product_except([1, 2, 3, 4]))
