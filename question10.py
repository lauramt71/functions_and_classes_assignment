#########IMPORT LIBRARIES HERE IF NEEDED#######
import datetime
################END IMPORTS####################
"""
Write a function that takes 2 strings s1 and s2 as inputs. These strings will represent times of the day and will be written in the format
HH:MM:SS. Your function should return the number of seconds between these 2 times. You may assume s2 always represents a later time than s1.
There are a number of ways to do this problem, but you will find making use of the datetime.datetime and datetime.timedelta modules will make
things easiest. For example, f('08:59:59','10:24:31') should return 5072.
"""

def f(s1, s2):
    ##########YOUR CODE HERE##########
    sd1 = datetime.datetime.strptime(s1, '%H:%M:%S')
    sd2 = datetime.datetime.strptime(s2, '%H:%M:%S')

    if sd2 >= sd1:
        d = sd2 - sd1
    else:
        print('error')
        d = -1

    return(d.total_seconds())

    ###########END CODE###############
