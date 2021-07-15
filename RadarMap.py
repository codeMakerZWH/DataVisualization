import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygal

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
#含有中文字符用GBK编码
df=pd.read_csv('data3_1.csv', delimiter=',', header= 0, encoding="GBK")
gender_satis=pd.crosstab(df['性别'], df['网购次数'])
radar_chart = pygal.Radar()
radar_chart.title = '男女网购次数比较雷达图'
radar_chart.x_labels = gender_satis.iloc[0,:].index
radar_chart.add('女', gender_satis.iloc[0,:].values.tolist())
radar_chart.add('男', gender_satis.iloc[1,:].values.tolist())
radar_chart.render_to_file('网购比较.svg')