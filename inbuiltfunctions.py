import numpy as np
a=np.array([1,2,3,4])
b=np.array([4,5,6,7])

print("array a:",a)
print("array b:",b)
print("the sum of arrays a and b",np.add(a,b))
print("the difference of arrays a and b",np.subtract(a,b))
print("the product of arrays a and b",np.multiply(a,b))
print("the division of arrays a and b",np.divide(a,b))
print("the square of arrays a and b",np.sqrt(a))
print("the exponentiAL of arrays a and b",np.exp(a))

print("the sum of arrays a and b",np.min(a))
print("the sum of arrays a and b",np.max(a))
print("the sum of arrays a and b",np.mean(a))
print("the sum of arrays a and b",np.std(a))
print("the sum of arrays a and b",np.sum(a))

c=np.array([[1,2],[3,4],[5,6]])
print("Array c")
print(c)
print("reshaped array c(2 rows,2 columns)")
print(np.reshape(c,(2,3)))
d=np.array([[1,2,3],[4,5,6]])
print("Array d")
print(d)
print("transposed array")
print(np.transpose(d))

'''
array a: [1 2 3 4]
array b: [4 5 6 7]
the sum of arrays a and b [ 5  7  9 11]
the difference of arrays a and b [-3 -3 -3 -3]
the product of arrays a and b [ 4 10 18 28]
the division of arrays a and b [0.25       0.4        0.5        0.57142857]
the square of arrays a and b [1.         1.41421356 1.73205081 2.        ]
the exponentiAL of arrays a and b [ 2.71828183  7.3890561  20.08553692 54.59815003]
the sum of arrays a and b 1
the sum of arrays a and b 4
the sum of arrays a and b 2.5
the sum of arrays a and b 1.118033988749895
the sum of arrays a and b 10
Array c
[[1 2]
 [3 4]
 [5 6]]
reshaped array c(2 rows,2 columns)
[[1 2 3]
 [4 5 6]]
Array d
[[1 2 3]
 [4 5 6]]
transposed array
[[1 4]
 [2 5]
 [3 6]]
 '''