#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises (Part 2)

# ## Full Data Workflow A-Z: Data Preparation and Feature Creation

# ### Exercise 15: Data Preparation and Feature Creation

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

# 132. Import and inspect the cars dataset (cars.csv)!

# 133. __Transform__ the format in the model_year column to __full year format__ (e.g. 1970 instead of 70)!

# 134. __Transform__ the __mpg__ column in way that the ralationship with the horsepower feature is __linear__/closer to linear!<br> __Visualize__ before and after!<br> <br>
# (Hint: Gallons per 100 miles might be a good format) 

# 135. Create a __new column__ with the __manufacturer__ name!

# 136. Add a __new column__ with the respective __continent__ (north america, asia, europe)!

# 137. __Visualize__ and inspect whether there are any __extreme values__ / outliers in the __numerical columns__ that are worth to be __capped__ / __floored__!

# 138. __Bin / discretize__ the __weight__ column! The __25%__ of cars with the __lowest weight__ shall get the label __"light"__, the __25%__ of cars with the __highest weight__ shall get the label __"heavy"__ and the remaining __50%__ the label __"medium"__! Create a new column __"weight_cat"__!

# 139. __Drop__ the columns "cylinders", "displacement", "weight", "acceleration", "name", "mpg"!

# 140. Bring the columns __horsepower__ and the column that you created in __question 133__ (transformed mpg column) to the same __scale__ by calculating __z-scores__! __Visualize__ before and after!

# 141. __Transform__ the columns __model_year__ and __origin__ into (k-1) columns with __dummy variables__!

# -----------------------------------------------------------------------------

# ## Option 2: Guided and Instructed

# ### No further guidance this time! Prepare yourself for the final challenge! (Take a look at the Hints, if necessary)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 132. Import and inspect the cars dataset (cars.csv)!

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use("seaborn")


# In[ ]:


cars = pd.read_csv("cars.csv")


# In[ ]:


cars.head()


# In[ ]:


cars.tail()


# In[ ]:


cars.info()


# 133. __Transform__ the format in the model_year column to __full year format__ (e.g. 1970 instead of 70)!

# In[ ]:


cars.model_year = cars.model_year.add(1900)


# In[ ]:


cars.model_year.value_counts()


# 134. __Transform__ the __mpg__ column in way that the relationship with the horsepower feature is __linear__/closer to linear!<br> __Visualize__ before and after!<br> <br>
# (Hint: Gallons per 100 miles might be a good format) 

# In[ ]:


cars.plot(kind = "scatter", x = "horsepower", y = "mpg", figsize= (12, 8), fontsize= 13)
plt.show()


# In[ ]:


cars["gpm"] = (1/cars.mpg*100).round(2)


# In[ ]:


cars.head()


# In[ ]:


cars.plot(kind = "scatter", x = "horsepower", y = "gpm" , figsize= (12, 8), fontsize= 13)
plt.show()


# 135. Create a __new column__ with the __manufacturer__ name!

# In[ ]:


cars["manufacturer"] = cars.name.str.split(" ", n = 1, expand = True)[0]


# In[ ]:


cars.head()


# In[ ]:


cars.manufacturer.value_counts()


# 136. Add a __new column__ with the respective __continent__ (north america, asia, europe)!

# In[ ]:


mapper = {"usa":"north america", "europe":"europe", "japan":"asia"}


# In[ ]:


cars["continent"] = cars.origin.map(mapper)


# In[ ]:


cars.head()


# 137. __Visualize__ and inspect whether there are any __extreme values__ / outliers in the __numerical columns__ that are worth to be __capped__ / __floored__!

# In[ ]:


cars.plot(figsize = (15,15), subplots = True)
plt.show()


# 138. __Bin / discretize__ the __weight__ column! The __25%__ of cars with the __lowest weight__ shall get the label __"light"__, the __25%__ of cars with the __highest weight__ shall get the label __"heavy"__ and the remaining __50%__ the label __"medium"__! Create a new column __"weight_cat"__!

# In[ ]:


cars.weight.plot(kind = "hist")
plt.show()


# In[ ]:


labels = ["light", "medium", "heavy"]


# In[ ]:


pd.qcut(cars.weight, q = [0, 0.25, 0.75,1], labels = labels).value_counts()


# In[ ]:


cars["weight_cat"] = pd.qcut(cars.weight, q = [0, 0.25, 0.75,1], labels = labels)


# 139. __Drop__ the columns "cylinders", "displacement", "weight", "acceleration", "name", "mpg"!

# In[ ]:


cars.drop(columns = ["cylinders", "displacement", "weight", "acceleration", "name", "manufacturer", "mpg"], inplace = True)


# In[ ]:


cars.head()


# 140. Bring the columns __horsepower__ and the column that you created in __question 133__ (transformed mpg column) to the same __scale__ by calculating __z-scores__! __Visualize__ before and after!

# In[ ]:


cars.loc[:, ["horsepower", "gpm"]].plot(figsize = (12,8))
plt.show()


# In[ ]:


cars["gpm_z"] = round((cars.gpm-cars.gpm.mean()) / cars.gpm.std(),2)
cars["horsepower_z"] = round((cars.horsepower-cars.horsepower.mean()) / cars.horsepower.std(),2)


# In[ ]:


cars.head()


# In[ ]:


cars.loc[:, ["horsepower_z", "gpm_z"]].plot(figsize = (12,8))
plt.show()


# 141. __Transform__ the columns __model_year__ and __origin__ into (k-1) columns with __dummy variables__!

# In[ ]:


cars.head()


# In[ ]:


cars = pd.get_dummies(cars, columns = ["model_year", "origin"], drop_first = True)


# In[ ]:


cars.head()


# In[ ]:


cars.info()


# ----------------------------

# ## Hints (Spoiler!)

# 132. At this point, you should know this!

# 133. Use the add() method.

# 134. 1/mpg * 100

# 135. string method split()

# 136. Pass a mapper/dictionary to the map() method

# 137. Lineplot for all columns. Hint: Nothing to cap / floor

# 138. pd.qcut()

# 139. drop() method

# 140. z-score for all elements in horsepower column: z-score = (cars.horsepower - cars.horsepower.mean()) / cars.horsepower.std()

# 141. pd.get_dummies(); drop_first = True
