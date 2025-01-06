# Getting the sum of numbers
# mrdthu003
# 01 September 2024

def sum_to_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_to_n(n-1)