"""
Problem 2: Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value 
I 1
V 5
X 10
L 50 
C 100 
D 500 
M 1000

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900. 
Given a roman numeral, convert it to an integer.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

"""
U: 
M:
P:
I:
R:
E:
"""


def kevc_solution(nums: str) -> int:
    if len(nums) == 0:
        return -1

    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    n = len(nums)
    result = roman_dict[nums[n - 1]]
    for i in range(n - 2, -1, -1):
        if roman_dict[nums[i]] >= roman_dict[nums[i + 1]]:
            result += roman_dict[nums[i]]
        else:
            result -= roman_dict[nums[i]]
    return result


"""
Understanding:
_ Convert Roman numerals to Arabic numerals
_ Some numbers such as 4, 9 are IV and IX not IIII and VIIII
_ What if the input is IIII? Should we return 4 or 2 & 3 or 3 & 2 -> assume that all the inputs are valid
_ What if the input is an empty string? Assume the string is not empty
_ What is the space constraint?
_ WHat is the time constraint?

Match:
_ Dictionary, HashMap, array

Plan:
_ Initilize a dictionary to store all the Roman numbers as keys and Arabic numerals as values.
_ Make a sum variable to store the sum
_ Loop from the end of the string input and check the next character. If the next character is less than 
the current chacacter, subtract it from the current character and add to the sum, otherwise, just convert
and add every character to the sum

Implement: see below

Review:

Evaluate:
*Time complexity : O(n)
*Space complexity : O(n)
"""


def convertNumbers(s):
    numSum = 0
    numDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i in range(len(s) - 1, 0, -1):
        if numDict(s[i]) <= numDict(s[i - 1]):
            numSum += numDict(s[i])
        else:
            numSum += numDict(s[i]) - numDict(s[i - 1])
    return numSum


if __name__ == "__main__":
    test_cases = ["III", "LVIII", "MCMXCIV", "XIX"]

    for tests in test_cases:
        print(f"Roman: {tests}\t | Value: {kevc_solution(tests)}")
        # print(f"Roman: {tests}\t | Value: {convertNumbers(tests)}")
