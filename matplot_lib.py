from tkinter.ttk import Style
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
x=[8,6,4,7,2,3,6,4]
y=[5,6,7,2,1,4,8,9]
z=[8,7,6,6,9,7,6,0]
'''x1=np.arange(1,55,5)
y1=2+x1'''

print("welcome to data visualization...!!!")

#Line ploting demo
'''plt.subplot(1,2,1)
plt.plot(x, y, color='red', linestyle='--', linewidth=3)
plt.title("Line plotting Demo")
plt.xlabel("x-labal")
plt.ylabel("y-label")

plt.subplot(1,2,2)
plt.plot(x1, y1, color='brown', linestyle=':', linewidth=3)
plt.title("Line plotting Demo")
plt.xlabel("x-labal")
plt.ylabel("y-label")

#Bar Demo
dict={'pooja':78, 'pritee':85, 'vinayak':95, 'vishal':65, 'vivek': 56}
print(dict)
name=dict.keys()
marks=dict.values()
plt.bar(name, marks, color="pink")
plt.xlabel("Names")
plt.ylabel('Marks')
plt.title("Bar Demo of Marks")

#Scatter Plot
plt.subplot(1,2,1)
plt.scatter(x,y, marker='*', color='red', s=50)
plt.title('Scatter Star Demo')
plt.xlabel('X-label')
plt.ylabel('y-label')

plt.subplot(1,2,2)
plt.scatter(y,z, marker=',', color='blue', s=50)
plt.title('Scatter Square Demo')
plt.xlabel('X-label')
plt.ylabel('y-label')

# Histogram
#plt.hist(x, color='red', bins=16)
file=pd.read_csv('country.csv')
plt.hist(file['country-code'], color='red', bins=50)
print('hello')
#print(file.head())

#Box Plot
data=list([x, y, z])
plt.boxplot(data)

#Voilin Plot
plt.violinplot(data)
plt.title('Box and Violin Plot')

#Pie Chart
values=['Mango', 'apple', 'grapes', 'Banana', 'papaya']
quan=[85,75,80,70,37]
plt.pie(quan, labels=values, autopct= '%0.1f%%', colors=['pink', 'red', 'green', 'yellow', 'orange'])
plt.title('Pie chart of fruits')

#Donut Chart
values=['Mango', 'apple', 'grapes', 'Banana', 'papaya']
quan=[85,75,80,70,37]
plt.pie(quan, labels=values, autopct= '%0.1f%%', colors=['pink', 'red', 'green', 'yellow', 'orange'], radius = 1)       #outer circle
plt.pie([500], colors=['black'], radius=0.4)      #inner circle
plt.title('Donut chart of fruits')

#Seaborn line Plot
file=sns.load_dataset('fmri')
file.head()
#print(file)
#sns.lineplot(x='timepoint', y='signal', data=file)
sns.lineplot(x='timepoint', y='signal', hue='region', style='region', markers=True, data=file)
plt.title("Seaborn Demo")

#Bar Plot with seaborn
sns.set(style='whitegrid')
file=pd.read_csv("country.csv")
print(file.head())
sns.barplot(x='region-code', y='name', data=file)

#Scatter plot with seaborn
file=pd.read_csv("country.csv")
sns.scatterplot(x='country-code', y='region-code', hue='sub-region-code', data=file)

# Seaborn Dist Plot
file=pd.read_csv("country.csv")
sns.distplot(file['country-code'], color='purple', vertical=True)
plt.title("Dist_Plot of country file ")

#Seaborn Joinplot
file=pd.read_csv("country.csv")
sns.jointplot(x='country-code', y='region-code',color='brown', data=file, kind='reg')

#pair Plot
df=sns.load_dataset("iris")
sns.pairplot(df, hue='species')
'''
file=sns.load_dataset("matches")
print(file)
plt.show()