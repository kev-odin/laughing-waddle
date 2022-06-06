"""
Problem #1 Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Examples:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

"""
U: Determine if a given string is palindrome. 
M: Recursion, two pointers, string slicing
P: 
    1) Process the string to convert uppercase letters into lowercase
    2) Remove all non-alphanumeric characters (spaces, commas)
    3) Base cases:
        a) Length of the remaining string is less than or equal to 1 -> True
        b) If the first and last character of the string are different -> False
    4) Recursive case:
        a) Pass through the base cases, recurse through substring by slicing 2 
        characters shorter. "abccba" -> "bccb" -> "cc" -> True
I: See below
R: Test cases are in main function
E: 
Time complexity O(n) because the input is dependent on the length of the string.
Space complexity O(n) because we are using the call stack to hold our values before pop out of our recursive calls.
"""


def palindrome(s: str):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1 : len(s) - 1])


def convert(s: str):
    s = s.replace(" ", "").lower()
    new_str = []
    for i in s:
        if i.isalnum():
            new_str.append(i)

    s = "".join(new_str)
    return palindrome(s)


def kevc_convert(s: str):
    s = s.replace(" ", "").lower()
    new_str = [char for char in s if char.isalnum()]
    return palindrome("".join(new_str))
