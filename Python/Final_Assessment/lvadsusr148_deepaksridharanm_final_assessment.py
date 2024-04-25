# -*- coding: utf-8 -*-
"""LVADSUSR148_DeepakSridharanM_Final_Assessment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LvM6e2aphoj97YxL6pnrVASVuOLgZin2
"""

#1 Load Dataset
#a.
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('/content/Final Dataset - IPL.csv')
df.head()

#b.

print("Rows:", df.shape[0])
print("Columns:",df.shape[1])
print("Data types \n",df.dtypes)

numerical_columns=df.select_dtypes(include=['int64','float64']).columns
categorical_columns=df.select_dtypes(include=['object']).columns

print("numerical columns:",numerical_columns)
print("categorical columns:",categorical_columns)

print("Three quartiles")
print(df.describe().loc[['25%','50%','75%']])

print("Unique values:")
print(df.nunique())

print("Null values")
print(df.isnull().sum())

#2. Data Cleaning:
# a.Check and Handle Missing Values
missing_values=df.isnull().sum()
print("Missing Values Count \n",missing_values)
count_of_null_values=df.isnull().sum().sum()
df=df.dropna(axis=1,thresh=0.5)
numeric_columns = df.select_dtypes(include=['int64','float64']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

print("Missing values:", count_of_null_values)

# There are no missing values in this dataset but the above code is to handle and replace missing values

#b.Identify and Resolve Duplicate Data Entries
duplicate_rows=df.duplicated()
df=df.drop_duplicates()#if duplicates are present but we dont have duplicates in our dataset
print("Duplicate rows:", duplicate_rows.sum())

# there are no duplicate entries in this dataset

#3. Descriptive Statistics:
#a.

numerical_data=df.select_dtypes(include=['int64','float64'])
print(numerical_data)
mean=numerical_data.mean(axis=0)
median=numerical_data.median(axis=0)
mode=numerical_data.mode(axis=0)
range=numerical_data.max(axis=0)-numerical_data.min(axis=0)
variance=numerical_data.var(axis=0)
std_dev=numerical_data.std(axis=0)

print(numerical_data.describe())
print("Means:\n", mean)
print("Medians:\n", median)
print("Modes:\n", mode)
print("Ranges:\n", range)
print("Variances:\n", variance)
print("Standard deviations:\n", std_dev)

# 4. Data Visualization:
#a.
#histogram
#first innings score distribution histogram
plt.figure(figsize=(10,6))
sns.histplot(df['first_ings_score'], bins=30, kde=True, color='blue')
plt.title('Distribution of First Inning Scores')
plt.xlabel('First Innings Score Ranges')
plt.ylabel('Frequency')
plt.show()

#second innings score distribution histogram
plt.figure(figsize=(10,6))
sns.histplot(df['second_ings_score'], bins=30, kde=True, color='red')
plt.title(' Distribution of Second Inning Scores')
plt.xlabel('Second Innings Score Ranges')
plt.ylabel('Frequency')
plt.show()

#scatterplot
#Relationship between First inning scores and Second inning scores
plt.title("Relationship between First inning scores and Second inning scores")
sns.scatterplot(x='first_ings_score',y='second_ings_score',data=numerical_data)
plt.xlabel('First Inning Scores')
plt.ylabel('Second Inning Scores')
plt.show()

#boxplot
plt.title(" Match Winners first inning scores ")
sns.boxplot(x='match_winner',y='first_ings_score',data=df)
plt.xticks(rotation=45)
plt.show()

#pie_chart
#winner Teamwise highscores
plt.figure(figsize=(8, 8))
plt.title('Teamwise highscores')
d1=df.groupby('match_winner')['highscore'].sum()
plt.axis('equal')
plt.pie(d1,labels=d1.index,autopct='%1.1f%%')
plt.show()

#barplot
#venue vs total matches played
plt.title("venue vs total matches played")
d2=df.groupby('venue')['match_id'].sum()
print(d2)
print(d2.index.tolist())
plt.bar(d2.index,d2.values)
plt.xlabel("Venue")
plt.ylabel("matches played")
plt.xticks(rotation=45)
plt.show()

# 5. Identifying Relationships:
# a.

corr_matrix=numerical_data.corr()
sns.heatmap(corr_matrix,annot=True, cmap='coolwarm', fmt=".2f")

#corr btw sales and quantity
correlation_btw_inning_scores = df['first_ings_score'].corr(df['second_ings_score'])
print("Correlation between first inning score and second inning score :",correlation_btw_inning_scores)
correlation_btw_inning_wickets = df['first_ings_wkts'].corr(df['second_ings_wkts'])
print("Correlation between first inning wicket and second inning wicket :",correlation_btw_inning_wickets )

# 6. Outlier Detection:
#a.
import numpy as np

numerical_columns=df.select_dtypes(include=['int64','float64']).columns
for i in numerical_columns:
  sns.boxplot(df[i])
  plt.title(i)
  plt.ylabel("Values")
  plt.show()

def check_outliers_frame_and_treat(df,columns):
  for column in columns:
    Q1=df[column].percentile(0.25)
    Q3=df[column].percentile(0.75)
    IQR=Q3-Q1
    lower_bound=IQR-1.5*Q1
    upper_bound=IQR+1.5*Q3
    median = df[column].median()
    df[column] = np.where((df[column] < lower_bound) | (df[column] > upper_bound), median, df[column])
  return df

# #yes there are some outliers and these outliers can be treated using the check_outliers_fram_and_treat function
# and the outlier values are treated using mean of that column

# 7.Performance Treands and Venue Impacts
# a.

d3=df.groupby('venue').agg({
    'first_ings_score':'sum',
     'second_ings_score':'sum'
}).reset_index()
print()

plt.bar(df['venue'],df['first_ings_score'])
plt.bar(df['venue'],df['second_ings_score'])
plt.xticks(rotation=45)
plt.xlabel('Venue')
plt.ylabel('Scores')
plt.legend()
plt.show()

#8. player spotlight
#a.
p=df.groupby('player_of_the_match')['match_id'].sum()
print("Player with highest player of the match title :",p.idxmax())
#jasprit Bumrah is often the winner of the "player of the match" title



# The impact of top scorers and best bowlers impacted their team in a very positive way as the data
# suggests that most cases the team of top scorers and team of best bowlers win the match

#9
#a.

#insight 1:
# from the pie chart it is concluded that Gujarat had the highest scores

plt.figure(figsize=(8, 8))
plt.title('Teamwise highscores')
d1=df.groupby('match_winner')['highscore'].sum()
plt.axis('equal')
plt.pie(d1,labels=d1.index,autopct='%1.1f%%')
plt.show()

#insight 2:
#jasprit Bumrah is often the winner of the "player of the match" title
p=df.groupby('player_of_the_match')['match_id'].sum()
print("Player with highest player of the match title :",p.idxmax())

#insight 3:
#Wankhede Stadium Mumbai has the highest number of matches played
plt.title("venue vs total matches played")
d2=df.groupby('venue')['match_id'].sum()
print(d2)
print(d2.index.tolist())
plt.bar(d2.index,d2.values)
plt.xlabel("Venue")
plt.ylabel("matches played")
plt.xticks(rotation=45)
plt.show()

#insight 4:
#the first inning scores and second inning scores often fall in the range 160 runs to 200 runs

plt.title("Relationship between First inning scores and Second inning scores")
sns.scatterplot(x='first_ings_score',y='second_ings_score',data=numerical_data)
plt.xlabel('First Inning Scores')
plt.ylabel('Second Inning Scores')
plt.show()