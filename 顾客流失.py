import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

#决策树不能有缺失值，且要保证数据类型一致

data = pd.read_csv('communication.csv')

X = data.drop('type', axis=1)  # 特征数据
y = data['type']              # 目标变量（客户是否流失）

# 划分训练集和测试集，决策树只支持二维数组，使用一维数组会报错
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

# 训练模型
model = DecisionTreeClassifier(criterion='entropy', max_depth=3)    #分类器,max_depth是树深参数
model.fit(X_train, y_train)

# 预测并评估
y_pred = model.predict(X_test)

print("准确率:", accuracy_score(y_test, y_pred))
print("混淆矩阵:\n", confusion_matrix(y_test, y_pred))

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=X.columns, class_names=['低', '高'], filled=True)
plt.show()
