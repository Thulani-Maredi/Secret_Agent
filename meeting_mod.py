# Program to count the number of hand shakes at an event
# mrdthu003
# 31 August 2024

def handshakes(n):
    if n == 1:
        return 0
    else:
        return (n-1) + handshakes(n-1)
    
