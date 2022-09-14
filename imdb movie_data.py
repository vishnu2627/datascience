#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as pl
import seaborn as sns


# In[3]:


data=pd.read_csv('imdb_top_1000.csv')


# In[4]:


data


# In[5]:


data.head()


# In[6]:


data.tail()


# In[7]:


data.columns


# In[9]:


data.shape


# In[10]:


data.Certificate.describe


# In[11]:


data.No_of_Votes.mean()


# In[12]:


data.isnull().sum()


# In[13]:


display(data['Certificate'].value_counts())


# In[15]:


df_imdb_by_year = data.groupby('Released_Year')['IMDB_Rating'].mean()
df_imdb_by_year.plot( label='Avg IMDB by year', c='r')
pl.legend()
pl.xlabel('Released Year')
pl.ylabel('Avg IMDB')
pl.show()


# In[16]:


df_meta_by_year = data.groupby('Released_Year')['Meta_score'].mean()
df_meta_by_year.plot( label='Avg Meta by year', c='g')
pl.legend()
pl.xlabel('Released Year')
pl.ylabel('Avg Meta')
pl.show()


# In[14]:


df_imdb_by_year = data.groupby('Released_Year')['IMDB_Rating'].mean()
df_meta_by_year = data.groupby('Released_Year')['Meta_score'].mean()

df_imdb_by_year.plot( label='Avg IMDB by year', c='r')
df_meta_by_year.plot( label='Avg Meta by year', c='g')

pl.legend()
pl.xlabel('Released Year')
pl.ylabel('Avg IMDB vs Avg Meta')
pl.show()


# In[18]:


data['Runtime'].describe()


# In[20]:


data[data['Runtime'] == data['Runtime'].min()]


# In[21]:


display(data[data['Runtime'] == data['Runtime'].max()])


# In[22]:


sns.histplot(data=data['Runtime'])
pl.xlabel('Movie running time(minutes)')


# In[27]:


pl.figure(figsize=(20,10))
sns.countplot(x='Certificate', order = data['Certificate'].value_counts().index[0:-1],palette =['#f5c518', '#121212','#8b8b8b'],data = data)


# In[28]:


pl.figure(figsize=(20,10))
sns.countplot(x='IMDB_Rating',palette =['#f5c518', '#121212','#8b8b8b'], data = data)


# In[29]:


pl.figure(figsize=(20,30))
sns.countplot(x='Certificate',hue='IMDB_Rating',order = data['Certificate'].value_counts().index[0:-1],palette ='mako', data = data)


# In[52]:


fig,ax=pl.subplots(figsize=(25,10))
ax.set(facecolor = 'white')
sns.barplot(x=data['Series_Title'][:10], y=data['No_of_Votes'][:10], palette = 'hls')
pl.title('10 Top Voted Movies', fontweight = 'bold', fontsize = 20)
pl.xlabel('Movies', fontsize = 15, fontweight = 'bold')
pl.ylabel('Votes', fontsize = 15, fontweight = 'bold')
pl.show()


# In[49]:


#these are the top 10 voted movies.Schindler's list,star wars episode 7 and The social network are top three most voted.


# In[ ]:


#most of the UA and R certified films are highly rated than other  certified films.


# In[ ]:


#THERE ARE MANY MOVIES IN THE LIST WITH THE RATING OF 7.7 .


# In[ ]:


#MOST OF THE MOVIES ARE U CERTIFICATE MOVIES IN IMDB


# In[ ]:


#FROM THE ABOVE DATASET WE CAN SEE THAT THE AVERAGE MOVIE RATINGS ARE DECREASING FROM 1920 TO PRESENT IN BOTH IMDB AND META.

