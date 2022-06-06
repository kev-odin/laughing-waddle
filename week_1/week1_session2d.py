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


def kevc_solution(array: list):
    if len(array) == 1:
        return [array]
    res = [list(x) for x in list(permutations(array))]
    return res


"""
U: Given a list of distinct integers, return a list of all combinations.
M: Recursion, set theory
P: 
    Base case:
    1) If the length of the array is 1, then return the array
    Recursive case:
    1) Determine remaining elements, recurse through those options
    2) Append remaining elements to the current value in the iteration loop
I: See code below.
R: Follow the test cases below
E: 
    Time complexity: O(n!) ??? I think this is correct. Anyone want to contribute to this??
    Space complexity: O(n!) Since the algorithm is storing all the permutations, which grows based on the number of elements.
"""


def kevc_solution2(array: list):
    if len(array) == 1:
        return [array]

    perm_list = []
    for val in array:
        remaining_elements = [x for x in array if x != val]
        temp = kevc_solution2(remaining_elements)

        for elements in temp:
            perm_list.append([val] + elements)

    return perm_list


if __name__ == "__main__":
    test_nums = [[1, 2, 3], [0, 1], [1]]
    for val in test_nums:
        print(kevc_solution(val))
        print(kevc_solution2(val))
