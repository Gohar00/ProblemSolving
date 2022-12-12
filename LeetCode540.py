def single_non_duplicate(nums):
    """
    Approach based on Binary Search: The idea is the use Binary search because the array is sorted.
    """
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = (low + high) // 2
        if mid % 2 == 1:
            mid -= 1
        if nums[mid] == nums[mid+1]:
            low = mid + 2
        else:
            high = mid

    return nums[low]

"""case"""
# print(single_non_duplicate([2, 3, 3, 4, 4, 8, 8]))
