'''
Write a method to convert a string representation of an integer into its equivalent integer number.

Examples:

Input: "123"
Output: 123

Input: "-6714"
Output: -6714
'''
'''
U:
kev: what happend when an empty string is given? Assume there is no empty string.
bao: Is casting allowed? Assume casting is not allowed
jes: agreed with Xingguo
xin: number with leading zeros valid integer? Assume there is no such number
tin: agreed with everyone
far: Are there white spaces or special characters? Assume all characters are integers and minus sign.
    Is there any limit to the length of the string? There is no limit, unlimited memory
M: 
String, casting
P:
Initialize the exponential number to be 0
Loop through the string from the back:
  Check if the character at the end of the loop is a neg sign or not, if it is we would mutiple the output to -1
  Using ord - 48 to convert the digit to integer then multiply it by the 10 to the exp number
  Increment the exp number
I:
See below
R:
E:
TC -> O(n)
SC -> O(1)
'''
def convert(s):
  exp = 0
  sum = 0
  for i in range(len(s) - 1, -1, -1):
    if s[i] == "-":
      return -sum
      
    digit = ord(s[i]) - 48
    num = digit * (10**exp)
    exp += 1
    sum += num
  return sum

if __name__ == "__main__":
  print(convert("89450349850943850493"))