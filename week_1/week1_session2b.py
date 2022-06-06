"""
Problem #2 Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Examples:

Input: s = "aba"
Output: true

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Input: s = "abc"
Output: false
"""

"""
U: Determine if a given string is a palindrome, if a single character is removed
M: string slicing, recursion  
P: 
    Base case:
    1) Length of the string is less than or equal to 1, return true
    Recursive cases:
    1) First and last char in substring are the same, continue recursive calls
    2) Different char, increment either left or right side and pass result to next 
    recursive call, change deleted flag to True.
    3) Another different character would result with termination of recursive calls.

I: See code below.  
R: Main function has test cases.  
E: 
    Time complexity: O(n) because the size of the input is determined by string length
    Space complexity: O(n) because the recursive calls will be held in the call stack
"""


def kevc_solution(s: str, deleted: bool = False):
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return kevc_solution(s[1 : len(s) - 1])
    else:
        if deleted:
            return False
        return kevc_solution(s[1:], deleted=True) or kevc_solution(
            s[0:-1], deleted=True
        )


if __name__ == "__main__":
    test_cases = ["aba", "abca", "abc", "aaaa", "aaca", "addbca"]
    for val in test_cases:
        print(kevc_solution(val))
