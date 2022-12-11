def solution(n, k):
    return n & ~(1 << (k - 1))


"""case1"""
# print(solution(374823748, 13))

"""case2"""
# print(solution(37, 4))

"""case3"""
# print(solution(2734827, 4))
