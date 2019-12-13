#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes a list of integers as input and returns the sum of the even numbers in the list
minus the sum of the odd numbers in the list. The list may contain zeros and negative numbers. For example,
f([0, -4, 2, -3, 6, -1, 8, 6]) should return 22.
"""

def f(l):
    ##########YOUR CODE HERE##########
    even = 0
    odd =0
    for x in l:
        if x % 2 == 0:
            x += even
        else:
            y += odd

    return(even - odd)
    ###########END CODE###############
