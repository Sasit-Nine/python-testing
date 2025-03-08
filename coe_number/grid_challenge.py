#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):

    grid = [sorted(row) for row in grid]
    
    for i in range(len(grid[0])):  
        for j in range(1, len(grid)):  
            if grid[j][i] < grid[j-1][i]: 
                return "NO"
    
    return "YES"