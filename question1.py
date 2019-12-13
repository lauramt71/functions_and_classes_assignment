#########IMPORT LIBRARIES HERE IF NEEDED#######

################END IMPORTS####################
"""
Write a function that takes a list of numbers as input and returns the index location
within the list of the largest number. If there is more than one location within the
list that contains the largest number, then have the function return the LAST index
location. For example, f([1,2,3,2,3,1]) should return 4.
"""
def f(l):
    ##########YOUR CODE HERE##########
    x = 0   #max number
    y = 0   #index
    for n in l:
        if n >= x:
            x = n
        y += 1

    return(y)
    ###########END CODE###############
