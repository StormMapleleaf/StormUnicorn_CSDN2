import pandas as pd # 用于读取数据
import matplotlib.pyplot as plt # 用于绘制图形
import seaborn as sns # 用于绘制图形

# 读取训练集和测试集数据
train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

# 合并训练集和测试集以便于整体观察
data = pd.concat([train_data, test_data])

# 显示数据的前几行
print("数据集前几行：")
print(data.head())

# 显示数据的基本统计信息
print("\n数据集的基本统计信息：")
print(data.describe())

# 绘制特征X与目标y的关系图
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data['X'], y=data['y'], label='Data points')
plt.title('Scatter plot of X vs y')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()

# 绘制X的分布直方图
plt.figure(figsize=(10, 6))
sns.histplot(data['X'], bins=20, kde=True, label='X distribution')
plt.title('Histogram of X')
plt.xlabel('X')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# 绘制y的分布直方图
plt.figure(figsize=(10, 6))
sns.histplot(data['y'], bins=20, kde=True, label='y distribution')
plt.title('Histogram of y')
plt.xlabel('y')
plt.ylabel('Frequency')
plt.legend()
plt.show()