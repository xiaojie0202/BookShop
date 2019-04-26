from django.db import models
from DjangoUeditor.models import UEditorField
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models piphere.

class Goods(models.Model):
    """商品信息表"""
    status_choices = (
        (0, '下线'),
        (1, '上线'),
    )

    name = models.CharField(max_length=20, verbose_name='书籍名称')
    desc = models.CharField(max_length=256, verbose_name='书籍简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='书籍价格')
    unite = models.CharField(max_length=20, verbose_name='商品单位')
    image = models.ImageField(upload_to='goods', verbose_name='书籍主图')

    book_type = models.CharField(max_length=64, verbose_name='书籍类型')
    publishing_house = models.CharField(max_length=64, verbose_name='出版社')

    stock = models.IntegerField(default=1, verbose_name='商品库存')
    sales = models.IntegerField(default=0, verbose_name='商品销量')
    status = models.SmallIntegerField(default=1, choices=status_choices, verbose_name='商品状态')
    detail = UEditorField(width=600, height=300, toolbars="full", imagePath="images/",
                          filePath="files/", upload_settings={"imageMaxSize": 1204000}, settings={},
                          verbose_name='商品详情')
    add_datetime = models.DateTimeField(verbose_name='添加时间', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'goods'
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name


class UserAddress(models.Model):
    """用户地址类"""
    user = models.ForeignKey(User, verbose_name='所属账户', on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name='收件人')
    addr = models.CharField(max_length=256, verbose_name='收件地址')
    zip_code = models.CharField(max_length=6, null=True, verbose_name='邮政编码')
    phone = models.CharField(max_length=11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name='是否默认')

    class Meta:
        db_table = 'user_address'
        verbose_name = '地址'
        verbose_name_plural = verbose_name


class OrderInfo(models.Model):
    """用户订单信息类"""
    PAY_METHODS = {
        '1': "货到付款",
        '2': "微信支付",
        '3': "支付宝",
        '4': '银联支付'
    }

    PAY_METHODS_ENUM = {
        "CASH": 1,
        "ALIPAY": 2
    }

    ORDER_STATUS_ENUM = {
        "UNPAID": 1,
        "UNSEND": 2,
        "UNRECEIVED": 3,
        "UNCOMMENT": 4,
        "FINISHED": 5
    }

    PAY_METHOD_CHOICES = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝'),
        (4, '银联支付')
    )

    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '已完成')
    )

    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单id')
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    addr = models.ForeignKey('UserAddress', verbose_name='地址', on_delete=models.CASCADE)
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    total_count = models.IntegerField(default=1, verbose_name='商品数量')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品总价')
    transit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单运费')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    trade_no = models.CharField(max_length=128, default='', verbose_name='支付编号')
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = 'df_order_info'
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name


class OrderGoods(models.Model):
    """用户订单商品类"""
    order = models.ForeignKey('OrderInfo', verbose_name='订单', on_delete=models.CASCADE)
    sku = models.ForeignKey('Goods', verbose_name='商品', on_delete=models.CASCADE)
    count = models.IntegerField(default=1, verbose_name='商品数目')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')

    def get_order_id(self):
        return self.order.order_id

    class Meta:
        db_table = 'df_order_goods'
        verbose_name = '订单商品'
        verbose_name_plural = verbose_name


# 购物车
class ShopCart(models.Model):
    """购物车"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    good_count = models.IntegerField(verbose_name='商品数量')

    def __str__(self):
        return self.good.name

    class Meta:
        db_table = 'shop_cart'
        verbose_name = '购物车'
        verbose_name_plural = verbose_name


# 浏览记录
class History(models.Model):
    """浏览记录"""
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    good = models.ForeignKey(Goods, verbose_name='商品', on_delete=models.CASCADE)
    show_datetime = models.DateTimeField(auto_now=True, verbose_name='浏览时间')
