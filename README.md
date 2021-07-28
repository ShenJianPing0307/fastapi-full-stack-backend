# fastapi-full-stack-backend

## 功能介绍
- 包含作者、出版社、书籍功能模块
- 作者与书籍一对多关系
- 出版社与书籍是多对多关系
- 三大模块目前都包含有获取数据与添加数据功能
- 通过alembic进行数据库版本管理

## 项目运行
#### 1、导入环境依赖
```shell
pip install -r requirements.txt
```
#### 2、生成数据库
```shell
# 初始化
alembic init alembic

# 在alembic.ini修改数据库的连接配置
sqlalchemy.url = mysql+pymysql://root:123456@127.0.0.1:3306/test

#在alembic文件夹中的env.py文件中修改target_metadata
import models
...
target_metadata = models.Base.metadata
...

# 生成迁移文件
alembic revision --autogenerate -m "generate tables"

# 迁移文件映射到数据库
alembic upgrade head
```
#### 3、运行
```shell
python main.py
```

## 项目效果
![](https://blog.jianping.fun/github_project_picture/fastapi-full-stack-1.png)

## 系列课程







