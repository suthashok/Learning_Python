import numpy as np

# Chagning Array dimensions

#reshape

a1=np.arange(10)
print(a1)

# New array of 2x5

a2=np.reshape(a1,(2,5))
print(a2)


#flatten


a3=a2.flatten()
print(a3)