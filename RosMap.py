import numpy as np
from matplotlib import cm,colors
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure, show, rc
import  matplotlib
import pandas as pd
#设置字体为楷体
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams["patch.force_edgecolor"] = True
plt.rc('axes',axisbelow=True)
#含有中文字符用GBK编码
df=pd.read_csv('data3_1.csv', delimiter=',', header= 0, encoding="GBK")
Satisfaction=df['满意度'].value_counts()
df2=Satisfaction.reset_index()
df2.columns = ['态度', '数量']
n_row= df2.shape[0]
#依据列数展现数据量在360度内均分角度空间
angle = np.arange(0,2*np.pi,2*np.pi/n_row)
#将展示数据转换为数组
radius = np.array(df2.数量)

fig = figure(figsize=(4, 4), dpi=90)
# 极坐标条形图，polar为True
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

# 方法用于设置角度偏离,参数值为弧度值数值
ax.set_theta_offset(np.pi / 2 - np.pi / n_row)
# 当set_theta_direction的参数值为1,'counterclockwise'或者是'anticlockwise'的时候，正方向为逆时针；
# 当set_theta_direction的参数值为-1或者是'clockwise'的时候，正方向为顺时针；
ax.set_theta_direction(-1)
# 方法用于设置极径标签显示位置,参数为标签所要显示在的角度
ax.set_rlabel_position(360 - 180 / n_row)
# plt.bar(angle,radius, color='#70A6FF',edgecolor="k",width=0.90,alpha=0.9)
plt.bar(angle, radius, color='#F9837A', edgecolor="k", width=0.90, alpha=0.9)
# x轴坐标轴标签
plt.xticks(angle, labels=df2.态度, size=12)
# plt.ylim(-15,125)
plt.ylim(0, 1000)
plt.yticks(np.arange(0, 1000, 100), verticalalignment='center', horizontalalignment='right')

plt.grid(which='major', axis="x", linestyle='-', linewidth='0.5', color='gray', alpha=0.5)
plt.grid(which='major', axis="y", linestyle='-', linewidth='0.5', color='gray', alpha=0.5)

plt.show()