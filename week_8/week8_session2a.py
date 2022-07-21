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
    bao:Can we use the python sort function or do we have to implement sorting?
    what are the constraints on space and time complexity?
    far:Driving 
    jes:
    kev:Can the input array be empty? what do we return if it is?
    tin:can k be zero? no!
    xin:agree with all - are we gonna have duplicates? no duplicates
M:
  
  -use the sort function
  -use heap algorithm , (time complexity = klogk)
P:
-use the sort function
I:





R:
E:
time complexity: O(Nlogk)
space complexity: O(k)


"""# Problem #1 Reverse a String
# Write a function that reverses a string.

# Examples:

# Input: "hello"
# Output: "olleh"
def kth_smallest(arr: list, k: int) ->int:
    arr = sorted(arr)
    return arr[k - 1]
    
    
import heapq

def kth_smallest2(arr: list, k: int):
    arr1 = []
    for num in arr:
        heapq.heappush(arr1, -num)
        if len(arr1) > k:
            heapq.heappop(arr1)
            
    return -1 * heapq.heappop(arr1)
    
def kth_smallest3(arr: list, k: int):
    arr1 = []
    for num in arr:
        if len(arr1) < k:
            heapq.heappush(arr1, -num)
        else:
            heapq.heappushpop(arr1, -num)
        
            
    return -1 * heapq.heappop(arr1)
    

print(kth_smallest3([7, 10, 4, 3, 20, 15], 3))
