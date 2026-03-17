import matplotlib.pyplot as plt 
import pandas as pd 
import seaborn as sns 

x1=[1,2,3,4,5,6,7,8,9,10]
y1=[10,6,8,9,23,9,12,2,4,12]

x2=[1,89,32,48,52,66,71,84,19,10]
y2=[10,36,81,92,23,91,12,23,46,12]

plt.scatter(x1, y1, marker="D", s=10, c="red", edgecolor="black")
plt.scatter(x2, y2, marker="+", s=20, c="maroon")
plt.show()

data=pd.read_csv("USA_Housing(1).csv")
data.head()
data.info()

sns.pairplot(data)
plt.show()

sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.show()