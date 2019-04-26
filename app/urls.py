"""book_shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name='index'),  # 主页
    path('Shop', views.shop, name='shop'),  # 商城
    path('detail/<int:good_id>', views.detail, name='detail'),  # 商城
    path('place_order', views.create_order, name='create_order'),  # 创建订单
    path('login', views.acc_login, name='login'),  # 登陆
    path('register', views.acc_register, name='register'),  # 注册
    path('logout', views.acc_logout, name='logout'),  # 注销
    path('UserInfo', views.user_info, name='user_info'),  # 用户中心
    path('UserOrder', views.user_order, name='user_order'),  # 个人订单
    path('UserAddr', views.user_addr, name='user_addr'),  # 地址管理
    path('set_default_addr', views.set_default_addr),  # 用户地址
    path('UserCar', views.user_car, name='user_car'),  # 购物车
    path('add_cart', views.add_cart),  # 添加购物车
    path('remove_cart', views.remove_cart),  # 删除购物车商品
    path('pay', views.pay),  # 支付
    path('receiving', views.receiving),  # 确认收货
]
