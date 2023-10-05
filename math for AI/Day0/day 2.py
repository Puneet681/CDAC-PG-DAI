
import numpy as np
from numpy import linalg as la # importing linear algorithm ---> linalg
import matplotlib.pyplot as plt
'''
a = np.array([[3,5],[2,3]])
b = np.array([[5,3],[2,1]])
print("inverse of a=\n",la.inv(a)) # command to inverse a matrix --->  la.inv()
print("inverse of a=\n",la.inv(b))

c = np.array([[1,1,0],[1,1,1],[0,2,1]])
print("inverse of a=\n",la.inv(c))

d = np.array([[4,2],[2,3]])
print("Rank of matrix D : ",la.matrix_rank(d))

e = np.array([[2,2],[4,4]])
print("Rank of matrix E : ",la.matrix_rank(e))


plt.xlim(0,10)
plt.ylim(0,10)

plt.arrow(0,0,3,2, head_width=0.3,head_length = 0.3 , color ='red')
plt.arrow(0,0,2,3, head_width=0.3,head_length = 0.3 , color ='green')
plt.arrow(3,2,5,3, head_width=0.3,head_length = 0.3 , color ='blue')
plt.arrow(2,3,6,2, head_width=0.3,head_length = 0.3 , color ='purple')

plt.show()

a = np.array([[2,1],
              [3,-5]])
b = np.array([[7],[4]])

c = (la.inv(a)@b)

print(c)

print(la.solve(a,b))

# Cramers Exmaple finding x,y,z

x = [[1,1,2],
     [2,3,6],
     [3,6,10]]

y = [[4],
     [10],
     [17]]

z = la.solve(x,y)

print("solution is = \n",z)


A = np.array(
    [[1,1,2],
     [2,3,6],
     [3,6,10]])

print(A[1,1])

'''


#=-=-=-=-=-=-EIGEN VALUE and EIGEN VECTORS=-=-=-=-=-=-=-=-=-=-=-


m = np.array([[5,-10,-5],
              [2,14,2],
              [-4,-8,6]])

print(la.eig(m))


#=-=-=-=-=-=-=-=-=Find Orthonormalized vector=-=-=-=-=-=-=-=-=-=-=-=-=

a = np.array([[3,2],[-4,-6]])
v1 = a[0]
v2 = a[1]

u1 = v1/la.norm(v1)
w2 = v2 - np.dot(u1,v2)*u1
u2 = w2/la.norm(w2)

o_n_a = np.array([u1,u2])
print("Orthonormalized vector : \n",o_n_a)


def ortho_norm(x):
    a = np.array([[3,2],[-4,-6]])
    v1 = x[0]
    v2 = x[1]

    u1 = v1/la.norm(v1)
    w2 = v2 - np.dot(u1,v2)*u1
    u2 = w2/la.norm(w2)
    o_n_a = np.array([u1,u2])
    return o_n_a


print("Orthonormalized vector : \n",ortho_norm(a))
s = ortho_norm(a)
print(np.dot(s[:,0],s[:,1]))



def ortho_norm_3(x):
    v1 = x[0]
    v2 = x[1]
    v3 = x[2]

    u1 = v1/la.norm(v1)
    w2 = v2 - np.dot(u1,v2)*u1
    u2 = w2/la.norm(w2)

    w3 = v3 - np.dot(u1,v3)*u1 - np.dot(u2,v3)*u2
    u3 = w3/la.norm(w3)

    o_n_a = np.array([u1,u2,u3])
    return o_n_a

a = np.array([[1,1,0],
              [1,1,1],
              [0,2,1]])

s1 = ortho_norm_3(a)
print(s1[:,1],s1[:,0])
