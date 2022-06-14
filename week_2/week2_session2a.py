"""
Problem 1: Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
"""
U:
    Input: array of numbers -> Output: value of the majority element
    Majority element appears more than n/2 times

    Questions:
        1) What if there is only two elements? No tie breakers?
        2) What should we return if the array is empty? None.
        3) Sorted. Not given.
        4) Space. Worry later.
        5) Time. As fast as possible.

M:
    HashMap, recursion?, collection.Counter - O(1), Sorting - O(n*logn)

P:
    1) Create a dictionary
    2) loop through our nums array
        a) Numbers that that not seen - add to dictionary
        b) Numbers that have been seen - increment by 1
    3) Find the max counted key and return key

I:
    See below.
R:
    See below.
E:
    Time: O(n) because looping through the array and dictionary items
    Space: O(n) because another DS is used to maintain counts
"""


import collections


def solution(array: list) -> int:
    seen = {}

    for num in array:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1

    for key, count in seen.items():
        if count > len(array) // 2:
            return key

    return -1


"""
Solution below uses the counter object from collections.
E: 
    Time: O(n) because to create a Counter object, the list needs to be traversed and added
    Space: O(n) because all the values that were in the array object are copied to Counter
"""


def kevc_solution(array: list):
    counts = collections.Counter(array)
    return max(counts, key=counts.get)  # type: ignore


def tpham_solution(array: list) -> int:
    seen = {}

    for num in array:
        if num not in seen:
            seen[num] = 1
        else:
            seen[num] += 1

    max_count = max(seen, key=seen.get)  # type: ignore
    return max_count


if __name__ == "__main__":
    test_cases = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [3, 3, 3, 3, 1, 1, 1],
    ]

    for array in test_cases:
        print(f"Current array: {array} | Majority element: {solution(array)}")
        print(f"Current array: {array} | Majority element: {kevc_solution(array)}")
        print(f"Current array: {array} | Majority element: {tpham_solution(array)}")
