#!/usr/bin/env python
# coding: utf-8

# In[76]:


get_ipython().system('pip install seaborn')
import pandas as pd
data = pd.read_csv(r"C:\Users\balad\Desktop\titanic.csv")
dataunchanged=pd.read_csv(r"C:\Users\balad\Desktop\titanic.csv")


# In[77]:


print(data.head())


# In[78]:


data=data.drop(columns=["Name"])


# In[79]:


gender={"male":1,"female":2}
data.Sex=[gender[i] for i in data.Sex]


# In[80]:


data.head()


# In[81]:


from collections import Counter
countClass = [i for i in data.Pclass]
countCabin= [i for i in data.Cabin]
print(Counter(countClass))
print(Counter(countCabin))


# In[82]:


data.isnull().sum()


# In[83]:


import numpy as np
avg=np.nanmean(data.Age)
data["Age"]=data["Age"].replace(np.nan,avg)
print(data.head())
print(data.isnull().sum())


# In[86]:



import seaborn as sns
sns.violinplot(x="Embarked",y="Fare",data=data)


# In[87]:


import seaborn as sns
sns.violinplot(x="Embarked",y="Fare",data=data,palette="rainbow")


# In[88]:


sns.violinplot(x="Embarked",y="Pclass",data=data)


# In[89]:


sns.violinplot(x="Pclass",y="Age",data=data)


# In[90]:


sns.violinplot(x="Pclass",y="Sex",data=data)


# In[84]:


from collections import Counter
countSurvived = [i for i in data.Survived]
print(Counter(countSurvived))


# In[85]:


print("Percentage of people who survied is "+str(34200/891))


# In[91]:


sns.barplot(x="Sex",y="Survived",data=data)


# In[92]:


sns.barplot(x="Pclass",y="Survived",data=data)


# In[93]:


g1 = sns.stripplot(y='Age', x='Survived', data=data)


# In[94]:


g1 = sns.stripplot(y='Age', x='Survived', data=dataunchanged)


# In[95]:


Ageless10=0
Agegreat10=0
Ageless10Survived=0
Agegreat10Survived=0
for i,j in data.iterrows():
    if(j.Age<=10):
        Ageless10+=1
    if(j.Age<=10 and j.Survived==1):
        Ageless10Survived+=1
    if(j.Age>10):
        Agegreat10+=1
    if(j.Age>10 and j.Survived==1):
        Agegreat10Survived+=1
    
print(Ageless10)
print(Ageless10Survived)

print(str(((Ageless10Survived)/Ageless10*100)) + " percent Aged<=10 survived" )

print(Agegreat10)
print(Agegreat10Survived)

print(str(((Agegreat10Survived)/Agegreat10*100)) + " percent Aged>10 survived" )


# In[99]:


Femalefirstclass=0
Femalefirstclasssurvivors=0
for i,j in data.iterrows():
    if(j.Pclass==1 and j.Sex==2):
        Femalefirstclass+=1
    if(j.Pclass==1 and j.Sex==2 and j.Survived==1):
        Femalefirstclasssurvivors+=1
    
print(Femalefirstclass)
print(Femalefirstclasssurvivors)

print(str(((Femalefirstclasssurvivors)/Femalefirstclass*100)) + " percent survived" )


# In[100]:


malenotfirstclass=0
malenotfirstclasssurvivors=0
for i,j in data.iterrows():
    if(j.Pclass!=1 and j.Sex==1):
        malenotfirstclass+=1
    if(j.Pclass!=1 and j.Sex==1 and j.Survived==1):
        malenotfirstclasssurvivors+=1
    
print(malenotfirstclass)
print(malenotfirstclasssurvivors)

print(str(((malenotfirstclasssurvivors)/malenotfirstclass*100)) + " percent survived" )


# In[101]:


sns.violinplot(x="Survived",y="SibSp",data=data)


# In[102]:


wSibsp=0
woutSibsp=0
totws=0
totwos=0

for i,j in data.iterrows():
    if(j.SibSp==1):
        totws+=1
    if(j.SibSp==0):
        totwos+=1
    if(j.SibSp==1 and j.Survived==1):
        wSibsp+=1
    if(j.SibSp==0 and j.Survived==1):
        woutSibsp+=1
    
print(wSibsp)
print(woutSibsp)

print(str(((wSibsp)/totws*100)) + " percent survived" )
print(str(((woutSibsp)/totwos*100)) + " percent survived" )


# In[103]:


sns.violinplot(x="Survived",y="Parch",data=data)


# In[104]:


Pclassnot3Sibsp0Parch0=0
totalPclass3=0
for i,j in data.iterrows():
    if(j.Pclass==3 and j.SibSp==0 and j.Parch==0):
        Pclassnot3Sibsp0Parch0+=1
    if(j.Pclass==3):
        totalPclass3+=1
print(str(((Pclassnot3Sibsp0Parch0)/totalPclass3*100)) + " percent of class 3 passengers have no family onboard" )


# In[105]:


wSibspParch=0
woutSibspParchnotPclass3=0
totwsp=0
totwosp3=0

for i,j in data.iterrows():
    if(j.SibSp==1 or j.Parch==1):
        wSibspParch+=1
    if(j.SibSp==0 and j.Parch==0 and j.Pclass!=3):
        woutSibspParchnotPclass3+=1
    if(j.SibSp==1 or j.Parch==1 and j.Survived==1):
        totwsp+=1
    if(j.SibSp==0 and j.Parch==0 and j.Pclass!=3 and j.Survived==1):
        totwosp3+=1
    

print(str((((totwsp/wSibspParch))*100)) + " percent survived" )
print(str(((totwosp3/woutSibspParchnotPclass3)*100)) + " percent survived" )


# In[106]:


parchsibspwomenpclass=0
totalparchsibspwomenpclass=0
for i,j in data.iterrows():
    if(j.Pclass==1 and j.Sex==2 and j.SibSp==1 and j.Parch==1):
        parchsibspwomenpclass+=1
    if(j.Pclass==1 and j.Sex==2 and j.SibSp==1 and j.Parch==1 and j.Survived==1):
        totalparchsibspwomenpclass+=1
print(parchsibspwomenpclass)
print(totalparchsibspwomenpclass)

print(str(((parchsibspwomenpclass)/totalparchsibspwomenpclass*100)) + " percent survived" )


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




