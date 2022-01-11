#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises (Part 2)

# ## Full Data Workflow A-Z: Advanced Visualization with Seaborn

# ### Exercise 16: Seaborn

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

# 142. __Import__ the cars dataset and __drop__ any missing values (__cars.csv__)!

# 143. __Create__ the following plot!

# ![image.png](attachment:image.png)

# 144. __Create__ the following plot! Cars with the lowest __fuel efficiency__ come from...?

# ![image.png](attachment:image.png)

# 145. __Create__ the following plot! Do you think that the lower fuel efficiency of us cars is __statistically significant__? 

# ![image.png](attachment:image.png)

# 146. __Create__ the following plot! Do you think that manufacturers from __all three regions significantly increased fuel efficiency__ from 1970 till 1982?

# ![image.png](attachment:image.png)

# 147. Create __similar plots__ (as above) with __horsepower__, __weight__ and __displacement__ on the y-axis! <br> Can you identify __differences__ in the ways how manufacturers managed to __increase fuel efficiency__?

# 148. __Add__ a new column __"gpm"__ with fuel efficiency in gallons per 100 miles unit. __Drop__ the mpg column!

# 149. __Create__ the following plot! Is there a __significant__ (linear) __relationship__ between horsepower and gpm?

# ![image.png](attachment:image.png)

# 150. Also create the following plot!

# ![image.png](attachment:image.png)

# 151. __Create__ the following __heatmap__ (correlation matrix)!

# ![image.png](attachment:image.png)

# 152. __Drop__ the columns __displacement__ and __acceleration__ and create the following __pairplot__ (sns.pairplot) for cars (kind = scatter)! 

# ![image.png](attachment:image.png)

# 153. __Run__ the cell and __inspect__!

# In[ ]:


# run!
sns.set(font_scale=1.5)
sns.pairplot(data = cars[["gpm", "horsepower", "origin"]], kind = "scatter", hue = "origin", aspect =2, height = 3)
plt.show()


# -----------------

# ## Option 2: Guided and Instructed

# ### No further guidance this time! Prepare yourself for the final challenge! (Take a look at the Hints, if necessary)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 142. __Import__ the cars dataset and __drop__ any missing values (__cars.csv__)!

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


cars = pd.read_csv("cars.csv")


# In[ ]:


cars.head()


# In[ ]:


cars.tail()


# In[ ]:


cars.info()


# In[ ]:


cars.dropna(inplace= True)


# 143. __Create__ the following plot!

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5, palette="viridis")
sns.countplot(data = cars, hue = "origin", x = "model_year")
plt.show()


# 144. __Create__ the following plot! Cars with the lowest __fuel efficiency__ come from...?

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5, palette="viridis")
sns.violinplot(data = cars, x = "origin", y = "mpg", dodge = True)
sns.swarmplot(data = cars, x = "origin", y = "mpg", dodge = True, color = "black")
plt.show()


# Cars with the lowest __fuel efficiency__ come from... usa.

# 145. __Create__ the following plot! Do you think that the lower fuel efficiency of us cars is __statistically significant__? 

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.barplot(data = cars, x = "origin", y = "mpg", dodge = True)
plt.show()


# Yes, it seems to be statistically significant.

# 146. __Create__ the following plot! Do you think that manufacturers from __all three regions significantly increased fuel efficiency__ from 1970 till 1982?

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.pointplot(data = cars, x = "model_year", y = "mpg", hue = "origin", dodge = True, ci = 95)
plt.show()


# Yes, they all increased fuel efficiency significantly.

# 147. Create __similar plots__ (as above) with __horsepower__, __weight__ and __displacement__ on the y-axis! <br> Can you identify __differences__ in the ways how manufacturers managed to __increase fuel efficiency__?

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.pointplot(data = cars, x = "model_year", y = "horsepower", hue = "origin", dodge = True, ci = 95)
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.pointplot(data = cars, x = "model_year", y = "weight", hue = "origin", dodge = True, ci = 95)
plt.show()


# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.pointplot(data = cars, x = "model_year", y = "displacement", hue = "origin", dodge = True, ci = 95)
plt.show()


# It seems like manufacturers from the usa managed to increase fuel efficiency by reducing engine power (horsepower, displacement) and weight. Manufacturers from europe and japan were able to increase fuel efficiency without reducing engine power and weight. There might have been other solutions...

# 148. __Add__ a new column __"gpm"__ with fuel efficiency in gallons per 100 miles unit. __Drop__ the mpg column!

# In[ ]:


cars["gpm"] = (1/cars.mpg*100).round(2)


# In[ ]:


cars.drop(columns = "mpg", inplace= True)


# In[ ]:


cars.head()


# 149. __Create__ the following plot! Is there a __significant__ (linear) __relationship__ between horsepower and gpm?

# In[ ]:


sns.set(font_scale=1.5)
sns.jointplot(data = cars, x = "horsepower", y = "gpm", height = 8, kind = "reg")
plt.show()


# Yes, there seems to be a significant positive relationship. The higher the engine power, the higher the fuel consumption.

# 150. Also create the following plot!

# In[ ]:


sns.set(font_scale=1.5)
sns.lmplot(data = cars, x = "weight", y = "horsepower", col = "origin")
plt.show()


# 151. __Create__ the following __heatmap__ (correlation matrix)!

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.4)
sns.heatmap(cars.corr(), annot= True, cmap = "Reds")
plt.show()


# 152. __Drop__ the columns __displacement__ and __acceleration__ and create the following __pairplot__ (sns.pairplot) for cars (kind = scatter)! 

# In[ ]:


cars.drop(columns = ["displacement", "acceleration"], inplace = True)


# In[ ]:


cars.head()


# In[ ]:


sns.set(font_scale=1.5)
sns.pairplot(data = cars, kind = "scatter")
plt.show()


# 153. __Run__ the cell and __inspect__!

# In[ ]:


sns.set(font_scale=1.5)
sns.pairplot(data = cars[["gpm", "horsepower", "origin"]], kind = "scatter", hue = "origin", aspect =2, height = 3)
plt.show()


# ------------------------------

# # Hints (Spoiler!)

# 142. cars.dropna(inplace= True)

# 143. 

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5, palette="viridis")
sns.countplot(data = cars, hue = "origin", x = "model_year")
plt.show()


# 144. 

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5, palette="viridis")
sns.violinplot(data = cars, x = "origin", y = "mpg", dodge = True)
sns.swarmplot(data = cars, x = "origin", y = "mpg", dodge = True, color = "black")
plt.show()


# 145. 

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.barplot(data = cars, x = "origin", y = "mpg", dodge = True)
plt.show()


# 146. 

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.5)
sns.pointplot(data = cars, x = "model_year", y = "mpg", hue = "origin", dodge = True, ci = 95)
plt.show()


# 147. pass horsepower, weight & displacement to y!

# 148. 1 / mpg * 100

# 149.  

# In[ ]:


sns.set(font_scale=1.5)
sns.jointplot(data = cars, x = "horsepower", y = "gpm", height = 8, kind = "reg")
plt.show()


# 150. 

# In[ ]:


sns.set(font_scale=1.5)
sns.lmplot(data = cars, x = "weight", y = "horsepower", col = "origin")
plt.show()


# 151.

# In[ ]:


plt.figure(figsize=(12,8))
sns.set(font_scale=1.4)
sns.heatmap(cars.corr(), annot= True, cmap = "Reds")
plt.show()


# 152. 

# In[ ]:


sns.set(font_scale=1.5)
sns.pairplot(data = cars, kind = "scatter")
plt.show()


# 153. Nothing to do!
