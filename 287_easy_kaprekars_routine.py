"""
https://goo.gl/EGPTte

Description

Write a function that, given a 4-digit number, returns the largest digit in that
number. Numbers between 0 and 999 are counted as 4-digit numbers with leading 0's.

Bonus 1
Write a function that, given a 4-digit number, performs the "descending digits"
operation. This operation returns a number with the same 4 digits sorted in
descending order.

Bonus 2
Write a function that counts the number of iterations in Kaprekar's Routine,
which is as follows. Given a 4-digit number that has at least two different
digits, take that number's descending digits, and subtract that number's
ascending digits.
"""

def largest_digit(num):
	return max(list(str(num).zfill(4)))


def desc_digits(num):
	return ''.join(sorted(list(str(num).zfill(4)), reverse = True))


def aesc_digits(num):
	return ''.join(sorted(list(str(num).zfill(4))))


def kaprekar(num, i = 0):
	if len(set(list(str(num)))) >= 2:
		while (num != 6174):
			num = int(desc_digits(num)) - int(aesc_digits(num))
			i += 1
	return i


print('largest_digit:')
print(largest_digit(1234))
print(largest_digit(3253))
print(largest_digit(9800))
print(largest_digit(3333))
print(largest_digit(120))

print('\ndesc_digits:')
print(desc_digits(1234))
print(desc_digits(3253))
print(desc_digits(9800))
print(desc_digits(3333))
print(desc_digits(120))

print('\nkaprekar:')
print(kaprekar(6589))
print(kaprekar(5455))
print(kaprekar(6174))
print(kaprekar(3333))

