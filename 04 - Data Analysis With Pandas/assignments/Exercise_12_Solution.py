#!/usr/bin/env python
# coding: utf-8

# # Coding Exercises (Part 1)

# ## Full Data Workflow A-Z: Merging, Joining, Concatenating

# ### Exercise 12: Merging, joining, aligning and concatenating Data 

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

# ### Concatenating DataFrames vertically

# __Import__ the cars dataset (with cars from usa and europe) from the csv-file __cars_clean.csv__. <br>
# Also __import__ the csv-file __cars_jap.csv__ (with cars from japan) and __concatenate__ both DataFrames __vertically__! <br>
# __Save__ the __concatenated DataFrame__ in the variable __cars_all__! <br>
# Finally, __sort__ cars_all by the model_year from __low to high__!

# ### Left Join

# __Import__ the csv-files __summer.csv__ (as summer) and __dictionary.csv__ (as dic) which contains the __full country name__ for the olympic country codes as well as __population__ and __gdp__ statistics for some countries.<br>
# 
# __"Copy and paste"__ the __full country name__, __population__ and __gdp__ from the dic DataFrame __into the summer DataFrame__ with a __Left Join__!<br>
# __Save__ the new merged DataFrame in the variable __summer_new__!<br>
# 
# __Inspect__ summer_new and determine the __olympic country codes__ for which the dic DataFrame does __not provide__ any information!

# ### Arithmetic operations between DataFrames / Alignment

# __Import__ the csv-files __ath_2008.csv__ and __ath_2012.csv__ with all medals winners in the Sport __Athletics__ in the Editions __2008__ and __2012__.

# For __all Athletes__ in the two DataFrames, __aggregate/add__ the total number of __Gold__, __Silver__ and __Bronze__ Medals over both editions! __Save__ the aggregated DataFrame in the variable __add__. (Hint: add should contain an index with the Athlete names and three columns, Gold, Silver, Bronze)

# __Sort__ add by Gold, Silver, Bronze from __high to low__! Change datatype to __integer__, if necessary! The first Athlete in your DataFrame should be ... no surprise ... Usain Bolt with 6 Gold and 0 Silver and Bronze Medals.

# -------------------------------------

# ## Option 2: Guided and Instructed

# # STOP HERE, IF YOU WANT TO DO THE EXERCISE ON YOUR OWN!

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# In[ ]:


#run the cell
import pandas as pd


# ### Concatenating DataFrames vertically

# In[ ]:


#run the cell
cars = pd.read_csv("cars_clean.csv")


# __Inspect__ the __cars__ DataFrame!

# In[ ]:


#run the cell
cars.head()


# In[ ]:


#run the cell
cars.tail()


# In[ ]:


#run the cell
cars.info()


# __Inspect__ the cars_jap DataFrame!

# In[ ]:


#run the cell
cars_jap = pd.read_csv("cars_jap.csv")


# In[ ]:


#run the cell
cars_jap.head()


# Before we can concatenate both DataFrames, we need to __align__ them!<br>
# 108. __Insert__ the column __origin__ to __cars_jap__ at the most appropriate position! __Fill in the gaps!__

# In[ ]:


cars_jap.insert(7, "origin", "japan")


# Also the column labels should match. <br>
# 109. __Overwrite__ the column labels in __cars_jap__ and use the same column labels that we have in cars!

# In[ ]:


cars_jap.columns = cars.columns


# __Inspect__!

# In[ ]:


#run the cell
cars_jap.head()


# 110. __Concatenate__ both DataFrames __vertically__ and create a __new RangeIndex__! __Save__ the new DataFrame in the variable __cars_all__!

# In[ ]:


cars_all = pd.concat([cars, cars_jap], ignore_index= True)


# __Inspect__!

# In[ ]:


#run the cell
cars_all.head()


# In[ ]:


#run the cell!
cars_all.tail()


# 111. __Sort cars_call__ by the __model_year__ from __low to high__! Create a __new RangeIndex__ (drop the old)! __Fill in the gaps__!

# In[ ]:


cars_all = cars_all.sort_values("model_year").reset_index(drop = True)


# __Inspect__!

# In[ ]:


#run the cell
cars_all.head()


# In[ ]:


#run the cell
cars_all.tail()


