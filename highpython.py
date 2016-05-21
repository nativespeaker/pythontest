import timeit

lst = []

def test_xrange(n):
	global lst
	lst = []
	for i in xrange(n):
		lst.append(1)
	assert len(lst) == n

def test_range(n):
	global lst
	lst = []
	for i in range(n):
		lst.append(1)
	assert len(lst) == n

def test_while(n):
	global lst
	lst = []
	i = 0
	while i < n:
		lst.append(1)
		i += 1
	assert len(lst) == n

def test_list_comprehension(n):
	global lst
	lst = []
	lst = [1 for i in xrange(n)]
	assert len(lst) == n

timer1 = timeit.Timer('test_xrange(4000000)','from __main__ import test_xrange')
timer2 = timeit.Timer('test_range(4000000)','from __main__ import test_range')
timer3 = timeit.Timer('test_while(4000000)','from __main__ import test_while')
timer4 = timeit.Timer('test_list_comprehension(4000000)','from __main__ import test_list_comprehension')

print 'xrange:', timer1.timeit(number=2)
print 'range:', timer2.timeit(number=2)
print 'while:', timer3.timeit(number=2)
print 'list comprehension:', timer4.timeit(number=2)
