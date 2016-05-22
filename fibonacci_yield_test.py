def fibonacci():
	a, b = 0, 1
	while True:
		yield b
		a, b = b, a + b

fib = fibonacci()

list_fib = [fib.next() for i in xrange(10)]

print list_fib