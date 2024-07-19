import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import matplotlib.pyplot as plt

# 读取训练集和测试集数据
train_data = pd.read_csv('train_data.csv')
test_data = pd.read_csv('test_data.csv')

# 提取特征和标签
X_train = train_data[['X']].values
y_train = train_data[['y']].values
X_test = test_data[['X']].values
y_test = test_data[['y']].values

# 创建一个线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 预测测试集
y_pred = model.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R^2 Score: {r2}")

# 保存模型到本地
joblib.dump(model, 'linear_regression_model.pkl')

# 可视化结果
plt.scatter(X_test, y_test, color='black', label='Actual data')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted data')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()

# 加载模型并进行推理
loaded_model = joblib.load('linear_regression_model.pkl')
sample_data = np.array([[5.0]])  # 示例数据
prediction = loaded_model.predict(sample_data)
print(f"Prediction for {sample_data[0][0]}: {prediction[0][0]}")