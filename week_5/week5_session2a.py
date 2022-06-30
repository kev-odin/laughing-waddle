"""
Problem #1: Evaluate Postfix expression
Write a function to evaluate the value of an expression in postfix notation
represented by a string with numbers between 0 and 9 and operators separated by whitespace.
The expression supports 4 binary operators '+', '*', '-' and '/'.

Note: Arithmetic Expressions can be written in Infix, Prefix or Postfix notations.

Infix notations are human readable form of expression. For example: “3 + 4”.
Prefix notations has operators before the operands like “+ 3 4” for the previous infix example.
Postfix notations keep operators after operands. A postfix expression for the examples above would be “3 4 +”.
Play with this infix, prefix and postfix notations on this infix and postfix converter and build an intuition.

Example:
Input: "5 1 2 + 4 * + 3 -"
Output: 14

The expression is evaluated as follows:
5 3 4 * + 3 -
5 12 + 3 -
17 3 -
14

UMPIRE
Understand what the interviewer is asking for by using test cases and questions about the problem.
Match what this problem looks like to known categories of problems, e.g. Linked List or Dynamic Programming and strategies or patterns in those categories.
Plan the solution with appropriate visualizations and pseudocode.
Implement the code to solve the algorithm.
Review the code by running specific example(s) and recording values (watchlist) of your code's variables along the way.
Evaluate the performance of your algorithm and state any strong/weak or future potential work.

U:
    bao: Should the number of value is more than the number of operands? And vice-versa. What is the input?
    far: What happens if the string is empty? 
    jes: Single operand without two values? Always going to have a valid expression.
    kev: Driving... - Single value - What do we return?
    tin: Would it be error if divide by 0? Example: 6 0 /
    xin: Agree.
M:
    * Stack
    * Tree traversal
    * Recursion
P:
    5 3 4 * + 3 -
    Create a stack.
    Push elements onto a stack one by one if they are values
    Pop twice for two numbers when we encounter an operand (* + - /)
        Keep track of first and second values popped
        Calculate and push the result back on the stack
    Continue we reach the end of the string
    Return the last element on the stack
I:
    * See below
R:
    * See below
E:
    Time: O(n) b/c of the length of the expression
    Space: O(n) b/c stack will scale with the input

"""


def postfix(exp: str) -> int:
    cool_stack = []

    for token in exp:
        if token in "*+-/":

            second = cool_stack.pop()
            first = cool_stack.pop()

            if token == "*":
                cool_stack.append(first * second)
            elif token == "+":
                cool_stack.append(first + second)
            elif token == "-":
                cool_stack.append(first - second)
            elif token == "/":
                cool_stack.append(first // second)

        elif token != " ":
            cool_stack.append(int(token))

    return cool_stack.pop() if len(cool_stack) != 0 else 0


if __name__ == "__main__":
    example = ""
    print(postfix(example))
