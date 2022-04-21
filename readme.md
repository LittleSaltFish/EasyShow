# 工具简介

本库可以快速将csv数据部署到网站。实现简单的可视化和搜索功能，便于后续开发。

# 环境需求

```shell
pip install sqlite3 flask pandas csv
```

# 食用方法

1. 将爬来的数据(xls/xlsx/csv格式)放进 `static`文件夹中
2. 执行 `MakeDB.py`生成SQLite数据库文件
3. 编辑 `app.py`第51行，将 `XXX` 改为要查询的列
4. 运行 `python3 app.py` 即可
