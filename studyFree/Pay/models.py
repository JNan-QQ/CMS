import datetime
import json
import traceback

from django.db import models

from Common.models import User


# 用户付款相关配置
class PayConfig(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)
    # 对应用户id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # F币
    coins = models.IntegerField(null=True, blank=True, default=0)
    # 经验
    exp = models.IntegerField(null=True, blank=True, default=0)
    # 等级
    lv = models.IntegerField(null=True, blank=True, default=0)
    # 网上服务截止时间
    deadline = models.DateTimeField(default=datetime.datetime.now)
    # 是否签到
    qd = models.BooleanField(default=False)
    # config
    userServerConfig = models.TextField(default={})

    class Meta:
        db_table = "pay_config"

    @staticmethod
    def list(data):
        try:
            qs = PayConfig.objects.filter(user_id__id=data['user_id']).values('coins', 'lv', 'deadline', 'qd')
            qs = list(qs)
            return {'ret': 0, 'retlist': qs}
        except:
            return {'ret': 1, 'msg': '获取用户配置出错'}

    @staticmethod
    def listServerConfig(data):
        try:
            qs = PayConfig.objects.filter(user_id__id=data['user_id']).values('userServerConfig')
            qs = list(qs)[0]
            return {'ret': 0, 'userServerConfig': json.loads(qs['userServerConfig'])}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '获取用户配置出错'}

    @staticmethod
    def add(data):
        try:
            user_id = data['user_id']
            if PayConfig.objects.filter(user_id__id=user_id).exists():
                return {'ret': 1, 'msg': f'账号已配置'}
            payConfig = PayConfig.objects.create(
                user_id_id=user_id
            )
            return {'ret': 0, 'pay_config_id': payConfig.id}
        except:
            return {'ret': 1, 'msg': '添加用户配置失败！'}

    @staticmethod
    def modify(data):
        try:
            user_id = data['user_id']
            try:
                # 根据 user_id 从数据库中找到相应的客户记录
                pay_config = PayConfig.objects.get(user_id__id=user_id)
            except:
                return {
                    'ret': 1,
                    'msg': f'id 为`{user_id}`的用户配置不存在'
                }

            if 'coins' in data:
                pay_config.coins += data['coins']
                if pay_config.coins < 0:
                    return {'ret': 1, 'msg': '你的余额不足，可以签到获取'}

            # 等级相关
            if 'exp' in data:
                pay_config.exp += data['exp']

                # 1:100,2:1000,3:5000,4:10000,5:50000,6:99999
                exps = pay_config.exp
                if exps < 100:
                    pay_config.lv = 0
                elif exps < 1000:
                    pay_config.lv = 1
                elif exps < 5000:
                    pay_config.lv = 2
                elif exps < 10000:
                    pay_config.lv = 3
                elif exps < 50000:
                    pay_config.lv = 4
                elif exps < 999999:
                    pay_config.lv = 5
                elif exps >= 999999:
                    pay_config.lv = 6

            # 服务截止时间相关
            if 'addDays' in data:
                if datetime.datetime.now() > pay_config.deadline:
                    pay_config.deadline = datetime.datetime.now() + datetime.timedelta(days=data['addDays'])
                else:
                    pay_config.deadline += datetime.timedelta(days=data['addDays'])

            if 'qd' in data:
                if not pay_config.qd:
                    pay_config.qd = True
                else:
                    return {'ret': 1, 'msg': '你今天已经签到过了'}

            if 'userServerConfig' in data:
                pay_config.userServerConfig = json.dumps(data['userServerConfig'])

            # 注意，一定要执行save才能将修改信息保存到数据库
            pay_config.save()
            return {'ret': 0}
        except:
            return {'ret': 1, 'msg': '修改用户信息失败！'}


class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 价格
    price = models.IntegerField(null=True, blank=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 产品名称
    title = models.CharField(max_length=100, null=True, blank=True)
    # 产品描述
    desc = models.CharField(max_length=100, null=True, blank=True)
    # 产品时长
    timeDays = models.IntegerField(null=True, blank=True)
    # 状态 1.正常 2.禁用
    status = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "pay_products"

    @staticmethod
    def add_products(data):
        try:
            Products.objects.create(
                price=data['price'],
                title=data['title'],
                status=1,
                desc=data['desc'],
                timeDays=data['timeDays']
            )
            return {"ret": 0}
        except:
            traceback.print_exc()
            return {'ret': 1}

    @staticmethod
    def modify_products(data):
        try:
            product_id = data['product_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                product = Products.objects.get(id=product_id)
            except:
                traceback.print_exc()
                return {'ret': 1}

            if 'price' in data:
                product.price = data['price']
            if 'title' in data:
                product.title = data['title']
            if 'desc' in data:
                product.desc = data['desc']
            if 'timeDays' in data:
                product.timeDays = data['timeDays']
            if 'status' in data:
                product.status = data['status']
            product.save()
            return {'ret': 0}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '修改失败！'}

    @staticmethod
    def list_products(data):
        if 'product_id' in data:
            qs = Products.objects.filter(id=data['product_id']).values()
            return list(qs)[0]
        user_type = data['usertype']
        if user_type == 1:
            qs = Products.objects.values().order_by('-id')
        else:
            qs = Products.objects.filter(status=1).values().order_by('-id')

        qs = list(qs)

        return {'ret': 0, 'retlist': qs}


class Order(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderNo = models.CharField(max_length=100, null=True, blank=True)
    money = models.IntegerField(null=True, blank=True)
    # 1： 未付款 | 2： 已付款
    GENDER_CHOICES = (
        (0, u'未付款'),
        (1, u'已付款'),
        (2, u'已关闭'),
    )
    status = models.SmallIntegerField(choices=GENDER_CHOICES)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pay_order"

    @staticmethod
    def add_order(data):
        try:
            Order.objects.create(
                user__id=data['user_id'],
                orderNo=data['orderNo'],
                status=1,
                money=data['money']
            )
            return {"ret": 0}
        except:
            traceback.print_exc()
            return {'ret': 1}

    @staticmethod
    def modify_order(data):
        try:
            orderNo = data['orderNo']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                orderLs = Order.objects.get(orderNo=orderNo)
            except:
                traceback.print_exc()
                return {'ret': 1}

            orderLs.status = 2
            orderLs.save()
            return {'ret': 0, 'user_id': orderLs.user.id, 'product': orderLs.product}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '修改失败！'}

    @staticmethod
    def list_order(data):
        user_id = data['user_id']
        user_type = data['usertype']
        if user_type == 1:
            qs = Order.objects.values().order_by('-id')
        else:
            qs = Order.objects.filter(user__id=user_id).values().order_by('-id')

        qs = list(qs)

        status_list = ['未付款', '已付款', '已关闭']
        for i in range(len(qs)):
            qs[i]['create_time'] = qs[i]['create_time'].strftime("%Y-%m-%d %H:%M:%S")
            qs[i]['status'] = status_list[qs[i]['status']]

        return {'ret': 0, 'retlist': qs}
