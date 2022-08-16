'''
Write a function to find if a given integer x appears more than n/2 times in a sorted array of n integers.

Input:  [1, 2, 3, 3, 3, 3, 10], x = 3
Output: True (x appears more than n/2 times in the given array)

Input:  [1, 1, 2, 4, 4, 4, 6, 6], x = 4
Output: False (x doesn't appear more than n/2 times in the given array)

Input:  [1, 1, 1, 2, 2], x = 1
Output: True (x appears more than n/2 times in the given array)
'''

'''
U:
    Bao: what if the input size is smaller than 2 or odd number? return first value if smaller than 2, round down
    Kev: Can we assume that the input is always well-formed? no guarantees that the input is well formed
    Tin: What if more than two number are duplicated? 
    Jes: What if the input is empty? Assume that there would also be at lease one value in the input array
    Far: What if there are more than one input that appears? It's not possible because we only have 100% of values not 110%
    Xin: What is the time complexity constraint? Unlimited

M:
Boolean
Counter
Hashmap
Count variable 

P:
Initilize a count to keep track of the target value's frequency
Increment the count when we see the target value as we loop through the input array
Check if the count is larger than half of the input array's length return true otherwise return false

I:
R:
below
E:
Time: O(N)
Space: O(1)
'''
def checkHalf(input, target):
    count = 0
    for num in input:
        if num == target:
            count += 1
    half = len(input) // 2
    return count > half

if __name__ == "__main__":
    print(checkHalf([1, 2, 3, 3, 3, 3, 10], 3))
    print(checkHalf([1, 1, 2, 4, 4, 4, 6, 6], 4))
    print(checkHalf([1, 1, 1, 2, 2], 1))