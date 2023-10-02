import numpy
import scipy
import time

A1=numpy.array([[-3,2,-1],
   [6,-6,7],
   [3,-4,4]])

b1=numpy.array([[-1],
   [-7],
   [-6]])

A2=numpy.array([[3,18,9],
   [2,3,3],
   [4,1,2]])

b2=numpy.array([[18],
   [117],
   [283]])

A3=numpy.array([[20,15,10],
   [-3,-2.24999,7],
   [5,1,3]])

b3=numpy.array([[45],
   [1.751],
   [9]])

def solve_system(A,b,method=None):

    #Tests

    #Tests if A is a square matrix
    if A.shape[0]!=A.shape[1]:
        print("Matrix [A] is not a square matrix.")
        return None
    
    #Tests if dimensions of A and b match
    if A.shape[0]!=b.shape[0]:
        print("Matrix dimension mismatch")
        return None

    #Tests rank for consistency
    if numpy.linalg.matrix_rank(numpy.concatenate((A,b),axis=1))    \
        >numpy.linalg.matrix_rank(A):
        print("Rank is inconsistent.")
        return None

    #If inverse string parameter entered, solve using inverse. Print time spent and return solution
    if method=="inv":
        start=time.time()
        sol = numpy.dot(numpy.linalg.inv(A),b)
        end=time.time()
        print("Time taken for inverse method: ",end-start,' seconds')
        return sol
        
    #If LU string parameter entered, solve using LU method. Print time spent and return solution
    elif method=="lu":
        start=time.time()
        lu,piv=scipy.linalg.lu_factor(A)
        sol=scipy.linalg.lu_solve((lu,piv),b)
        end=time.time()
        print("Time taken for inverse LU method: ",end-start,' seconds')
        return sol
    
    #If anything other string or no string entered, solve using linalg.solve. Print time spent and return solution
    else:
        start=time.time()
        sol=numpy.linalg.solve(A,b)
        end=time.time()
        print("Time taken for linalg.solve method: ",end-start,' seconds')
        return sol

print(solve_system(A1,b1,'inv'))
print(solve_system(A1,b1,'lu'))    
print(solve_system(A1,b1))
print("******************")
print(solve_system(A2,b2,'inv'))
print(solve_system(A2,b2,'lu'))
print(solve_system(A2,b2))
print("******************")
print(solve_system(A3,b3,'inv'))
print(solve_system(A3,b3,'lu')) 
print(solve_system(A3,b3))

