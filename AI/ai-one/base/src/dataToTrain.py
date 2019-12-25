import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
df1 = pd.read_csv('../data/kc_train.csv')
# target = pd.read_csv('kc_train2.csv')
target_data = pd.read_csv('../data/kc_test.csv')

# 数据预处理
# df1.info()

# 数据归一化
from sklearn.preprocessing import MinMaxScaler
min_max_scaler = MinMaxScaler()
normal_data = min_max_scaler.fit_transform(df1)
scaler_normal_data = df1 #pd.DataFrame(normal_data, columns=df1.columns)
# 数据初步分离
X = scaler_normal_data.loc[:, ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']]
y = scaler_normal_data.loc[:, ['B']]
# 训练数据和测试数据分化
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.9, random_state=0)
# 使用多远线性回归模型
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
model = linreg.fit(X_train, y_train)
# 训练完毕 使用该模型预测
y_pred = linreg.predict(X_test)
y_pred_target = linreg.predict(target_data)

# origin_data = min_max_scaler.inverse_transform(y_pred)
# 绘图
plt.figure()
plt.plot(range(len(y_pred[1:70])), y_pred[1:70], 'b', label="model")
plt.plot(range(len(y_pred[1:70])), y_test[1:70], 'r', label="predict")
plt.plot(range(len(y_pred[1:70])), y_pred_target[1:70], 'y', label="predict_target")
plt.legend(loc="upper right")
plt.show()


__name__ = "__main__"
print(model.coef_)
print(model.intercept_)
print(y_pred_target)

