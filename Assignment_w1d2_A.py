# 1.	Write a string that returns just the letter ‘r’ from ‘Hello World’
print('Hello World'[8])

# 2.	String slicing to grab the word ‘ink’ from the word  ‘thinker’
print('thinker'[2:5])

# 3.	S=’Sammy’ what is the output of s[2:]”
S='Sammy'
print("the lowercase s variable is not defined and cannot be interpreted")
print("if we change the variable s to a uppercase S, the value would be: "+str(S[2:]))

# 4.	With a single set function can you turn the word ‘Mississippi’ to distinct character word.
print(set('Mississippi'))

# 5.	The word or whole phrase which has the same sequence of letters in both directions is called a palindrome. Here are few examples:
num_lines = int(input("Enter number of lines: "))
print("Enter the phrases one line at a time: ")
output = ""
import re
while num_lines > 0 :
  s = re.sub(r"[^a-z]+", "", input("").lower())
  if s == s[::-1] :
    output += "Y "
  else:
    output += "N "
  num_lines -= 1
print(output)
