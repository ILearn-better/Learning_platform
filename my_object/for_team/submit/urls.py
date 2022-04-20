from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views#此处注意from对象

urlpatterns = [
    url(r'path', views.path_return),
    url(r'^$', views.submitT, name="home"),#主页面会印象其他页面响应,不能设为空。此处表示以空开头，以空结尾
    url(r'teacher_li', views.teacher_li),
    url(r'teacher_zhi', views.teacher_zhi),
    url(r'teacher_dai', views.teacher_dai),
    url(r'des',views.DESjiami),
    url(r'deepLeaning',views.deepLeaning),
    # path('admin/', admin.site.urls),
]
