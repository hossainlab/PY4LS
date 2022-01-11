#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises (Part 2)

# ## Full Data Workflow A-Z: Cleaning Data

# ### Exercise 11: Cleaning messy Data

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

# __Import__ the cars dataset from the csv-file __cars_unclean.csv__ and inspect. Then, __clean up__ the dataset:
# 
# - Identify and handle __inconsistent data__
# - Each column/feature should have the __appropriate/most functional datatype__
# - Identify and handle __missing values__
# - Identify and handle __duplicates__
# - Have a closer look into columns with __strings__ and clean up
# - Identify and handle __erroneous outliers__ in numerical columns
# (hint: there might be a "fat finger" issue in one column and some value(s) in the mpg column could be in "gallons per mile" units)
# - __Save and export__ the cleaned dataset in a new csv-file (cars_clean.csv)
# - Change the datatype of appropriate columns to __categorical__.

# --------------------------

# ## Option 2: Guided and Instructed

# # STOP HERE, IF YOU WANT TO DO THE EXERCISE ON YOUR OWN!

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# In[ ]:


# run the cell!
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[ ]:


# run the cell!
cars = pd.read_csv("cars_unclean.csv")


# __Inspect__ the DataFrame and identify obviously __inconsistent data__!

# In[ ]:


# run the cell!
cars.head(20)


# In[ ]:


# run the cell!
cars.tail(10)


# In[ ]:


# run the cell! 
cars.info()


# 85. __Identify__ one __column label__ that should be changed and adjust/__rename__ the column label! __Fill in the gaps__!

# In[ ]:


cars.rename(columns = {"model year": "model_year"}, inplace = True)


# 86. Have a closer look to the __origin__ column by analyzing the __frequency/count__ of unique values! Can you find __any inconsistency__?

# In[ ]:


cars.origin.value_counts()


# There are the values ... usa and United States

# 87. __Replace__ the value __"United States"__ in the origin column! __Save__ the change!

# In[ ]:


cars.origin.replace("United States", "usa", inplace = True)


# Inspect and __identify__ the __problem__ in the column __horsepower__!

# In[ ]:


# run the cell!
cars.horsepower.head()


# Datatype should be ... numerical. But first of all, we need to remove...?

# 88. Apply the appropriate __string operation__ to __remove "hp"__ from the horsepower column! Pay attention to __whitespaces__! __Overwrite__ the horsepower column!

# In[ ]:


cars.horsepower = cars.horsepower.str.replace(" hp", "")


# In[ ]:


# run the cell and inspect!
cars.head()


# Run and inspect, anything __strange__?

# In[ ]:


#run the cell!
pd.options.display.min_rows = None


# In[ ]:


# run the cell!
cars.horsepower.value_counts()


# There are 6 entries with the value ... "Not available"

# 89. Create __"real" missing values__ in the column horsepower! __Save__ the change! __Fill in the gaps__!

# In[ ]:


cars.horsepower.replace("Not available", np.nan, inplace = True)


# 90. Now you can __convert the datatype__ in the column __horsepower__! __Overwrite__ the column!

# In[ ]:


cars.horsepower = cars.horsepower.astype("float")


# Inspect!

# In[ ]:


# run the cell!
cars.info()


# In[ ]:


# run the cell!
cars.head(7)


# Any __inconsistencies__ in the column __name__? Inspect one element! 

# In[ ]:


#run the cell!
cars.loc[4, "name"]


# It seems like some names are uppercase, while others are lowercase. And there are some excess whitespaces in the strings.

# 91. __Convert__ all names to __lowercase__ and __remove all whitespaces__ on the left ends and right ends!

# In[ ]:


cars.name = cars.name.str.lower().str.strip()


# Run the next two cells and identify (erroneous) outliers in the numercial columns!

# In[ ]:


# run the cell!
cars.describe()


# In[ ]:


# run the cell!
cars.plot(subplots = True, figsize = (15,12))
plt.show()


# 92. Inspect the column __model_year__ in more detail by analyzing the __frequency/counts__ of unique values! Anything __strange__?

# In[ ]:


cars.model_year.value_counts()


# There are 5 entries with ... 1973 instead of 73. 

# 93. __Replace__ the value __1973__! __Save__ the change!

# In[ ]:


cars.model_year.replace(1973, 73, inplace = True)


# 94. Inspect the column __weight__ by __sorting__ the values from __high to low__. Can you see the __extreme value__?

# In[ ]:


cars.weight.sort_values(ascending = False)


# The by far highest value is ... 23000 lbs. Must be an error!

# 95. __Select__ the complete __row__ of the outlier with the method __idxmax()__!

