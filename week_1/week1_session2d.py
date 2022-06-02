"""
Problem #4 Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Examples:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
"""
from itertools import permutations

def solution(array: list):
    if len(array) == 1: return array
    res = [list(x) for x in list(permutations(array))]
    return res

nums = [1, 2, 3]
print(solution(nums))