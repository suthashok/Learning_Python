# Python : repr()

import numpy as np

a1=np.array([1,2,3])

print(a1)

print(str(a1))

print(repr(a1))

class satellite:
	def __init__(self,name):
		self.name=name

m=satellite("Moon")

print(repr(m))