# In[ ]:


#run the cell
cars_all.info()


# ----------------------------------------------------------------------

# ### Left Join

# In[ ]:


# run the cell!
summer = pd.read_csv("summer.csv")


# __Inspect__ the __summer__ DataFrame!

# In[ ]:


# run the cell!
summer.head()


# In[ ]:


# run the cell!
dic = pd.read_csv("dictionary.csv")


# __Inspect__ dict!

# In[ ]:


# run the cell!
dic.head()


# __dic__ contains the Olympic Games __Country Codes__ ("Code") with the corresponding __full country names__ ("Country") as well as recent __Population__ and __GDP__ statistics.<br>

# 112. __Create__ the columns __Country__, __Population__ and __GDP per Capita__ in the __summer__ DataFrame by using a __Left Join__ with __pd.merge()__. <br>
# __Save__ the merged Dataframe in the variable __summer_new__! __Fill in the gaps__!

# In[ ]:


summer_new = pd.merge(summer, dic, how = "left", left_on= "Country", right_on = "Code")


# __Inspect__ summer_new!

# In[ ]:


# run the cell!
summer_new.head()


# In[ ]:


# run the cell!
summer_new.info()


# Apparently, __dic__ does __not contain__ additional information for __all olympic country codes__ that are in the __summer__ Dataframe.

# 113. __Filter__ summer_new for the elements in the column __Country_x__, where the __corresponding value__ in the column __Code__ is __missing__! <br>
# __Count__ the frequency! __Fill in the gaps__!

# In[ ]:


summer_new.loc[summer_new.Code.isnull(), "Country_x"].value_counts()


# For these country codes, we need to find __other sources__ for additional information on the __full country name__, __population__ and __gdp__ (most of these countries do not exist any more.) -> BONUS EXERCISE ;-)

# --------------------------

# ### Arithmetic operations between DataFrames / Alignment

# In[ ]:


#run the cell
ath_2008 = pd.read_csv("ath_2008.csv")
ath_2012 = pd.read_csv("ath_2012.csv")


# __Inspect__ the __ath_2008__ DataFrame. It contains all athletes who won medals in __Athletics__ in the Edition __2008__.

# In[ ]:


#run the cell
ath_2008.head()


# In[ ]:


#run the cell
ath_2008.info()


# __Inspect__ the __ath_2012__ DataFrame. It contains all athletes who won medals in __Athletics__ in the Edition __2012__.

# In[ ]:


#run the cell
ath_2012.head()


# In[ ]:


#run the cell
ath_2012.info()


# For __all Athletes__ in the two DataFrames, __aggregate/add__ the total number of __Gold__, __Silver__ and __Bronze__ Medals over both editions! __Save__ the aggregated DataFrame in the variable __add__!

# 114. First, __set__ the __Athlete__ column as the __index__ in both DataFrames! __Save__ the changes!

# In[ ]:


ath_2008.set_index("Athlete", inplace= True)


# In[ ]:


ath_2012.set_index("Athlete", inplace= True)


# 115. __Add__ both DataFrames with the __most appropriate method__! __Save__ the resulting DataFrame in the variable __add__!

# In[ ]:


add = ath_2008.add(ath_2012, fill_value=0)


# __Inspect__!

# In[ ]:


#run the cell
add.head(10)


# 116. __Sort__ the athletes by the number of __Gold__, __Silver__ and __Bronze__ medals from __high to low__!<br>
# __Fill in the gaps!__ Who is the top athlete?

# In[ ]:


add = add.sort_values(["Gold", "Silver", "Bronze"], ascending = False).astype("int")


# In[ ]:


# run the cell!
add.head()


# In[ ]:


# run the cell!
add.tail()


# No surprise, it´s Usain Bolt!

# # Well Done!

# ------------------------------------------------

# # Hints (Spoiler!)

# 108. insert() method, index pos. 7

# 109. columns attribute

# 110. pd.concat() method, ignore index

# 111. methods sort_values() and reset_index()

# 112. left DataFrame: summer, on "Country" and "Code"

# 113. methods isnull() and value_counts()

# 114. set_index() method

# 115. add() method, fill_value = 0

# 116. pass a list of columns to sort_values() method (sequence matters!)
