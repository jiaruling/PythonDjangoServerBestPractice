# 基于python Django框架的http服务最佳实践



## 一、常用命令

### 源列表

- 豆瓣：http://pypi.douban.com/simple/
- 中科大：https://pypi.mirrors.ustc.edu.cn/simple/
- 清华：https://pypi.tuna.tsinghua.edu.cn/simple

### Anaconda

```shell

```

### Python

```shell
# 查看库的版本
$ python -m [django] --version # 查看当前环境中django的版本
2.2

# python 环境中的依赖写入 requirement.txt
$ pip freeze > requirements.txt
# 安装 requirement.txt 所包含的依赖
$ pip install -r requirement.txt # 清华源 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Django

```shell
# 创建项目
$ django-admin startproject [mysite]
$ cd mysite

# 创建应用
$ python manage.py startapp [polls]

# 迁移数据库
$ python manage.py makemigrations [polls] # 生成迁移文件
$ python manage.py migrate # 迁移数据库

# 创建管理员账号
$ python manage.py createsuperuser

# 启动项目
$ python manage.py runserver [8080|0.0.0.0:8000]
```



## 二、技术选型

| 名称                                                         | 安装方式                        | Github | Star | 说明                 |
| ------------------------------------------------------------ | ------------------------------- | ------ | ---- | -------------------- |
| **[Django](https://docs.djangoproject.com/zh-hans/4.0/)**    | pip install django==2.2         |        |      | web框架              |
| **[Simple UI](https://simpleui.72wo.com/docs/simpleui/)**    | pip install django-simpleui     |        |      | 后台                 |
| **[Django REST framework](Django REST framework)**           | pip install djangorestframework |        |      |                      |
| coreapi                                                      | pip install coreapi             |        |      | drf 自动生成接口文档 |
| django-filter                                                | pip install django-filter       |        |      | drf 字段过滤         |
| **[django-cors-headers](https://pypi.org/project/django-cors-headers/)** | pip install django-cors-headers |        |      | django 跨域          |
|                                                              |                                 |        |      |                      |
|                                                              |                                 |        |      |                      |
|                                                              |                                 |        |      |                      |

