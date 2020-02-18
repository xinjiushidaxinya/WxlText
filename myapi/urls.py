from django.conf.urls import url, include
import  myapi.views as views
from  myapi.views import Add

urlpatterns = [
    url(r'^add/(?P<name>\d*)/', Add),  # 配置浏览器路径add 用Add函数解析  http:/xxx/add/2344
               ]
#Django 1.10 url 映射规则 为列表，1.80 为元组，所以 逗号不要忘了加