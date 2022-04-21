import pandas
import csv, sqlite3

conn= sqlite3.connect("./static/Data.db")
df = pandas.read_csv("./static/Data.csv")

# df = pandas.read_excel(io='./Data.xlsx',sheet_name=0)
# 如果源文件存储为xls或xlsx，切换为注释掉的命令即可

df.to_sql('Data', conn, if_exists='append', index=False)
# 默认写入表：Data
print('写入成功')
