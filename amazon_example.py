#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'searchSuggestions' function below.
#
# The function is expected to return a 2D_STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY repository
#  2. STRING customerQuery
#

def searchSuggestions(repository, customerQuery):
    repository = sorted(repository)
    responses = []
    for i in range(2,len(customerQuery)+1):
        responses.append([k for k in repository if customerQuery[:i] == k[:i]][:3])
    return responses

if __name__ == '__main__':