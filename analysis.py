#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
@File    :   analysis.py
@Time    :   2024/05/08 23:04:23
@Author  :   Guillermo Martin
@Version :   1.0
@Personal email : gfmg1992@hotmail.com
@Student email: G00438885@atu.ie
@License :   (C)Copyright 2023, Guillermo Martin
@Desc    :   Guillermo Martin projects for the 2024 Programming and Scripting course
'''
 
 # Libraries
import os
import pandas as pd

#Creating directories for outputs: 
dirs = ['./outputs','./outputs/summary','./outputs/figures']

for d in dirs:
 if not os.path.exists(d):
    os.makedirs(d)

# Importing the Iris dataset: 
# Source: https://archive.ics.uci.edu/dataset/53/iris 
# Downloaded: 08/05/2024

# Data:
# Column names from the iris.names file Attributes section
dat = pd.read_csv('./data/iris.data',
                  names=['sepal_length','sepal_width','petal_length','petal_width','class'])

# Importing data directly from the website (https://github.com/uci-ml-repo/ucimlrepo):
# from ucimlrepo import fetch_ucirepo
#dat = fetch_ucirepo(name='Iris') # Importing Iris dataset and call it dat. 


# Brief summary of the data for each column saved into a single .txt file
for c in dat.columns: #Iterate over every column
    file_name = f"{c}_summary.txt" # Define file name to be saved as ("columnName_summary.txt")
    with open(os.path.join(dirs[1],file_name), 'w') as f: #Write each filename. dirs[1] is the directory of the summaries
        f.write(f"Summary for column '{c}':\n") # Title of the file
        f.write(f"{dat[c].describe()}\n") #dat. describe (brief description of each colum (e.g count, mean, std...))