import numpy as np
import pandas as pd
from pandas import Series

dic = {
    '名字' : "张三",
    '学号' : "20180015",
    '英语' : 80,
    '程序设计' : 90,
    '高数' : 95,
    '物理' : 88
}

# index = ["名字", "学号","英语" , "程序设计" , "高数" , "物理"]
# data = ["张三","20180015",80,90, 95,88]
mySeries = Series(dic)
mySeries['物理'] = 80
mySeries['总分'] = mySeries['英语'] + mySeries['程序设计'] + mySeries['高数'] + mySeries['物理']
print(mySeries['总分'])
#print(mySeries.loc['物理'])
#print(mySeries.loc['高数'])

#print(mySeries)