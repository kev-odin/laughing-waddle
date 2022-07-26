"""
Problem #1: Kth Smallest Element

Given an array and a number k where k is less than size of array, we need to find the 
k th smallest element in the given array. It is given that all array elements are distinct.

Examples:

Input: [7, 10, 4, 3, 20, 15] k = 3
Output: 7

Input: [7, 10, 4, 3, 20, 15] k = 4
Output: 10

U:
    bao:
    far:
    jes:
    kev:
    tin:
    xin:
M:
P:
I:
R:
E:
"""


def solution(arr, k) -> int:
    arr.sort()

    return arr[k - 1]


if __name__ == "__main__":
    elements = [7, 10, 4, 3, 20, 15]
    value = 1

    print(solution(elements, value))
