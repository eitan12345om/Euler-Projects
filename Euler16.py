"""
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2**1000?
"""

number = str(2**int(input('number: ')))
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