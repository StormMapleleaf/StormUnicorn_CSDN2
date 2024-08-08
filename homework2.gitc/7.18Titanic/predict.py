import pandas as pd
import joblib

# 数据预处理函数
def preprocess_data(data):
    # 将性别和登船港口转换为数值
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
      
    # 忽略列
    if 'Ticket' in data.columns:
        data = data.drop(columns=['Ticket'])
    if 'PassengerId' in data.columns:
        data = data.drop(columns=['PassengerId'])
    if 'Name' in data.columns:
        data = data.drop(columns=['Name'])
    if 'Cabin' in data.columns:
        data = data.drop(columns=['Cabin'])
    
    return data

# 加载模型并进行预测
def predict_new_data(file_path):
    model = joblib.load('titanic_model.pkl')
    new_data = pd.read_csv(file_path)
    new_data = preprocess_data(new_data)
    X_new = new_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']].values
    predictions = model.predict(X_new)
    
    # 将预测结果添加到新数据中
    new_data['Survived'] = predictions

    return new_data

# 使用模型进行预测
new_data_predictions = predict_new_data('predict.csv')
print(new_data_predictions)