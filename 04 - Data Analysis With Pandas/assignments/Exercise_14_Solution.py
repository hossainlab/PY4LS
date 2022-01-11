#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises (Part 2)

# ## Full Data Workflow A-Z: Reshaping and Pivoting

# ### Exercise 14: Reshaping and Pivoting DataFrames

# Now, you will have the opportunity to analyze your own dataset. <br>
# __Follow the instructions__ and insert your code! You are either requested to 
# - Complete the Code and __Fill in the gaps__. Gaps are marked with "__---__" and are __placeholders__ for your code fragment. 
# - Write Code completely __on your own__ 

# In some exercises, you will find questions that can only be answered, if your code is correct and returns the right output! The correct answer is provided below your coding cell. There you can check whether your code is correct.

# If you need a hint, check the __Hints Section__ at the end of this Notebook. Exercises and Hints are numerated accordingly.

# If you need some further help or if you want to check your code, you can also check the __solutions notebook__.

# ### Have Fun!

# --------------------------------------------------------------------------------------------------------------

# In[ ]:


#run the cell
import pandas as pd


# In[ ]:


#run the cell
cars = pd.read_csv("cars.csv")


# In[ ]:


#run the cell
cars.head()


# In[ ]:


#run the cell
cars.tail()


# In[ ]:


#run the cell
cars.info()


# 127. Calculate the __mean mpg__ for all combinations of __model_year__ and __origin__! __Save__ the resulting DataFrame in the variable __mpg_year_origin__! <br>__Fill in the gaps__!

# In[ ]:


mpg_year_origin = cars.groupby(["model_year", "origin"]).mpg.mean().unstack().round(2)
mpg_year_origin


# 128. __Transpose__ mpg_year_origin!

# In[ ]:


mpg_year_origin.T


# Import the __mean_mpg.csv__ file, save in the variable __mean_mpg__ and inspect!

# In[ ]:


# run the cell
mean_mpg = pd.read_csv("mean_mpg.csv")
mean_mpg


# 129. __Pivot__ mean_mpg! Resulting wide-format DataFrame shall have three columns __europe__, __japan__ and __usa__. __model_year__ shall be the __index__!<br>
# __Save__ new DataFrame in the variable __pivot__!

# In[ ]:


pivot = mean_mpg.pivot(index = "model_year", columns = "origin", values = "mpg")


# In[ ]:


#run the cell!
pivot.head()


# Reset the index!

# In[ ]:


# run the cell!
pivot.reset_index(inplace= True)


# In[ ]:


# run the cell!
pivot.head()


# 130. __Melt__ the DataFrame __pivot__ from wide format __back to long format__! __Fill in the gaps!__

# In[ ]:


pivot.melt(id_vars= "model_year", value_vars= ["europe", "japan", "usa"], var_name = "origin", value_name = "mpg")


# 131. Return the __number of cars__ for each __combination of model_year and origin__ with __pd.crosstab()__ (e.g. 5 cars from europe in 1970)! <br>
# __How many__ cars from __usa__ are built in __1972__?

# In[ ]:


pd.crosstab(cars.model_year, cars.origin)


# ... 18 Cars from usa are built in 1972.

# # Well Done!

# -----------------------------------------------------

# # Hints (Spoiler!)

# 127. mpg, mean() method

# 128. T attribute / transpose() method

# 129. pivot() method

# 130. check the parameters of melt() with SHIFT + TAB

# 131. cars.model_year, cars.origin
