#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df  = pd.read_csv('D:/Jacob/ADS/Assignments/ADS-Assignment-2-3-main/WA_Fn-UseC_-HR-Employee-Attrition.csv')

df[['Education','Attrition','MonthlyIncome']]

educ_att =  df.groupby(['Education','Attrition'],as_index=False).MonthlyIncome.mean()
print(educ_att)

plt.figure(figsize=(15,10))
sns.barplot(data = educ_att,x="Education", y="MonthlyIncome", hue="Attrition")

plt.title("Comparison Monthly Income to Education & Attrition")
plt.xlabel("Education")
plt.ylabel("MonthlyIncome")


# In[ ]:




