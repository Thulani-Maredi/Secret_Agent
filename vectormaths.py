# Program that acts as a module for another program
# mrdthu003
# 10 August 2024

import math

def vector_sum(A,B):
    add = []
    for index in range(len(A)):
        ans = A[index] + B[index]
        add.append(ans)
    return add    
    
def vector_product(A,B):
    product = []
    for index in range(len(B)):
        ans = A[index] * B[index]
        product.append(ans)
    total = sum(product)
    return total
    
def vector_norm(A):
    square = []
    for index in range(len(A)):
        ans = A[index] ** 2
        square.append(ans)
    root = math.sqrt(sum(square))
    return root
    
def vector_norm(B):
    square = []
    for index in range(len(A)):
        ans = B[index] ** 2
        square.append(ans)
    root = math.sqrt(sum(square))
    return root
    