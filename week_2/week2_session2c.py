"""
Bonus Problem: Destination City
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists 
a direct path going from cityAi to cityBi. Return the destination city, that is, 
the city without any path outgoing to another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore, 
there will be exactly one destination city.

Example 1:
Input: paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
Output: "Sao Paulo" 
Explanation: Starting at "London" city you will reach "Sao Paulo" city which is 
the destination city. 

Your trip consist of: "London" -> "New York" -> "Lima" -> "Sao Paulo".

Example 2:
Input: paths = [["B","C"],["D","B"],["C","A"]]
Output: "A"
Explanation: All possible trips are: 
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
Clearly the destination city is "A".

Example 3:
Input: paths = [["A","Z"]]
Output: "Z"

UMPIRE  
Understand what the interviewer is asking for by using test cases and questions about the problem.  
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.  
Plan the solution with appropriate visualizations and pseudocode.  
Implement the code to solve the algorithm.  
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.  
Evaluate the performance of your algorithm and state any strong/weak or future potential work.
"""

"""
U: 
    1) What happens with an empty list?
    2) Where are we going?
    3) Each origin will be unique, there are no duplicate routes
M: HashMap, Set Theory
P: 
    1) Create a HashMap, create an empty string for destination city
    2) Iterate through the array of flight plans
        a) add {destA : destB}
        b) update destination city if destB is not in the HashMap keys
    3) Return destination city
I: See below.
R: See below.
E: 
    Time: O(n) because the time will grow as the list of flight plans grows
    Space: O(n) because a hashmap is generated to keep track of paths
"""


def kevc_solution(flight_plans: list) -> str:
    if not all(flight_plans):
        return ""

    destination = ""
    flight_path = {}

    for flights in flight_plans:
        flight_path[flights[0]] = flights[1]
        if flights[1] not in flight_path:
            destination = flights[1]
    return destination


"""
U: Same as above.
M: Same as above.
P: 
    1) Create HashMap from flight plans array
    2) Use set difference to determine the missing HashMap value not in HashMap keys 
I: See below.
R: See below.
E: 
    Time: O(n) because the time will grow as the list of flight plans grows
    Space: O(n) to create relevant data structures
"""


def kevc_solution2(flight_plans: list) -> str:
    if not all(flight_plans):
        return ""

    flight_path = {flights[0]: flights[1] for flights in flight_plans}
    dest_a = set(flight_path.values())
    dest_b = set(flight_path.keys())
    return "".join(dest_a.difference(dest_b))


def jesw_solution(destArr):
    pathsDct = {}
    # creates a dictionary with the destArr
    for paths in destArr:
        pathsDct[paths[0]] = paths[1]
    print(pathsDct)
    # go through the pathsDct, find the next key
    for key in pathsDct:
        dest = pathsDct[key]
        if pathsDct.get(pathsDct[key], None) == None:
            return dest
    return None


if __name__ == "__main__":

    test_cases = [
        [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]],
        [["B", "C"], ["D", "B"], ["C", "A"]],
        [["A", "Z"]],
        [[]],
    ]

    for tests in test_cases:
        print(f"Paths: {tests}\nDestination City: {kevc_solution(tests)}\n")  # type: ignore
        print(f"Paths: {tests}\nDestination City: {kevc_solution2(tests)}\n")  # type: ignore

    print(
        jesw_solution(
            [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
        )
    )
