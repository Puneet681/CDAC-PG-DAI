from numpy import linalg as la
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity 
'''
a = np.array([3,-4,5])
b = np.array([1,1,-2])
print(a+b)

u = np.array([2,-7,1])
print(3*u)

u = np.array([2,-3,6])
v = np.array([8,2,-3])

print(np.sum(u*v))
#OR
print(np.dot(u,v))

print("L2 norm of U = : ",np.sqrt(np.sum(u*u)))
print("L2 norm of U = : ",np.sqrt(np.dot(u,u)))
print("L1 norm of U = : ",la.norm(u,1))



print("cos(u,v) = ", np.dot(u,v)/(la.norm(u)*la.norm(v)))
print("cos(u,v) = ", cosine_similarity([u,v]))
'''

#----cosine similarity between n numbers of items(vectors)-------------------------------------
'''
item1 = np.array([-0.89,0.2,0.8])
item2 = np.array([0.2,0.4,0.5])
item3 = np.array([0.3,-0.9,0.3])
item4 = np.array([0.4,0.23,0.4])
item5 = np.array([0.34,0.3,-0.1])


print("cos(u,v) = \n", cosine_similarity([item1,item2,item3,item4,item5]))
'''

#-------matrix in numpy----------------------------
'''
a = np.array([ [1,2,-3],
               [0,-4,1] ])
print("dimension of matrix a =",a.shape)

b = np.array([[3,2,1] ,
              [0,1,0]])

print("a+b =\n",a+b)
print()
print("a-b =\n",a-b)
'''
#--------Hadamard Product--------------
'''
print("hadamard Product as a*b\n",a*b)
print("hadamard Product by np.multiply(a,b)\n",np.multiply(a,b))
'''
#------matrix multiplication-------------
'''
a = np.array([ [1,3],
               [2,-1] ])

b = np.array([ [2,0,-4],
              [3,-2,6] ])
print(a.shape)
print(b.shape)
print("AB = \n", np.matmul(a,b))
print("AB = \n", a@b)
print("AB = \n", np.dot(a,b))
'''
#-----identity matrix in numpy-------
np.eye(3)

#-------Example-----------

b = np.array([ [1,3],
               [5,3] ])

ans = (2*(b@b))-(4*b)+(3*(np.eye(2)))
ans2 = ((b@b) - (4*b) - (12*np.eye(2)))
print("f(x) = 2X^2-4x+3 =\n",ans)
print()
print("g(x) = x^2-4x-12 =\n",ans2)

a = np.array([[2,1],[4,0]])


#-----------determinant---------------

print("determinant = ",la.det(a))
