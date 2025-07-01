import numpy as np

# m33=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float32)

# print(m33)

n=np.array([1,2,3])

print(n)

m=n
l=n.copy()
n[0]=5

print(n)
print(m)
print(l)

