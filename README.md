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
[Python虚拟环境搭建-学习视频教程-腾讯课堂ke.qq.com
![](https://upload-images.jianshu.io/upload_images/26768070-a12c979c9ca46549?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)](https://link.zhihu.com/?target=https%3A//ke.qq.com/course/3615906%3Ftuin%3D24638831)   

[FastAPI+SQLAlchemy+Alembic后台开发-学习视频教程-腾讯课堂ke.qq.com
![](https://upload-images.jianshu.io/upload_images/26768070-d8d4312697c2dcab?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)](https://link.zhihu.com/?target=https%3A//ke.qq.com/course/3615855%3Ftuin%3D24638831)  

[Vue+Easy Mock前台开发-学习视频教程-腾讯课堂ke.qq.com
![](https://upload-images.jianshu.io/upload_images/26768070-efed3d1742e14348?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)](https://link.zhihu.com/?target=https%3A//ke.qq.com/course/3616355%3Ftuin%3D24638831)  

[前后台分离项目部署实战-学习视频教程-腾讯课堂ke.qq.com
![](https://upload-images.jianshu.io/upload_images/26768070-6b74d152ef385a1e?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)](https://link.zhihu.com/?target=https%3A//ke.qq.com/course/3617910%3Ftuin%3D24638831)






