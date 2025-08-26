import seaborn as sns
import matplotlib.pyplot as plt

"""
数据集特征

泰坦尼克数据集包含多个特征，其中包括：

PassengerId：乘客编号

Survived：乘客是否存活（0=否，1=是）

Pclass：乘客所在的船舱等级（1=一等舱，2=二等舱，3=三等舱）

Name：乘客姓名

Sex：乘客性别

Age：乘客年龄

SibSp：乘客的兄弟姐妹和配偶数量

Parch：乘客的父母与子女数量

Ticket：票的编号

Fare：票价

Cabin：座位号

Embarked：乘客登船码头（C = Cherbourg; Q = Queenstown; S = Southampton）
"""
df = sns.load_dataset("titanic")
print(df.head())
print("--------------------------------------------------------------------------------")

print(df.info())
print("--------------------------------------------------------------------------------")

print(df.describe())
print("--------------------------------------------------------------------------------")
print(df["sex"].value_counts())
print(df["class"].value_counts())


sns.countplot(x="sex", data=df)
plt.show()

print(df.groupby("sex")["survived"].mean())
