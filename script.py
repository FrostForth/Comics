# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:17:30 2020

@author: Kaitlin

Design

1. Import libraries
    1. OS
    2. pandas
2. Import datasets
3. Output table
    1. group
    2. proportion female in sample
    3. number female in sample
    4. number not female in sample
    5. total >5 appearances (= sample size n)
    6. population size N
4. Output and save graphs
    1. Frequency bargraph
    2. Percentage bargraph
    3. Scatterplot (date vs. freq. fem.)
"""

import os
import pandas as pd

#set working path
data_path = os.path.join(os.getcwd(), 'data')

#import datasets
dc14 = pd.read_csv(os.path.join(data_path, 'dc-wikia-data.csv'))
m14 = pd.read_csv(os.path.join(data_path, 'marvel-wikia-data.csv'))
dc18 = pd.read_csv(os.path.join(data_path, 'dcprofileresult.csv'))
m18 = pd.read_csv(os.path.join(data_path, 'mprofileresult.csv'))
dc20 = pd.read_csv(os.getcwd()+'\dc2020.csv')
m20 = pd.read_csv(os.getcwd()+'\m2020.csv')

#Table header
print('| | Prop | Num. Fem. | Num. Not | Total >5| Total|\n|-----|-----|-----|-----|-----|-----|')

#Create arrays for table and dataframes
dfs = [dc14, dc18, dc20, m14, m18, m20]
names = ['dc14', 'dc18', 'dc20', 'm14', 'm18', 'm20']
pfem = []
pnot = []
numf = []
numn = []

#iterate through list and calculate necessary values
for i in range(len(dfs)):
    app = 0
    fem = 0
    tot = dfs[i].shape[0]
    
    if 'APPEARANCES' in dfs[i]:
        app = dfs[i]['APPEARANCES'] >= 5
    elif 'Appearances' in dfs[i]:
        app = dfs[i]['Appearances'] >= 5
    
    cur = dfs[i][app]
    
    if 'SEX' in cur:
        fem = cur['SEX'] == 'Female Characters'
    if 'Sex' in cur:
        fem = cur['Sex'] == 'Female'
        
    numf.append(cur[fem].shape[0])
    numn.append(cur.shape[0]-numf[i])
    pfem.append(numf[i]/cur.shape[0])
    pnot.append(1-pfem[i])
    
    print('|{}|{}|{}|{}|{}|{}|'.format(names[i], pfem[i], numf[i], numn[i],
          cur.shape[0],dfs[i].shape[0]))
    
# Frequency Bargraph
freq = list(zip(numf,numn))
barf = pd.DataFrame(freq, columns = ['Num. Fem.', 'Num. Not'], index = names).plot.bar()
barf.figure.savefig(os.getcwd()+'\images\{}reqbar.png'.format('f'))

# Percentage Bargraph
per = list(zip(pfem,pnot))
barp = pd.DataFrame(per, columns = ['Prop. Fem.', 'Prop. Not'], index = names).plot.bar(stacked=True)
barp.figure.savefig(os.getcwd()+'\images\percentbar.png')

# Wicked Epic Scatterplot
num = {'DC': numf[0:3], 'Marvel': numf[3:]}
scat = pd.DataFrame(num, index = [pd.Timestamp('2014-10-13'),
                                     pd.Timestamp('2018-12-27'),
                                     pd.Timestamp('2020-03-26')]).plot()
scat.figure.savefig(os.getcwd()+'\images\scatter.png')