import numpy as np
import pandas as pd


 d = {'a':1, 'b':2, 'c':3}
 s4 = pd.Series(d)
 print(d)


 ser1 = pd.Series([2,3,1,4],index=["USA","GERMANY","RUSSIA","JAPAN"])
 print(ser1)

 print(ser1 > 2) 
 print(ser1.iloc[2]) 
 print(ser1.loc("USA")) 


 print(ser1.values) 


 df = pandas.DataFrame(
     data=[[5,True,"x", 2.7]
           ,[5,True,"y", 3.7]
           ,[5,True,"z", 4.7]],
     index=["A","B","C"],
     columns=['num','bool','str','real']
 )
 print(df)


 df = pd.read_csv(r'C:\\Users\\MSI\Desktop\\PythonMath\\demodata.csv') 

 df.to_csv(filename) 

 print(df.head()) 

 df.info() 

 print(df.describe()) 

 df["date"]


 print(df[df["gains"] < 0])
 print(df[(df.weekdays=="Wed") & df.up])
 print(df.query('weekdays == "Wed" and up'))
 res = df.query('weekdays == "Sun" or prices < prices.mean() and gains < 0')

 print(df.sample())
 print(df.sample(n=3))


 print("Info of df:\n", df.info(), "\n\n\nMain desccribes of df:\n", df.describe())

 print(df.head())

 df.dillna(0) # заполняет пробелы
 df.dropna() # удаляет пробелы


 print(df[["Age", "Sex"]].head())

 df["Relatives"] = df["SibSp"] + df["Parch"]

print(df[["SibSp","Parch","Relatives"]].head())
print(len(df[(df['Sex'] =='female') & (df['Survived']== 1)]))
print(len(df[(df['Sex'] =='male') & (df['Survived'] == 1)]))
