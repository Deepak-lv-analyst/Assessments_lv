# -*- coding: utf-8 -*-
"""LVADSUSR148_DeepakSridharanM-ia2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1A4ISIOwPj93IEDN_sDsodIEMhp1b-ZTk
"""

#1
import numpy as np
arr=np.array([1,2,3,4,5])
mean=np.mean(arr)
median=np.median(arr)
sum=np.sum(arr)
std_deviation=np.std(arr)
print("Mean:",mean,"Median:",median,"Sum:",sum,"Standard Deviation:",std_deviation)

#2

import numpy as np
def normalize_data_attributes(data):

    mean = np.mean(data, axis=0)
    std_deviation = np.std(data, axis=0)
    norm_data = (data - mean) / std_deviation

    return norm_data
d = np.array([[160, 70, 30],
                 [165, 65, 35],
                 [170, 75, 40]])

data = normalize_data_attributes(d)
print("Normalized Data:")
print(data)

#3
import numpy as np

def avg_last_three(scores):
    d1 = scores[:, -3:]
    scores_last = np.ma.masked_equal(d1, -1)
    avg_scores = scores_last.mean(axis=1)
    return avg_scores


scores = np.array([[68,45,91,33,-1,43,66],
                   [91,78,-1,43,66,55,-1],
                   [51,-1,43,96,93,-1,63]])

data = avg_last_three(scores)
print("average scores of last three subjects:")
print(data)

#4
import numpy as np

arr=np.linspace(15,25,24)
print(arr)

#5
import numpy as np
daily_closing_prices=np.array([100,102,98,105,107,110,108,112,115,118,120])
window_size=5
arr=daily_closing_prices(0:,window_size).mean()
print(arr)

#6
n/a

#7
import numpy as np
properties_matrix=np.array([[1,2,3],
                            [4,5,6],
                            [7,8,9]])
print(np.linalg.det(properties_matrix))

#8
arr=np.array([[1,2,3],
                            [4,5,6],
                            [7,8,9]])
condition=arr>5
arr2=arr[condition]
print(arr2)

#9
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
        'Age': [25, 30, 35, 40, 45, 50, 55],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Miami', 'Boston'],
        'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales', 'IT', 'HR']}


import pandas as pd
df = pd.DataFrame(data)

filtered_df = df[(df['Age'] < 45) & (df['Department'] != 'HR')]
employees_list = filtered_df[['Name', 'City']].values.tolist()

print("List of employees who are under 45 not working in the HR Dept:")
print(employees_list)

#Q10
import pandas as pd

data = {
    'Department': ['Electronics', 'Electronics', 'Clothing', 'Clothing', 'Home Goods'],
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Sales': [70000, 50000, 30000, 40000, 60000]
}

df = pd.DataFrame(data)
department_sales = df.groupby('Department')['Sales'].sum()

department_salespeople_count = df.groupby('Department')['Salesperson'].size()
average_sales_per_salesperson = department_sales / department_salespeople_count
ranked_departments = average_sales_per_salesperson.sort_values(ascending=False).reset_index()
ranked_departments['Salespeople Count'] = department_salespeople_count.reset_index(drop=True)

print("Ranked Departments based on Average Sales per Salesperson:")
print(ranked_departments)

#11
import pandas as pd

data = {
    'Product': ['Apples', 'Bananas', 'Cherries', 'Dates', 'Elderberries', 'Flour', 'Grapes'],
    'Category': ['Fruit', 'Fruit', 'Fruit', 'Fruit', 'Fruit', 'Bakery', 'Fruit'],
    'Price': [1.20, 0.50, 3.00, 2.50, 4.00, 1.50, 2.00],
    'Promotion': [True, False, True, True, False, True, False]
}

df = pd.DataFrame(data)
fruit_df = df[df['Category'] == 'Fruit']

avg_fruit_price = fruit_df['Price'].mean()

potential_promotions = fruit_df[(fruit_df['Price'] > avg_fruit_price) & (~fruit_df['Promotion'])]

print("Potential candidates for future promotions:")
print(potential_promotions)

#12
import pandas as pd
employee_data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David'],
    'Department': ['HR', 'IT', 'Finance', 'IT'],
    'Manager': ['John', 'Rachel', 'Emily', 'Rachel']
}

project_data = {
    'Employee': ['Alice', 'Charlie', 'Eve'],
    'Project': ['P1', 'P3', 'P2']
}

employee_df = pd.DataFrame(employee_data)
project_df = pd.DataFrame(project_data)

merged_df = pd.merge(project_df, employee_df, on='Employee', how='left')
merged_df['Department'] = merged_df['Department'].fillna('Unassigned')
merged_df['Manager'] = merged_df['Manager'].fillna('Unassigned')
department_overview = merged_df.groupby(['Department', 'Manager'])['Project'].apply(list).reset_index()

print("Complete Departmental Overview:")
print(department_overview)

#13
n/a

#14
n/a

#15
n/a