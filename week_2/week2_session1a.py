"""
Problem 1 - Element with a frequency of K
Find the element that appears k number of times in an array.
Examples:
Input: [8, 7, 9, 6, 7, 5, 1], k = 2
Output: 7
"""

"""
UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.  

U:
- Given a List and k number. Output is an element that appears k number.
- What if k is given, but no frequency match?
- What if k is larger than the List?
- What if more than one number in the List has the same frequency equal to k.
- What if the length of the List is less than k?
- What if the length of the list is empty?
- Do we have to exit if we get frequency match k? Or do we continue to check the entire List?
M:
- Hash table, Dictionary, Counter, Frequency.
P:
- Creating a dictionary
- Iterating the List and making the key to be the value of the List and the value to be a frequency.
- Looping through the dictionary to the end to find the value match with k.
E:
- Time complexity: O(N) + O(N) = O(2N) - > O(N)
- Space complexity: O(N)
"""

"""
Solution using standard library
"""
from collections import Counter


def kevc_solution(array: list, freq: int):
    count = Counter(array)
    elements = [value for value, count in count.items() if count == freq]
    return elements


"""
U: Same as group above
M: Same as group above
P: 
    1) Use a dictionary to keep track of seen elements.
    2) Elements that are seen are incremented by 1.
    3) At the end a list of elements that match k are returned.
I: See implementation below.
R: Test cases are in main method.
E: 
    Time: O(n) because this solution will iterate through the list twice.
    Space: O(n) because this solution is storing value in another data structure
        that will grow as more elements are added.

"""


def kevc_solution2(array: list, freq: int):
    if not array:
        return

    if freq > len(array):
        return

    seen = {}
    for element in array:
        if element not in seen:
            seen[element] = 1
        else:
            seen[element] += 1

    return [value for value, count in seen.items() if count == freq]


if __name__ == "__main__":
    input = [8, 7, 9, 6, 7, 5, 1, 5]
    freq = 2
    print(kevc_solution(input, freq))
    print(kevc_solution2(input, freq))
