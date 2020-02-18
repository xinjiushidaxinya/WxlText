from django.db import models

# 每一个模型都映射一个数据库表。每个模型都是一个 Python 的类
class Fangyuan(models.Model):#新建1个Fangyuan表，字段名称为 leixing,weizhi,name,number
    hostname = models.CharField(max_length=64)
