import pymysql

conn=pymysql.connect(host = '127.0.0.1' # 连接名称
,user = 'root' # 用户名
,passwd='root' # 密码
,port= 3306 # 端口，默认为3306
,db='stu' # 数据库名称
,charset='utf8' # 字符编码
)
cur = conn.cursor()
sql="select * from `orders` "
cur.execute(sql) # 执行SQL语句
data = cur.fetchall() # 通过fetchall方法获得数据
#print(data) #data 是个元组
for i in data[:5]:
    print (i)
cur.close()
conn.close()