#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises (Part 2)

# ## Full Data Workflow A-Z: Group Operations

# ### Exercise 13: GroupBy

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

# Import the cars dataset (cars.csv).

# __Calculate__ the mean/average mpg __by origin__ (mean mpg for usa, for europe and for japan)! Who built the __least__ fuel efficient cars?

# __Calculate__ the mean/average mpg __by model_year__ (mean mpg for the years 70, 71, ...). Can you see a __trend__? __Visualize__!

# __Calculate__ the mean/average mpg for each __combination of model_year & origin__ and __visualize__ how the mean mpg evolved over time for usa, europe and japan. <br>
# Can you see the __same trend__ for all three orgins?

# Calculate the __mean__, __min__ and __max__ mpg for each combination of model_year & origin!

# Return the columns __name__ and __mpg__ for the __two most fuel efficient cars__ for __each combination of model_year & origin__! <br>(hint: a __user defined function__ might help!)

# Calculate the __mean mpg__ for each combination of __model_year & origin__ and __assign__ the corresponding __group-specific value__ to all cars (__new column__!).<br>
# Then, __filter__ all cars, where the __absolute difference__ between __mpg__ and __group-specific mpg__ is __greater than 10__. These cars are outliers/special cases in their respective group.

# ------------------------

# ## Option 2: Guided and Instructed

# # STOP HERE, IF YOU WANT TO DO THE EXERCISE ON YOUR OWN!

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# In[ ]:


#run the cell
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")


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


# 117. __Group__ cars by the column __origin__ and __calculate__ the __mean__/average __mpg__ for each origin (mean mpg for usa, for europe and for japan)! <br>
# Who built the __least__ fuel efficient cars?

# In[ ]:


cars.groupby("origin").mpg.mean()


# The least fuel efficient cars are from ... usa.

# 118. __Group__ cars by the column __model_year__ and __calculate__ the __mean__/average __mpg__ for each model_year (mean mpg for 70, 71, 72,...)! <br>__Save__ the result in the variable __mpg_by_year__ and __round__ to two decimals!

# In[ ]:


mpg_by_year = cars.groupby("model_year").mpg.mean().round(2)


# In[ ]:


# run the cell
mpg_by_year


# __Inspect__! Can you see a __trend__?

# In[ ]:


# run the cell!
mpg_by_year.plot()
plt.show()


# The cars are getting ... more fuel efficient over time.

# 119. __Group__ cars by the columns __model_year and origin__ and return the __mean mpg__ for each group! <br> __Save__ the resulting DataFrame in the variable __mpg_year_origin__!
# __Column labels__ of mpg_year_origin shall be __europe__, __japan__ & __usa__. __Fill in the gaps__! 

# In[ ]:


mpg_year_origin = cars.groupby(["model_year", "origin"]).mpg.mean().unstack().round(2)


# In[ ]:


# run the cell
mpg_year_origin


# __Inspect__! Do we have the __same trend__ for europe, japan and usa?

# In[ ]:


# run the cell
mpg_year_origin.plot()
plt.show()


# It seems that manufacturer from europe, japan and usa were able to improve efficiency!

# 120. __Group__ cars by __model_year and origin__ and return __mean__, __max__ and __min mpg__ for all groups! __Fill in the gaps!__

# In[ ]:


cars.groupby(["model_year", "origin"]).mpg.agg(["mean", "min", "max"]).unstack().round(2)


# Next, return the columns __name__ and __mpg__ for the __two most fuel efficient cars__ for __each combination of model_year & origin__!

# 121. First, __create__ the __user defined function__ get_most_efficient! __Fill in the gaps!__ 

# In[ ]:


def get_most_efficient(group):
    return group.nlargest(n =2, columns = "mpg").loc[:, ["name", "mpg"]]


# 122. __Apply__ get_most_efficient on the appropriate __groupby object__! __Save__ the resulting DataFrame in the variable __most_eff__. __Fill in the gaps!__

# In[ ]:


most_eff = cars.groupby(["model_year", "origin"]).apply(get_most_efficient)


# Tidy up and __Inspect__!

# In[ ]:


# run the cell
most_eff = most_eff.droplevel(-1)


# In[ ]:


# run the cell
most_eff.head(10)


# 123. __Select__ the 2 most efficient cars from __japan__ in __1980__! __Fill in the gaps!__ The __most efficient__ car is...?

# In[ ]:


most_eff.loc[(80, "japan")]


# The most efficient car is... the mazda glc.

# Calculate the __mean mpg__ for each combination of __model_year & origin__ and __assign__ the corresponding __group-specific value__ to all cars (__new column__!). Then, __filter__ all cars where the __absolute difference__ between __mpg__ and __group-specific mpg__ is __greater than 10__. These cars all outliers/special cases in their respective group.

# 124. First, __group__ cars by __model_year & origin__ and calculate the __mean mpg__ for each group via the --- method to create the new column __"group_mpg"__. <br>
# __Fill in the gaps!__

# In[ ]:


cars["group_mpg"] = cars.groupby(["model_year", "origin"]).mpg.transform("mean").round(2)


# __Inspect!__ The group-specific mpg for the vw pickup is ... ?

# In[ ]:


# run the cell
cars.head()


# In[ ]:


# run the cell
cars.tail()


# The group-specific mpg for the vw pickup is... 40.0!

# 125. __Create__ the column __"mpg_outlier"__ by __substracting__ the __group_mpg__ column from the __mpg__ column. __Round__ to 2 decimals! 

# In[ ]:


cars["mpg_outlier"] = (cars.mpg-cars.group_mpg).round(2)


# In[ ]:


# run the cell
cars.mpg_outlier.describe()


# 126. __Filter__ cars for all cars/rows, where the __absolute value__ in the __mpg_outlier__ column is __greater than 10__! __Fill in the gaps!__<br>
# There is only one car, that is __significantly less fuel efficient__ than it´s peer group. Which one?

# In[ ]:


cars.loc[cars.mpg_outlier.abs() > 10]


# The... mazda rx-7 gs is significantly less fuel efficient than it´s peer group (negative value in mpg_outlier column).

# # Well Done!

# -------------------

# # Hints (Spolier!)

# 117. cars.groupby("---").---.mean()

# 118. mpg_by_year = cars.groupby("---").---.---.round(2)

# 119. Don´t forget unstack() method!
# 

# 120. agg() method, unstack() method

# 121. nlargest() method; 

# 122. group cars by model_year & origin; pass get_most_efficient to the apply() method

# 123. outer index level: 80; inner index level: "japan"

# 124. transform() method

# 125. (_pandas series_ - _pandas series_).round()

# 126. abs() method

# In[ ]:




