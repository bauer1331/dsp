# Matrix Algebra

import numpy as np

A = np.array( ((1,2,3), (2,7,4)) )
B = np.array( ((1,-1), (0,1)) )
C = np.array( ((5,-1), (9,1), (6,0)) )
D = np.array( ((3,-2,-1), (1,2,3)) )
u = np.array( [6,2,-3,5] )
v = np.array( [3,5,-1,4] )
w = np.array( [1,8,0,5] )

#Question 1
print A.shape #(2, 3)
print B.shape #(2, 2)
print C.shape #(3, 2)
print D.shape #(2, 3)
print u.shape #(4,)
print v.shape #(4,)
print w.shape #(4,)

# Question 2
print u+v #[ 9  7 -4  9]
print u-v #[ 3 -3 -2  1]
print 6*u #[ 36  12 -18  30]
print u*v #[18 10  3 20]
print np.linalg.norm(u) #8.60232526704

# Question 3
# q 3.1
# print A+C #not defined - ValueError: operands could not be broadcast together with shapes (2,3) (3,2) 
# q 3.2
print A-np.transpose(C) #[[-4 -7 -3] [ 3  6  4]]
# q 3.3
print np.transpose(C) + (3*D)
# q 3.4
print np.dot(B,A) #[[-1 -5 -1] [ 2  7  4]]
# q 3.5
print np.dot(B*np.transpose(A)) #not defined ValueError: operands could not be broadcast together with shapes (2,2) (3,2) 