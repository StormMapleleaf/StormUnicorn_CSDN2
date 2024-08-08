import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

def preprocess_data(data):
    # 将性别和登船港口转换为数值
    data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
    data['Embarked'] = data['Embarked'].map({'C': 0, 'Q': 1, 'S': 2})
    return data

train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')

train_data = preprocess_data(train_data)
test_data = preprocess_data(test_data)

X_train = train_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch','Fare','Embarked']].values
y_train = train_data[['Survived']].values
X_test = test_data[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare','Embarked']].values
y_test = test_data[['Survived']].values

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'模型准确率: {accuracy:.2f}')

joblib.dump(model, 'titanic_model.pkl')

