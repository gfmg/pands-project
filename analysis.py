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
import seaborn as sns
import matplotlib.pyplot as plt

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

# Making the data check plots
for c in range(dat.shape[1]):
   if not dat.columns[c] == "class": #Dont make figures for class column
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))  # Create a figure with two subplots
    plt.suptitle(f"Data visualization for {dat.columns[c]}")
    #ax[0].set_title("Histogram")
    #ax[1].set_title("Boxplot")
    sns.histplot(data=dat, x=dat.columns[c], hue="class", element="poly", ax=ax[0])
    sns.boxplot(data=dat, y=dat.columns[c], x="class", hue="class", ax=ax[1])
   
    plt.savefig(os.path.join(dirs[2],f"Data checks_{dat.columns[c]}.png")) 
    plt.close()  


#Scatter plots of each pair
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

cols = dat.columns[0:4]

for i in range(len(dat.columns[0:4])):
    for j in range(i + 1, len(dat.columns[0:4])):
        sns.scatterplot(data=dat, x=dat.columns[i], y=dat.columns[j],hue="class", ax=axs[i, j - 1])
        axs[i, i + j - 1].set_title(f"{dat.columns[i]} vs {dat.columns[j]}")

plt.tight_layout()
plt.show()