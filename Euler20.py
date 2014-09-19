"""
n! means n × (n − 1) × ... × 3 × 2 × 1
For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!
"""

import math

number = math.factorial(int(input('Number: ')))
correct = False
working_number = 0

while correct == False:
	working_number += int(str(number)[-1])
	number = int(number) // 10
	if number < 1:
		correct = True

print(working_number)



#Get last digit = working_number
#Divide by ten // and set number = number