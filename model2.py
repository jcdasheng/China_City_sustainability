import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection  import cross_val_score, GridSearchCV
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['Simhei']
pd.plotting.register_matplotlib_converters()
df = pd.read_excel('new1.xlsx')
df2 = pd.read_excel('test.xlsx')

plt.figure(figsize=(14,6))
sns.lineplot(data=df['Score'], label="Score")
sns.scatterplot(x=df['Score'], y=df.index)
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
model = XGBRegressor(n_estimators=1000, learning_rate=0.05, n_jobs=4)
model = model.fit(X_train, y_train,
             early_stopping_rounds=5,
             eval_set=[(X_test, y_test)],
             verbose=False)
print(model.score(X_test, y_test))#输出
pre = model.predict(X_test)
print('r2:', r2_score(pre, y_test))
print('mse:', mean_squared_error(pre, y_test))
newx =df2.iloc[:, 2:19]
print(newx)

#pd.DataFrame(model.predict(newx), columns=['prediction_score']).to_excel('~/Desktop/final.xlsx')

plt.figure(figsize=(16,7))
plt.plot(y_test.values,'og:', label='true', )
plt.plot(pre, '*r:', label='prediction')
plt.legend()
plt.show()