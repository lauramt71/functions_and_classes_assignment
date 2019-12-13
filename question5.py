#########IMPORT LIBRARIES HERE IF NEEDED#######
import statistics
import math
################END IMPORTS####################
"""
Write a function that returns both the sample mean and sample standard deviation of a list of numbers. Your function will calculate
the mean and standard deviation separately and the last line of your function should look something like

return m, sd

where m is the mean, and sd is the standard deviation. Make sure to return them in that order. See
https://www.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review
for the equations to calculate the sample standard deviation. Make sure you use the sample standard deviation and not the population
standard deviation.
"""

def f(l):
    ##########YOUR CODE HERE##########
    num = 0
    i = 0
    #Step 1: Find the mean
    m = statistics.mean(l)

    #Step 2: Subtract the mean from each score
    #Step 3: Square each deviation
    for x in l:
        num += (x - m) ** 2
        i += 1

    #Step 4: Add the squared deviations
    #Step 5: Divide the sum by one less than the number of data points
    #Step 6: Take the square root of the result from Step 5
    if i == 1:
        return('None')
    else:
        sd = math.sqrt(num/(i-1))
    return(m,sd)
    ###########END CODE###############
