#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 14:22:41 2017

@author: sahebsingh
"""

""" Titanic Prediction 

Questions we will try and answer :
    Which passenger class has the highest numbers of Survivors ?
    What is the distribution based on age, gender among different class ?
    What is the distribution of various classes who have a family aboard the ship ?
    What is the survival percent among different groups ?

"""

""" Which passenger class has the highest number of Survivor """

import pandas as pd
import pylab as plt
import numpy as np

df = pd.read_csv('/Users/sahebsingh/Desktop/Projects/books/Mastering/Data/titanic data.csv')
print(df.head())

# Checking for null Values

print(df['Pclass'].isnull().value_counts())
print(df['Survived'].isnull().value_counts())# No null values.

# Passengers survived in each class.

passengers_survived = df['Survived'].groupby(df['Pclass']).agg(sum)
#print(passengers_survived)
total_passengers = df['PassengerId'].groupby(df['Pclass']).count()
#print(total_passengers)
survivor_percentage = passengers_survived / total_passengers

# PLotting the Total Number of Survivors.

fig = plt.figure()
ax = fig.add_subplot(111)
rect = ax.bar(passengers_survived.index.values.tolist(),
              passengers_survived, color = 'blue', width = 0.5)
ax.set_ylabel('No of Survivors')
ax.set_xlabel('Total Number of Survivors based on class')
plt.show()
fig.savefig('figure1.png')

# Plotting percentage of plots.

plt.bar(survivor_percentage.index.values.tolist(), survivor_percentage, color = 'blue')
plt.xlabel('Total Percent of Survivors Based on Class')
plt.ylabel('Survivor Percentage')
fig.savefig('figure2.png')
plt.show()


""" What is the distribution based on age, gender among different classes ? """

# Check for null values 

print(df['Sex'].isnull().value_counts()) #No null values.
print(df['Age'].isnull().value_counts()) # 177 Null Values
df = df.fillna(method = 'pad')
print(df["Age"].isnull().value_counts()) # No Null Values.

# Passengers Survived of Each Age.

survived_passengers = df['Survived'].groupby(df['Sex']).agg(sum)
print(survived_passengers)
male_passengers = survived_passengers['male']
print(male_passengers)
female_passengers = survived_passengers['female']
print(female_passengers)


# Plotting for Male vs Female Survivors

plt.bar(1, female_passengers, width = 0.35)
plt.bar(2, male_passengers, width = 0.35)
plt.xlabel('Male vs Female')
fig.savefig('figure3.png')
plt.show()


# Survivors based on gender and class

male_survivors = df[df['Sex'] == 'male'].groupby('Pclass')['Survived'].sum()
print(male_survivors)

female_survivors = df[df['Sex'] == 'female'].groupby('Pclass')['Survived'].sum()
print(female_survivors)

total_male_passengers = df[df['Sex'] == 'male'].groupby('Pclass')['PassengerId'].count()
print(total_male_passengers)
total_female_passengers = df[df['Sex'] == 'female'].groupby('Pclass')['PassengerId'].count()
print(total_female_passengers)

percent_male_survivors = male_survivors / total_male_passengers
percent_female_survivors = female_survivors / total_female_passengers

# PLotting on the basis of Sex

fig = plt.figure()
ax = fig.add_subplot(111)
index = np.arange(male_survivors.count())

rect_1 = ax.bar(index, male_survivors, width = 0.25, color = 'blue')
rect_2 = ax.bar(index + 0.25, female_survivors, width = 0.25, color = 'gold')
plt.ylabel('Survivor Numbers')
plt.title('Male and Female Survivors based on Class')
xTickMarks = passengers_survived.index.values.tolist()
ax.set_xticks(index)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, fontsize=20)
plt.legend()
fig.savefig('figure8.png')
plt.show()


# Plotting by percentage on basis of Sex

fig = plt.figure()
ax = fig.add_subplot(111)
index = [1, 2, 3]
index1 = [1.25, 2.25, 3.25]

rect_1 = ax.bar(index, percent_male_survivors, width = 0.25, color = 'blue')
rect_2 = ax.bar(index1, percent_female_survivors, width = 0.25, color = 'gold')
plt.ylabel('Percentage of Survivors')
plt.title('Male and Female Passengers Based on Class')
xtickmarks = passengers_survived.index.values.tolist()
ax.set_xticks(index)
xtickNames = ax.set_xticklabels(xtickmarks)
plt.setp(xtickNames, fontsize = 20)
plt.legend()
fig.savefig('figure4.png')
plt.show()



""" Distribution of Non Survivors among various classes who have Family Aboard """

# Checking for Null Values 

print(df['SibSp'].isnull().value_counts()) # No Null Values 
print(df['Parch'].isnull().value_counts()) # No Null Values

# Total number of non-survivors in each class

non_survivors = df[(df['SibSp'] > 0) | (df['Parch'] > 0) &
       (df['Survived'] == 0)].groupby('Pclass')['Survived'].count()
print(non_survivors)

# Total Passengers in each class 

total_passengers = df.groupby('Pclass')['PassengerId'].count()
print(total_passengers)

# Percent of Non-Survivors

percent_non_survivors = non_survivors / total_passengers

# Plotting For non-survivors 

fig = plt.figure()
ax = fig.add_subplot(111)
rect = ax.bar(non_survivors.index.values.tolist(), non_survivors, color ='blue',
              width = 0.25)
plt.ylabel('No of Non Survivors')
plt.title('Non Survivor Based on Class')
xtickmarks = non_survivors.index.values.tolist()
ax.set_xticks(xtickmarks)
xticknames = ax.set_xticklabels(xtickmarks)
plt.setp(xticknames, fontsize = 20)
plt.tight_layout()
fig.savefig('figure5.png')
plt.show()


# Plotting percent of non-survivors

fig = plt.figure()
ax = fig.add_subplot(111)
rect = ax.bar(non_survivors.index.values.tolist(), percent_non_survivors, 
              color = 'blue', width = 0.25)
plt.ylabel('Percent of Non Survivors')
plt.title('Non Survivor Percent Based on Class')
xtickmarks = non_survivors.index.values.tolist()
ax.set_xticks(xtickmarks)
xticknames = ax.set_xticklabels(xtickmarks)
plt.setp(xticknames, fontsize = 20) 
fig.savefig('figure6.png')
plt.show()


""" Following Observations are made:
    1) There are a lot of non-survivors in the third class 
    2) Second class has the least number of nonsurvivors with relatives
    3) With respect to the number of passengers first class has the highest 
    percent of non-survivors
    4) Most number of first class passengers has relaives aboard, whereas third
    class had least number of relatives
    
