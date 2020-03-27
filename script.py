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

#order sets for table
dfs = [dc14, dc18, dc20, m14, m18, m20]

#create new dataframe for graphs

#iterate through list and calculate necessary values
for i in range(len(dfs)):
    names = ['dc14', 'dc18', 'dc20', 'm14', 'm18', 'm20']
    app = 0
    fem = 0
    prop = 0.0
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
        
    
    print('|{}|{}|{}|{}|{}|{}|'.format(names[i], cur[fem].shape[0]/cur.shape[0], cur[fem].shape[0], cur.shape[0]-cur[fem].shape[0], cur.shape[0],dfs[i].shape[0]))