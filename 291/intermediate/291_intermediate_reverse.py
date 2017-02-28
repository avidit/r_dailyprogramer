opr = {
			'+': lambda b, a: a + b,
      '-': lambda b, a: a - b,
      '*': lambda b, a: a * b,
      'x': lambda b, a: a * b,
      '/': lambda b, a: a / b,
      '//': lambda b, a: a // b,
      '%': lambda b, a: a % b,
      '^': lambda b, a,: a ** b
}

def factorial(x):
    return x * factorial(x - 1) if x > 1 else 1

def rpn(input_data):
	stack = []
	for i in input_data.split():
		if i == '!': stack.append(factorial(stack.pop()))
		elif i in opr: stack.append(opr[i](stack.pop(), stack.pop()))
		else: stack.append(float(i))
	return stack[0]


input_data_1 = "1 2 3 4 ! + - / 100 *"
input_data_2 = "100 807 3 331 * + 2 2 1 + 2 + * 5 ^ * 23 10 558 * 10 * + + *"

if __name__ == "__main__":
	print(rpn(input_data_1))
	print(rpn(input_data_2))
