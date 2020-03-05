import numpy as np
import time
import math

start=time.time()

def gauss(A, b, x, n):

    L = np.tril(A)
    U = A - L
    for i in range(n):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        print(x)
    return x

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1, 1, 1]
n = 20

print(gauss(A, b, x, n))
end=time.time()
total=end-start


start2=time.time()
print(np.linalg.solve(A,b))
end2=time.time()
total2=end2-start2
print("The computation at {} iterations for {} matrix took:{}, versus deterministic method {} ".format(n, str(math.sqrt(A.size)) + ' x ' + str(math.sqrt(A.size)) ,total,total2))
