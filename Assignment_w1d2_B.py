# 1.	Create a list with one number, one word and one float value. Display the output of the list.
print([1,"number",0.1])

# 2.	I have a nested list [1,1[1,2]], how to grab the value of 2 from the list.
# there is a typo in the list. I will assume it is: [1,1,[1,2]]
print([1,1,[1,2]][2][1])

# 3.	lst=['a','b','c'] What is the result of lst[1:]?
# the result would be a sub list starting with index 1 till the end of the list elements
lst=['a','b','c']
print(lst[1:])

# 4.	Create a dictionary with weekdays an keys and week index numbers as values.do assign dictionary to a variable
weekdays = {
  "Sunday" : 0,
  "Monday" : 1,
  "Tuesday" : 2,
  "Wednesday" : 3,
  "Thursday" : 4,
  "Friday" : 5,
  "Saturday" : 6
}
print(weekdays)

# 5.	D={‘k1’:[1,2,3]} what is the output of d[k1][1]
# the output would be an error because the lowercase variable d is not declared and the k1 is not surrounded with quotes
# if I were to assume that there are typos, this would be the answer: the integer 2
D={'k1':[1,2,3]}
print(D['k1'][1])

# 6.	Can you create a list [1,[2,3]] into a tuple
# yes you can, although after the tuple is created, it cannot be altered
print( ([1,[2,3]]) )

# 7.	With a single set function can you turn the word ‘Mississippi’ to distinct character word.
# yes
example = set('Mississippi')
print(example)

# 8.	Can you add an element ‘X’ to the above created set
# yes
example.add('X')
print(example)

# 9.	Output of set([1,1,2,3])
print(set([1,1,2,3]))

# Write a program which will find all such numbers which are divisible
# by 7 but are not a multiple of 5,between 2000 and 3200 (both included).
#	The numbers obtained should be printed in a comma-separated sequence on a single line.
sequence = ""
for number in range(2000, 3201):
  if number % 7 == 0 and number % 5 != 0:
    sequence += str(number)+","
print(sequence[:-1])

# Write a program which can compute the factorial of a given numbers.
#	The results should be printed in a comma-separated sequence on a single line.
#	Suppose the following input is supplied to the program:
#	8
#	Then, the output should be:
#	40320
output = ""
user_input = 1
print("Please enter numbers to find their factorials (enter 0 to end)")
while (user_input != 0):
  user_input = int(input(""))
  if user_input == 0:
    continue
  value = 1
  for number in range(1,user_input+1):
    value *= number
  output += str(value)+","
print(output[:-1])