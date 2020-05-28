# -*- coding: utf-8 -*-

#Write a function so that the columns of the output matrix are powers of the input vector. The order of the powers is 
#determined by the increasing boolean argument. Specifically, when increasing is False, the i-th output column is the input vector 
#raised element-wise to the power of N - i - 1. Such a matrix with a geometric progression in each row is named for Alexandre-Theophile Vandermonde.

import numpy as np

## Iterate over each number in the input vector n times, n being the number of columns in the o/p matrix and output 
## an intermediate vector. Use diff order formula based on increasing and decreasing condition.
## Reshape the intermediate vector using the size of the input vector (rows) and n (columns) to generate the o/p matrix. 
   
def gen_vander_matrix(ipvector, n, increasing=False):
    
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    elif increasing:
        op_matx = np.array([x**i for x in ipvector for i in range(n)]).reshape(ipvector.size,n)
    
    return op_matx

print("------------OUTPUT-------------\n")

inputvector = np.array([1,2,3,4,5])
no_col_opmat = 3
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")

inputvector = np.array([1,2,4,6,8,10])
no_col_opmat = 5
op_matx_dec_order = gen_vander_matrix(inputvector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(inputvector,no_col_opmat,True)

print("---------------------------------------------------------------\n")
print("The input array is:",inputvector,"\n")
print("Number of columns in output matrix should be:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n\n",op_matx_inc_order,"\n")


#Write a function to find moving average in an array over a window:
#Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.

def mov_avg_val(mylist,N):
    cumsum, moving_aves = [0], []
    for i, x in enumerate(mylist,1):
        cumsum.append(cumsum[i-1]+x) #summing up all the values one by one and appending the list 
        if i>=N:
            moving_ave = round(((cumsum[i] - cumsum[i-N])/N),2) #computing the moving average using temp array sum array cumsum
            #can do stuff with moving_ave here
            moving_aves.append(moving_ave) # listing the moving average as an single array
            
    print("Moving average values list:",moving_aves)
    print("Length of the list l-N+1:",len(moving_aves))
                                

mylist = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
N = 3

#invoking the function
mov_avg_val(mylist, N)