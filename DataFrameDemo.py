import numpy as np
import pandas as pd
# data = [["A",2010,1],["B",2010,3],["C",2010,4],
#         ["A",2011,3],["B",2011,5],["C",2011,2]]
#
# df=pd.DataFrame(data, columns=['x','year','value'])

dic={
    'x':['A','B','C','A','B','C'],
    'year':[2010,2010,2010,2011,2011,2011],
    'value':[1,3,4,3,5,2]
}
# df=pd.DataFrame(dic)
#print(df)

#print(df[['value','year']])
# print(df.loc[0])
# print(df.head(2))
# print(df.iat[2,1] )
#print(df[df.value>=3])

# columns =pd.MultiIndex.from_product([['A','B','C'],[2010,2011]])
# df2=pd.DataFrame(data=[[1x,3,3,5,4,2]],columns=columns)
# df=df.set_index(['x','year'])
# print(df.loc[('A',2010),'value'])
# df_pivot=df.pivot_table(index='x', columns='year', values='value').reset_index()
# # print(df_pivot)
# print(pd.melt(df_pivot,id_vars='x',var_name='year',value_name='value') )

# print(df.sort_values(by='value',ascending= True) )·
# print(df.sort_values(by='value',ascending= False) )

df1 =pd.DataFrame(dict(x= ["a","b","c"], y=range(1,4)))
df2=pd.DataFrame(dict(x= ["a","b","d"], z =[2,5,3]))
df3=pd.DataFrame(dict(g= ["a","b","d"], z =[2,5,3]))
df4=pd.DataFrame(dict(x= ["a","b","d"], y=[1,4,2],z =[2,5,3]))
#print(df1)
# print(pd.concat([df1,df2],axis= 1) )#横
# print(pd.concat([df1,df3],axis= 0) )#纵

# print(df1.drop(labels="y",axis=1, inplace=False))#列
# print(df1.drop(labels=0,axis=0, inplace=False))#行

# print(pd.merge(left=df1,right=df2,how="left",on="x"))
# print(pd.merge(left=df1,right=df2,how="right",on="x"))
# print(pd.merge(left=df1,right=df2,how="inner",on="x"))
# print(pd.merge(left=df1,right=df2,how="outer",on="x"))
# print(pd.merge(left= df1, right= df4, how= "left",on= ["x", "y"]))

df= pd.DataFrame({'x':['A','B','C', 'A', 'C'],'2010':[ 1,3,4,4,3],'2011':[3,5,2,8,9]})
df_melt= pd.melt(df,id_vars= ['x'],var_name='year',value_name='value')
print('\033[0;31;40m(1):\n\033[0m',df[['2010','2011']].apply(lambda x: x.sum(), axis=1))
print('\033[0;31;40m(2):\n\033[0m',df[['2010','2011']].apply(lambda x: x.sum(), axis=0))
df['2010_2'] = df['2010'].apply(lambda x: x + 2)
df['2010_2011'] = df.apply(lambda x: x['2010'] + 2 * x['2011'], axis=1)
print('\033[0;31;40m(3)(4):\n\033[0m',df)
print('\033[0;31;40m(5):\n\033[0m',df_melt.groupby('year').sum())
print('\033[0;31;40m(6):\n\033[0m',df_melt.groupby('year').std())