import numpy as np
from pypoly import Polynomial
y = []
x = []
for n in range(1,13):
	y.append(long(1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10))
	x.append(n)

equations = np.array([[point[0] ** i for i in range(order)] for point in X])
values = np.array([point[1] for point in X])
coefficients = np.linalg.solve(equations, values)

# print scipy.interpolate.lagrange(x, y)
# for j in range(1,10):
# 	testy = []
# 	q = scipy.interpolate.lagrange(x[0:j], y[0:j])
# 	# for n in range(1,3):
# 	# 	temp = 0
# 	# 	for p in range(len(q)):	
# 	# 		temp += (n**p)*q[p]
# 	# 	testy.append(temp)
# 	# print testy
# 	print q
# print y
