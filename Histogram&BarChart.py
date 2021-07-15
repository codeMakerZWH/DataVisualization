import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data3_1.csv',encoding="GBK")
# nv = 0
# nan = 0
# for i in range (0,2000):
#     if(df.iat[i,0]== '女'):
#         nv += 1
#     else:
#         nan += 1
#
# #gender=df['性别'].value_counts()
# plt.figure(figsize = (12,8),dpi = 100,facecolor='#ecf0e2')
# plt.bar(['男','女'], [nan,nv], color = ['#f6d2c4','#95d1cf'])
# plt.xlabel('性别', fontsize = 10)
# plt.ylabel('网购人数', fontsize = 10)
# plt.title('网购男女人数比较', fontsize = 15)

#按照满意度分析
# Satisfaction=df['满意度'].value_counts()
# plt.barh(Satisfaction.index, Satisfaction.values)
# plt.figure(figsize = (12,8),dpi = 100)
# plt.barh(Satisfaction.index, Satisfaction.values,color = ['#ecf0e2', '#f6d2c4', '#95d1cf'])
# plt.xlabel('人数', fontsize = 10)
# plt.ylabel('满意度', fontsize = 10)
# plt.title('网购满意度人数比较', fontsize = 15)
#
print(df)
gender_satis=pd.crosstab(df['性别'], df['网购次数'])
print(gender_satis)
plt.figure(figsize=(13, 8))
# 构造x轴刻度标签、数据
labels = gender_satis.iloc[0,:].index
first = gender_satis.iloc[0,:].values
second = gender_satis.iloc[1,:].values
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.25  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width/2，x + width/2即每组数据在x轴上的位置
plt.bar(x - width/2, first, width, label='女')
plt.bar(x + width/2, second, width, label='男')
plt.ylabel('购物次数')
plt.xlabel('网购次数')
plt.title('男女购物次数比较')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()

plt.show()