###### Coding exercise 2 ######
# Authored By Craig Saunders

# Exercise 1.	Numbers: Example code to add two numbers 50+50 and 100-10 and print it.
# instructions weren't very clear
# Print two different numbers? or the sum of the result of both?
print((50+50)+(100-10))
# Exercise 1b
print(50+50)
print(100-10)

# Exercise 2.	30+*6,6^6,6**6,6+6+6+6+6+6
# there are no instructions for this exercise
# I will assume that these need to be printed out like the previous exercise
# print(30+*6) # '+*' is an invalid operator
# bitwise exclusive or operator ^ compares "0001 0110" and "0001 0110" which evalutates to the decimal value of 0
print(6^6)
print(6**6)
print(6+6+6+6+6+6)

# Exercise 3.	Print “Hello World” on the console output. Print output “Hello World : 10”
# Make sure capitalization and spacing matches.

print("Hello World")
print("Hello World : 10")

#Exercise 4.	Below is a mathematical calculation exercise
def getMonthlyPayment(P, R, L):
  interest = P*(R/12)
  return (P+(interest*L))/L

print(getMonthlyPayment(800000, 0.06, 103))