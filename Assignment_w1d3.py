# 1.	 Write a Python program to find those numbers which are divisible by 7
#       and multiple of 5, between 1500 and 2700 (both included). Go to the editor
sequence = ""
for number in range(1500, 2701):
  if number % 7 == 0 and number % 5 == 0:
    sequence += str(number)+","
print(sequence[:-1])

# 2.   Write a Python program to convert temperatures to and from celsius, fahrenheit.
def convertTemperatureScales(temp, convert_from, convert_to):
  if str(convert_from).lower() == "c":
    if str(convert_to).lower() == "f":
      return (temp * 5/9) + 32
  elif str(convert_from).lower() == "f":
    if str(convert_to).lower() == "c":
      return (temp - 32) * 5/9
fahrenheit = 100.0
celsius = 0.0
print("F to C where F is "+str(fahrenheit)+": "+str(convertTemperatureScales(fahrenheit, "f", "c")))
print("C to F where C is "+str(celsius)+": "+str(convertTemperatureScales(celsius, "c", "F")))

import random

# 3.   Write a Python program to guess a number between 1 to 9.
guess_correct = False
random_number = random.randrange(1, 10)
print("Guess a random number between 1 and 9: ")
while True:
  if(input() == str(random_number)):
    print("Well guessed!")
    break
  print("Guess Incorrect. Please guess again: ")

# 4-5.  Write a Python program to construct the following pattern, using a nested for loop.
stars = [["*"],["*","*"],["*","*","*"],["*","*","*","*"],["*","*","*","*","*"]]
stars.extend(stars[-2::-1])
for element in stars:
  star_string = ""
  for star in element:
    star_string += star+" "
  print(star_string)

# 6.	 Write a Python program that accepts a word from the user and reverse it.
print(input("Enter a word to be reversed: ")[::-1])

# 7 Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = range(random.randrange(1, 50), random.randrange(50, 101))
print("Sample range: "+str(numbers[0])+" - "+str(numbers[-1]))
print("Number of even numbers: "+str(len([x for x in numbers if x % 2 == 0])))
print("Number of odd numbers: "+str(len([x for x in numbers if x % 2 != 0])))

# 8.	Write a Python program that prints each item and its corresponding type from the following list
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for element in datalist:
  print(type(element))

# 9.	Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
output = ""
for num in range(0, 7):
  if num == 3 or num == 6:
    continue
  else:
    output += str(num)+" "
print(output[:-1])