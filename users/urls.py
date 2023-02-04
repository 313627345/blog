from django.urls import path
from users.views import RegisterView

from users.views import ImageCodeView #验证码

urlpatterns = [
    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('register/',RegisterView.as_view(),name='register'),

    # 参数1：路由
    # 参数2：视图函数
    # 参数3：路由名，方便通过reverse来获取路由
    path('imagecode/', ImageCodeView.as_view(),name='imagecode'),
]