# In[ ]:


cars.loc[cars.weight.idxmax()]


# It´s an opel manta ... could be a "fat finger" problem, weight could be 2300 instead of 23000.
# 

# 96. __Overwrite__ the erroneous outlier! __Fill in the gaps__!

# In[ ]:


cars.loc[cars.weight.idxmax(), "weight"] = 2300


# Inspect the column __mpg__! Any strange __outlier__?

# In[ ]:


# run the cell!
cars.mpg.sort_values()


# An mpg of ... 0.060606 cannot be correct...

# 97. __Select__ the complete __row__ of the outlier with the method __idxmin()__!

# In[ ]:


cars.loc[cars.mpg.idxmin()]


# 98. After some research we have found out that this extreme value is in __"gallons per mile"__ units instead of "miles per gallon". <br>
# __Convert__ to __"miles per gallon"__ units! __Fill in the gaps__!

# In[ ]:


cars.loc[cars.mpg.idxmin(), "mpg"] = 1/cars.loc[cars.mpg.idxmin(), "mpg"]


# 99. Next, select all __rows__ with at least one __missing__/na value! __Fill in the gaps__!

# In[ ]:


cars.loc[cars.isna().any(axis = 1)]


# There are 6 cars, where the horsepower is unknown.

# 100. As horsepower is an important feature in the cars dataset, we decide to remove all 6 rows. __Remove__ and __save__ the change!

# In[ ]:


cars.dropna(inplace= True)


# Now let´s find __duplicates__. First, we need to understand __which columns__ we have to take into consideration to identify duplicates.

# 101. The first __naive assumption__ is that two cars cannot have the __same name__. Let´s count the number of __name-duplicates__. __Fill in the gaps__!

# In[ ]:


cars.duplicated(subset = ["name"]).sum()


# There are ... 86 potential duplicates to remove.

# 102. Let´s inspect the __duplicated pairs__ by selecting __all instances__ of a name duplicate! __Fill in the gaps__! <br>
# Should the __name__ be the __only criteria__ to identify duplicates?

# In[ ]:


cars.loc[cars.duplicated(subset = ["name"], keep = False)].sort_values("name")


# No! Cars can have several vintages/model_year and several variants with different technical specifications (e.g. weight, horsepower)  

# 103. To be on the safe side, let´s include __all columns__ to identify duplicates. __Count__ the number of duplicates! __Fill in the gaps__!

# In[ ]:


cars.duplicated().sum()


# There are ... 10 potential duplicates.

# 104. Let´s inspect the __duplicated pairs__ by selecting __all instances__ of a duplicate! __Fill in the gaps__!

# In[ ]:


cars.loc[cars.duplicated(keep = False)].sort_values("name")


# All pairs seem to be real duplicates.

# 105. __Drop one instance__ of each duplicated pair! __Save__ the change!

# In[ ]:


cars.drop_duplicates(inplace = True)


# In[ ]:


# run the cell
cars.head()


# In[ ]:


# run the cell!
cars.info()


# 106. Our dataset seems to be pretty clean now! __Save__ and __export__ to a new csv-file (cars_clean.csv)! Do not export the RangeIndex!

# In[ ]:


cars.to_csv("cars_clean.csv", index= False)


# Call the __describe()__ method on all __non-numerical columns__!

# In[ ]:


# run the cell!
cars.describe(include = "O")


# Are there any __categorical features__ (only few unique values) where the datatype could be __converted to "category"__? <br>
# 107. If so, __convert__ and __overwrite__ the column(s)!

# In[ ]:


cars.origin = cars.origin.astype("category")


# __Inspect__. Did we __reduce memory usage__?

# In[ ]:


#run the cell!
cars.info()


# Yes, we reduced memory usage!

# # Well Done!

# -----------------------------------------

# # Hints (Spoiler!)

# 85. rename() method, column "model year"

# 86. value_counts() method

# 87. replace() method

# 88. string(str) method replace(), " hp"

# 89. replace() method, np.nan

# 90. astype() method, "float"

# 91. string(str) methods lower() and strip()

# 92. value_counts() method

# 93. replace() method

# 94. sort_values() method

# 95. Filter cars with cars.weight.idxmax()

# 96. cars.weight.idxmax(), "weight"

# 97. Filter cars with cars.mpg.idxmin()

# 98. cars.mpg.idxmin(), "mpg", 1/x

# 99. methods isna() and any()

# 100. dropna() method

# 101. subset parameter, "name"

# 102. keep parameter

# 103. methods duplicated() and sum()

# 104. keep parameter

# 105. drop_duplicates() method

# 106. to_csv() method

# 107. astype() method
