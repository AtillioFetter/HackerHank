#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar: list[int]) -> int:
    """
    This function calculates the sum of all the numbers inside a list.
    
    Args:
        ar(list[int]): The input list (array).
    
    Returns:
        (int): The sum of the elements inside the array.
    """
    return sum(ar)

if __name__ == '__main__':
    fptr = open('Easy/SimpleArraySum/output.txt', 'w')

    ar_count = int(input("Enter the length of the array: ").strip())

    ar = list(map(int, input("Enter all the numbers of the array separated by spaces:\n").rstrip().split()))

    result = simpleArraySum(ar)

    print("Result is", result)
    fptr.write(str(result) + '\n')

    fptr.close()
