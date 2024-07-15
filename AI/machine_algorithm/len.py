import numpy as np
import matplotlib.pyplot as plt

# 创建模拟数据
np.random.seed(1) # 设置随机数种子，确保每次运行结果一致
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 定义模型（断言或预测）
def predict(X, w, b):
    return X.dot(w) + b # 线性回归模型 y = wx + b

# 定义损失函数
def compute_loss(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2) # 均方误差损失函数

# 梯度下降优化（相对简单的机器算法）
def gradient_descent(X, y, w, b, learning_rate, epochs):
    m = len(y)
    loss_history = [] # 存储每次迭代的损失值
    
    for epoch in range(epochs): # 循环迭代次数
        y_pred = predict(X, w, b) # 预测值
        loss = compute_loss(y, y_pred) # 计算损失值
        loss_history.append(loss) # 记录每次迭代的损失值
        
        dw = -2/m * X.T.dot(y - y_pred) # 计算梯度
        db = -2/m * np.sum(y - y_pred)  
        
        w -= learning_rate * dw # 更新参数
        b -= learning_rate * db
        
        if epoch % 100 == 0:
            print(f'Epoch {epoch}: Loss = {loss}')
    
    return w, b, loss_history # 返回优化后的参数和损失值

# 初始化参数
w = np.random.randn(1, 1)
b = np.random.randn(1)

# 设置超参数
learning_rate = 0.1
epochs = 1000 # 迭代次数

# 训练模型
w, b, loss_history = gradient_descent(X, y, w, b, learning_rate, epochs)

# 可视化损失函数的变化过程
plt.plot(loss_history)
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Loss Function')
plt.show()

# 预测
y_pred = predict(X, w, b)

# 可视化结果
plt.scatter(X, y, label='Data')
plt.plot(X, y_pred, color='red', label='Prediction')
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
