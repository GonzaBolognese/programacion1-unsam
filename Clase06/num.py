import numpy as np

a = np.array([[1,2,3,4,5,6],
             [5,6,7,8,9,0]])

b = np.arange(6,36,3)

array_ejemplo = np.array([[[0, 1, 2, 3],
      [4, 5, 6, 7]],
      [[0, 1, 2, 3],
      [4, 5, 6, 7]],
      [[0 ,1 ,2, 3],
      [4, 5, 6, 7]]])

print(a[1,4])
print(b)
print(array_ejemplo.ndim)
print(array_ejemplo.shape)
print(array_ejemplo.size)