#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises (Part 2)

# ## Full Data Workflow A-Z: Importing Data

# ### Exercise 10: Importing Data from messy csv-files

# Now, you will have the opportunity to analyze your own dataset. <br>
# __Follow the instructions__ and insert your code! You are either requested to 
# - Complete the Code and __Fill in the gaps__. Gaps are marked with "__---__" and are __placeholders__ for your code fragment. 
# - Write Code completely __on your own__ 

# In some exercises, you will find questions that can only be answered, if your code is correct and returns the right output! The correct answer is provided below your coding cell. There you can check whether your code is correct.

# If you need a hint, check the __Hints Section__ at the end of this Notebook. Exercises and Hints are numerated accordingly.

# If you need some further help or if you want to check your code, you can also check the __solutions notebook__.

# ### Have Fun!

# --------------------------------------------------------------------------------------------------------------

# ## Option 1: Self_guided

# __Import__ the cars Dataset from the messy csv-file __cars_raw.csv__ into a Pandas DataFrame. Use appropriate __parameters__ in the __pd.read_csv()__ method to bring the DataFrame into a clean format. __Columns__ should have the following __labels__:

# In[ ]:


labels = ['mpg',
 'cylinders',
 'displacement',
 'horsepower',
 'weight',
 'acceleration',
 'model year',
 'origin',
 'name']


# Finally, __save__ and __export__ the dataset as new csv-file (__cars_imp.csv__).

# --------------------------------

# ## Option 2: Guided and Instructed

# # STOP HERE, IF YOU WANT TO DO THE EXERCISE ON YOUR OWN!

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 77. __Import__ Pandas (pd)!

# In[ ]:


import pandas as pd


# 78. __Import__ the csv-file __cars_raw.csv__ with the appropriate pandas method and __inspect__ the data!

# In[ ]:


pd.read_csv("cars_raw.csv")


# Use appropriate __parameters__ in the __pd.read_csv()__ method to clean the format. The following issues need to be solved:

# 79. __Remove__ the __first row(s)__ containing nonsense content.

# 80. __Remove__ the __last row(s)__ containing nonsense content.

# 81. Define that there are __no appropriate column labels/headers__ in the data. 

# 82. __Set__ the following __column labels/headers__:

# In[ ]:


labels = ['mpg',
 'cylinders',
 'displacement',
 'horsepower',
 'weight',
 'acceleration',
 'model year',
 'origin',
 'name']


# In[ ]:


#complete the code and run the cell!
pd.read_csv("cars_raw.csv", skiprows= 2, skipfooter= 1, header = None, names = labels)


# 83. Once you are happy with the import, __save__ the DataFrame in the variable __cars__!

# In[ ]:


#complete the code and run the cell!
cars = pd.read_csv("cars_raw.csv", skiprows= 2, skipfooter= 1, header = None, names = labels)


# In[ ]:


# run the cell!
cars.head()


# In[ ]:


# run the cell!
cars.tail()


# 84. __Export__ and __save__ cars as new csv-file (__cars_imp.csv__). Do __not__ export any __RangeIndex__!

# In[ ]:


cars.to_csv("cars_imp.csv", index= False)


# __Reimport__ cars_imp.csv and check!

# In[ ]:


#run the cell!
pd.read_csv("cars_imp.csv")


# # Well Done!

# ----------------------------

# # Hints (Spoiler!)

# 77. at this point, you should know this ;-) !

# 78. pd.read_csv("filename")

# 79. parameter skiprows

# 80. parameter skipfooter

# 81. header = N---

# 82. parameter names

# 83. see hints 79-82

# 84. to_csv() method
