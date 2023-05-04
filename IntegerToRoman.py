# Given an integer 'N', teh task is to find its corresponding Roman numerals.
# Roman Numerals are represented by seven different symbols: I, V, X,L,C,D,and M.


from os import *
from sys import *
from collections import *
from math import *

def intToRoman(num):
    # Write your code here.
    romans = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }
    div = 1
    while num >= div:
        div *= 10
 
    div /= 10
 
    res = ""
 
    while num:
        lastNum = int(num / div)
        if lastNum <= 3:
            res += (romans[div] * lastNum)
        elif lastNum == 4:
            res += (romans[div] +
                        romans[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romans[div * 5] +
            (romans[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romans[div] +
                        romans[div * 10])
 
        num = floor(num % div)
        div /= 10
         
    return res