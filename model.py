import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection  import cross_val_score, GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler

import seaborn as sns
plt.rcParams['font.sans-serif'] = ['Simhei']
pd.plotting.register_matplotlib_converters()
df = pd.read_excel('new1.xlsx')
df2 = pd.read_excel('test.xlsx')

sns.lineplot(data=df)
# df['Score'] = (df['Score'] - df['Score'].min()) / (df['Score'].max() - df['Score'].min())
#df = df[df['Score']<1.2] #保留小于1.2的
# df['label'] = df['Score'].apply(lambda x:1 if x>0.1 else 0)
# score = df[['Score']]
# df.drop('Score', axis=1, inplace=True)
x = df.iloc[:, 2:19]
y = df.iloc[:, [19]]
print(x)
print(y)
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state=42)#分割测试集训练集
model = KNeighborsRegressor()
model = model.fit(X_train, y_train)
params = {'n_neighbors':range(1, 15, 2),
          'leaf_size':[10, 30, 50]}
grid = GridSearchCV(model, params, cv=5, scoring='r2', n_jobs=-1)#选取最佳参数
grid.fit(X_train, y_train)
print(grid.best_score_, ' using: ', grid.best_params_)
#model = KNeighborsRegressor(n_neighbors=5, leaf_size=10)#k近邻算法
#model = KNeighborsRegressor(n_neighbors=grid.best_params_['n_neighbors'], leaf_size=grid.best_params_['leaf_size'])
model = KNeighborsRegressor(n_neighbors=1, leaf_size=10)
model = model.fit(X_train, y_train)
print(model.score(X_test, y_test))#输出
pre = model.predict(X_test)
print('r2:', r2_score(pre, y_test))
print('mse:', mean_squared_error(pre, y_test))
newx =df2.iloc[:, 2:19]
print(newx)

pd.DataFrame(model.predict(newx), columns=['prediction_score']).to_excel('~/Desktop/final.xlsx')

plt.figure(figsize=(16,7))
plt.plot(y_test.values,'og:', label='true', )
plt.plot(pre, '*r:', label='prediction')
plt.legend()
plt.show()