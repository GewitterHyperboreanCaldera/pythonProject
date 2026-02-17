import numpy as np

x = np.array([[1,2], [3,4]])
y = np.linalg.inv(x)
print(x)
print(y)
print(np.dot(x,y))
