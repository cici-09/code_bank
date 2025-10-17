import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

# 加载数据（示例：销售数据）
data = pd.read_excel('sales_data.xls', index_col='序号')
data.replace({'好': 1, '是': 1, '高': 1, '否': -1, '坏': -1, '低': -1}, inplace=True)
X = data.iloc[:, :3]  # 特征：天气、是否周末、是否有促销
y = data.iloc[:, 3]   # 标签：销量高低
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练模型
model = DecisionTreeClassifier(criterion='entropy', max_depth=3)    #分类器,max_depth是树深参数
model.fit(X_train, y_train)

# 预测并评估
y_pred = model.predict(X_test)

print("准确率:", accuracy_score(y_test, y_pred))
print("混淆矩阵:\n", confusion_matrix(y_test, y_pred))

dot_data = export_graphviz(
    model,
    feature_names=['天气', '是否周末', '是否有促销'],
    class_names=['低', '高'],
    filled=True,
    rounded=True
)   #这段代码原本是生成了一个可供graphviz的字符串，但是没有用到graphviz库，故这段代码毫无意义

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(figsize=(15, 10))
plot_tree(model, feature_names=X.columns, class_names=['低', '高'], filled=True)
plt.show()