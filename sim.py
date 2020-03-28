# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:07:35 2020

@author: Kaitlin

1. Import libraries
    1. OS
    2. numpy
    3. seaborn
    4. pandas
    5. scipy
2. Set variables
    1. n = 1000
    2. x = 23.513
3. Perform simulation and create graph
    1. Generate n random numbers in chi-squared dist.
    2. Plot the numbers with chi-squared overlay
4. Test x
    1. Create vertical line
    2. Calculate number of observations >= x
    3. Display results on graph
5. Save graph
"""

import os
import numpy as np
import seaborn as sns
import pandas as pd

n = 1000
s = np.random.chisquare(5,n)
s = pd.Series(s, name="Chi-Square")

from scipy.stats import chi2
ax = sns.distplot(s, fit=chi2, kde=False)

# Create x
x =  23.513
ax.axvline(x, 0,.5)

# calculate number observations above x

y = len(s[s >= x])
print(y)

ax.text(15, .13,'{}/{} observations\n>= {}'.format(y,n,x), fontsize=10)

ax.figure.savefig(os.getcwd()+'\images\sim.png')