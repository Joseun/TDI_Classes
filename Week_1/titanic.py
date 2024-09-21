#!/usr/bin/env python
# coding: utf-8

# Certainly! Here’s an expanded list of relevant SWE concepts for this project:
# 
# - **VSCode**: Code editor for writing and debugging Python scripts locally.
# - **Google Colab**: Cloud-based environment for running Python code without local setup.
# - **Jupyter Notebooks**: Interactive notebooks for writing and executing Python code in chunks.
# - **GitHub**: Repository for version control, collaboration, and storing the project files.
# - **Git**: Tool for version control and managing code revisions (commits, branches, merges).
# - **Libraries**: External Python modules like Pandas, NumPy, Matplotlib, and Seaborn for data manipulation, computation, and visualization.
# - **Functions**: Blocks of reusable code for tasks like data preprocessing, cleaning, or analysis.
# - **Terminal**: Command-line interface for executing scripts, installing libraries (via pip), and using Git commands.
# - **Kernel**: Computational engine in Jupyter or Colab notebooks that runs code blocks and displays output.
# - **Error messages**: System-provided diagnostics when code fails, aiding debugging and problem-solving.
# - **DataFrames**: 2D data structure used in Pandas to store and manipulate tabular data.
# - **Type Checking**: Ensuring correct data types for columns in your dataset (like converting to categorical or numeric types).
# - **Data Validation**: Process of checking data quality and integrity (handling missing or duplicate values).
# - **Pip**: Python package manager for installing libraries.
# - **Virtual Environments**: Isolated Python environments to manage project dependencies without conflicts.
# - **Version Control**: Managing changes to the codebase with Git (committing, branching, pulling, merging).
# - **Data Preprocessing**: Cleaning and preparing raw data for analysis (handling missing data, normalizing values).
# - **Binning**: Grouping continuous data into discrete intervals (e.g., creating age groups for survival analysis).
# - **Visualization**: Creating plots (like bar charts, scatter plots) to represent data using libraries like Matplotlib and Seaborn.
# - **Loops & Conditionals**: Basic control structures for iterating over data and making decisions in code.
# - **Data Wrangling**: Transforming and mapping raw data into a format more suitable for analysis.
# - **CSV Handling**: Reading from and writing to CSV files using Pandas.
# - **Project Structure**: Organizing code, data, and results in a logical folder and file structure.
# - **Unit Testing**: Writing small tests to ensure that individual code components (e.g., functions) work as expected.
# - **Documentation**: Writing clear comments and markdown cells in Jupyter Notebooks to explain code logic.
# - **Collaboration Tools**: Using GitHub for team collaboration, pull requests, and code reviews.
# - **IDE Shortcuts**: Navigating efficiently within VSCode or Colab using keyboard shortcuts and extensions.
# 
# 

# In[3]:


# %pip install pandas
get_ipython().run_line_magic('pip', 'install seaborn')


# In[4]:


import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib.ticker import StrMethodFormatter


# Special character
# 
# \ $ ?

# In[71]:


data = pd.read_csv("./tested.csv")
print(data.head(5))
data.tail(4)


# In[76]:


data.info()
# data.isnull().sum()


# In[75]:


327+86+1


# In[ ]:


data.bfill
data.ffill
data.fillna()


# In[39]:


data.duplicated().value_counts()
data.drop_duplicates


# In[42]:


data.describe(include='all')


# In[48]:


data.groupby(['Pclass', 'Sex'])[['Embarked', 'Survived',]].value_counts()


# In[51]:


data.groupby('Survived')['Age'].count()


# In[57]:


type(True)


# In[53]:


data.Sex.value_counts()


# In[69]:


age_bins = [0, 18, 40, 60, 100]  # Age intervals (0-18, 18-40, 40-60, 60+)
age_labels = ['<18', '18-40', '40-60', '60+']

# Create a new column 'AgeGroup' by binning the 'Age' column
data['AgeGroup'] = pd.cut(data['Age'], bins=age_bins, labels=age_labels, right=False)

# Calculate the survival rate for each age group
age_group_survival = data.groupby('AgeGroup')['Survived'].mean()

# Display the survival rates for each age group
age_group_survival


# In[70]:


# Group by 'Pclass' and 'Sex' and calculate the mean survival rate for each group
gender_class_survival = data.groupby(['Pclass', 'Sex'])['Survived'].mean()

# Display the survival rates for each gender and class combination
gender_class_survival