"""


""" Survival Percent Among Different Age Groups """

# Checking for Null Values 

print(df['Age'].isnull().value_counts()) # No null values

# Defining the age binning interval.

age_bins = [1, 18, 25, 40, 60, 80]

# Creating the bins 

df['AgeBin'] = pd.cut(df['Age'], bins = age_bins)
df['AgeBin'] = df['AgeBin'].astype(str)

# Number of Survivors based on age bin

survivors_age = df['Survived'].groupby(df['AgeBin']).agg(sum)
print(survivors_age)

# Total Passengers in Each Bin

total_passengers = df.groupby('AgeBin')['Survived'].count()
print(total_passengers)

# Plotting Total Passengers 

plt.pie(total_passengers, labels = total_passengers.index.values.tolist(), 
        autopct='%1.1f%%', shadow=True, startangle=90)
plt.title('Total Passengers in Different Age Group')
plt.savefig('figure9.png')
plt.show()


# Plotting the pie percentage of Different Survivors of Age Group

plt.pie(survivors_age, labels = survivors_age.index.values.tolist(),
        autopct = '%1.1f%%', shadow = True, startangle = 90)
plt.title('Total Survivors in Different Age Groups')
plt.savefig('figure7.png')
plt.show()


# Difference between Count and Sum

#d_temp = df['Survived'][:20]
#print(d_temp)
#sum_1 = d_temp.agg(sum)
#print(sum_1)
#count_1 = d_temp.count()
#print(count_1)

# Removing cabin, name and ticket

df = df.drop(['Cabin', 'Ticket', 'Name'], axis = 1) # As they do not provide any additional Knowledge.

# Remove missing Values

df = df.dropna()

import patsy

formula = 'Survived ~ C(Pclass) + C(Sex) + Age + SibSp + C(Embarked) + Parch'

# Creating a results dictionary to hold our data regression.

train = df.iloc[0:600, :]
test = df.iloc[600:, :]

# Splitting the data into dependent and independent variable

y_train, x_train = patsy.dmatrices(formula, data = train,
                                   return_type = 'dataframe')
                                   
y_test, x_test = patsy.dmatrices(formula, data = test,
                                 return_type = 'dataframe')
                                   

# Building a Model

import statsmodels.formula.api as sm

model = sm.Logit(y_train, x_train)
res = model.fit()
print(res.summary())

# Pseduo R value between 0.2 and 0.4 is considered to be good. And we got 0.323
# Pseudo R is the correlation between actual and predicted values. Gets values between 0 and 1.

""" 
Also we see that the number of children/parents is of significant importance as
the value of p is greater than 0.05(parch). We will rebuild the model not using parch.
"""

formula2 = 'Survived ~ C(Pclass) + C(Sex) + SibSp + Age'

train = df.iloc[0:600, :]
test = df.iloc[600:, :]

y_train, x_train = patsy.dmatrices(formula2, data = train, 
                                   return_type = 'dataframe')

y_test, x_test = patsy.dmatrices(formula2, data = test, 
                                 return_type = 'dataframe')       
                                 
# Instatenous Model

model = sm.Logit(y_train, x_train)
res = model.fit()
print(res.summary())
                                 
# Model Evaluation.

import seaborn as sns

kde_res = res.predict()
sns.kdeplot(kde_res, shade = True, color = 'b')
plt.title('Distribution of Our Prediction ')
plt.show()
# Distribution is mostly dense btw 0 and 1 which means most people did not survive.


# Evaluating wrt to Gender
sns.regplot(kde_res, x_train['C(Sex)[T.male]'])
plt.xlabel('Predicted Survivor')
plt.ylabel('Male Gender')
plt.title('Predicting the Survivors of Males')
plt.show()
# This shows that the survivor chances of male passengers is less than female passengers.


# Evaluating wrt to Class == 3
sns.regplot(res.predict(), x_train['C(Pclass)[T.3]'])
plt.xlabel('Predicted Chances of Survivors')
plt.ylabel('Class 3')
plt.title('Predicted Chances of Survivors of Class 3')
plt.show()
# This shows that the chances of Survival of Class 3 is less than other classes.


# Evaluating wrt to Age
sns.regplot(res.predict(), x_train['Age'])
plt.xlabel('Chances of Survival')
plt.ylabel('Age')
plt.title('Percentage of Survival wrt Age')
plt.show()
# This shows that older people have lower probability of Survival.


# Evaluating wrt Number of Siblings/Spouces
sns.regplot(res.predict(), x_train['SibSp'])
plt.xlabel('Chances of Survival')
plt.ylabel('Number of Siblings/Spouse')
plt.title('Predicting Survival wrt to Number of Spouse or Siblings')
plt.show()


# Evaluating based on Test Data.







                             






























