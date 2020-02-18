from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse   #通过url显示执行效果，则需要导入此模块
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json

from myapi.models import Fangyuan  # 因为要操作具体的表，所以要导入modle.py 中 定义的类

# Create your views here.
# 在app目录下的views里我们新增两个接口，一个是show_books返回所有的书籍列表（通过JsonResponse返回能被前端识别的json格式数据），
# 二是add_book接受一个get请求，往数据库里添加一条book数据：

def Add(request,name):
    a = Fangyuan.objects.create(hostname=name)
    #给数据库增加数据 ,hostname 为数据库表中的字段名称 ，name 是你传人的参数
    print(name)               #打印 参数具体数值
    return HttpResponse('增加第{}数据成功'.format(a.id))  #通过占位符format，来显示具体修改来哪行ID ，

