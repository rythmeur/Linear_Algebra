import numpy as np
A= np.eye( 4, 4 )
print( A )

"""
numpy.tril(m, k=0)[source]
Lower triangle of an array.

Return a copy of an array with elements above the k-th diagonal zeroed.

Parameters :
m : array_like, shape (M, N)
Input array.
k : int, optional
Diagonal above which to zero elements. k = 0 (the default) is the main diagonal, k < 0 is below it and k > 0 is above.
Returns :
tril : ndarray, shape (M, N)
Lower triangle of m, of same shape and data-type as m.
"""
import numpy as np
A= np.matrix( '1,2,3;4,5,6;7,8,9' )
print( A )
B= np.tril( A )
print( B )
B= np.tril( A , 1 )
print( B )
B= np.tril( A , -2 )
print( B )
B= np.triu( A )
print( B )
B= np.triu( A , 1 )
print( B )
B= np.tril( A , 2 )
print( B )

a = np.matrix( '-1,0,2;2,-1,1;3,1,-1' )
b = np.matrix('-1; 2; 1')
print a * b

a = np.array([[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]])
b = np.array([1, 2, 3])

print a*b

print a