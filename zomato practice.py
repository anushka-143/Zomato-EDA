import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing dataset
data = pd.read_csv('zomato.csv',encoding='latin-1')
print(data.head(3))

#checking columns
print(data.columns)

#check basic information about the dataset using .info() and .describe()

print(data.info())
print(data.describe())

'''In data analysis, things we do:
1. Missing values
2. Explore about numerical variables
3. Explore about categorical variables
4.Find relationship between features
'''
#finding missing values
print(data.isnull().sum())

#other way to find missing values is to use list comprehension
print([features for features in data.columns if data[features].isnull().sum()>0])

country = pd.read_excel('Country-Code.xlsx')
print(country.head(3))
# we have country code column in our main dataset, lets combine the two dataframes

final = pd.merge(data,country,on='Country Code',how='left')

country_names = final.Country.value_counts().index
print(country_names)

country_val = final.Country.value_counts().values
print(country_val)

#lets plot a pie charge using the above information to find which country has the maximum number of orders(only top 3)

plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')
plt.show()

'''Observation: Zomato's maximum records or transactions are from India then US and then UK'''

ratings=final.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating count'})
'''Observation:
1. when rating is between 4.5 to 4.9---> Excellent
2. When rating is between 4.0 to 4.4---> Very good
3. When rating is between 3.5 to 3.9---> good
4. When rating is between 3.0 to 3.4---> Average
5. When rating is between 2.5 to 2.9---> Average
6. When rating is below than 2.5---> Poor
'''

#plot barplot

sns.barplot(x='Aggregate rating',y='Rating count',data=ratings)
plt.show()


'''Observations: 
1.Not rated count is very high
2.Maximum number of ratings are between 2.5 to 3.4'''