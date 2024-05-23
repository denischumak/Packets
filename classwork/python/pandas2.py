import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv(r'titanic.csv')
class_names = {1: 'Elite', 2: 'Middle', 3: 'Worker'}
df['Class_Name'] = df['Pclass'].map(class_names)
df['Price_Category'] = df['Fare'].apply(lambda x: 'cheap' if x < 25 else 'expensive')
print(df)
new_df = df[['Name', 'Pclass']].copy()

new_df['Class'] = new_df['Pclass'].map(class_names)
new_df = new_df.sort_values('Pclass')
print(new_df)

class_counts = new_df['Class'].value_counts()
w = len(df[(df['Sex'] =='female') & (df['Survived']== 1)])
m = len(df[(df['Sex'] =='male') & (df['Survived']== 1)])
wd = len(df[(df['Sex'] =='female') & (df['Survived']== 0)])
md = len(df[(df['Sex'] =='male') & (df['Survived']== 0)])
plt.subplot(2, 3, 1)
plt.title('People by Class')
plt.pie(class_counts, labels=class_counts.index, autopct='%1.1f%%', startangle=90)
plt.subplot(2, 3, 2)
plt.title('Survived people by sex')
plt.pie([w, m], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90)
plt.subplot(2, 3, 3)
plt.title('Died people by sex')
plt.pie([wd, md], labels=['Male', 'Female'], autopct='%1.1f%%', startangle=90)
