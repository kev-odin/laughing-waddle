"""
Problem #3 Pow(x,n)
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Examples:

Input: x = 2.00000, n = 10
Output: 1024.00000

Input: x = 2.10000, n = 3
Output: 9.26100

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""

def exponential(x,n):
  outPut = (x ** n)
  return (round(outPut, 5))

#test all cases
def test(actual, expected): # unit test
    import sys
    linenum = sys._getframe(1).f_lineno
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'.".
               format(linenum, expected, actual))
    print(msg)

def test_suite(): #test suite with multiple cases.
    test(exponential(2.00000,10), 1024.00000)
    test(exponential(2.10000,3), 9.26100)
    test(exponential(2.00000,-2), 0.25000)
test_suite() 
