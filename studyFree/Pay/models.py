import datetime
import json
import traceback

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage
from django.db import models, transaction

# 用户付款相关配置
from django.db.models import Q

from Common.lib.shara import generate_random_str


class PayConfig(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)
    # 对应用户id
    user_id = models.ForeignKey('Common.User', on_delete=models.CASCADE)
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
    # web_url
    web_url = models.TextField(default={})
    # articleNum
    article = models.IntegerField(null=True, blank=True, default=0)
    # noteBookNum
    notebook = models.IntegerField(null=True, blank=True, default=0)
    # click
    click = models.IntegerField(null=True, blank=True, default=0)

    class Meta:
        db_table = "pay_config"
        app_label = "Pay"

    @staticmethod
    def list(data):
        # noinspection PyBroadException
        try:
            qs = PayConfig.objects.filter(user_id__id=data['user_id']) \
                .values('coins', 'lv', 'deadline', 'qd', 'exp', 'article', 'notebook', 'click')
            qs = list(qs)
            return {'ret': 0, 'retlist': qs}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '获取用户配置出错'}

    @staticmethod
    def listServerConfig(data):
        # noinspection PyBroadException
        try:
            qs = PayConfig.objects.filter(user_id__id=data['user_id']).values('userServerConfig')
            qs = list(qs)[0]
            return {'ret': 0, 'userServerConfig': json.loads(qs['userServerConfig'])}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '获取用户配置出错'}

    @staticmethod
    def listWebUrl(data):
        # noinspection PyBroadException
        try:
            qs = PayConfig.objects.filter(user_id__id=data['user_id']).values('web_url')
            qs = list(qs)[0]
            return {'ret': 0, 'web_url': json.loads(qs['web_url'])}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '获取用户配置出错'}

    @staticmethod
    def modify(data):
        # noinspection PyBroadException
        try:
            user_id = data['user_id']
            try:
                # 根据 user_id 从数据库中找到相应的客户记录
                pay_config = PayConfig.objects.get(user_id__id=user_id)
            except ObjectDoesNotExist:
                return {
                    'ret': 1,
                    'msg': f'id 为`{user_id}`的用户配置不存在'
                }

            if 'coins' in data:
                pay_config.coins += data['coins']
                if pay_config.coins < 0:
                    return {'ret': 1, 'msg': '你的余额不足，可以签到免费获取'}

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
                    pay_config.lv = int((exps - 999999) / 100000)

            # 服务截止时间相关
            if 'addDays' in data:
                if datetime.datetime.now() > pay_config.deadline:
                    pay_config.deadline = datetime.datetime.now() + datetime.timedelta(days=data['addDays'])
                else:
                    pay_config.deadline += datetime.timedelta(days=data['addDays'])

            if 'deadline' in data:
                print(data['deadline'])
                pay_config.deadline = datetime.datetime.strptime(data['deadline'], "%Y-%m-%dT%H:%M:%S.%fZ")

            if 'qd' in data:
                if not pay_config.qd:
                    pay_config.qd = True
                else:
                    return {'ret': 1, 'msg': '你今天已经签到过了'}

            if 'userServerConfig' in data:
                pay_config.userServerConfig = json.dumps(data['userServerConfig'])

            if 'web_url' in data:
                pay_config.web_url = json.dumps(data['web_url'])

            # 注意，一定要执行save才能将修改信息保存到数据库
            pay_config.save()
            return {'ret': 0, 'msg': '修改成功'}
        except:
            traceback.print_exc()
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
        app_label = "Pay"

    @staticmethod
    def add_products(data):
        # noinspection PyBroadException
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
        # noinspection PyBroadException
        try:
            product_id = data['product_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                product = Products.objects.get(id=product_id)
            except ObjectDoesNotExist:
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
    user = models.ForeignKey('Common.User', on_delete=models.CASCADE)
    orderNo = models.CharField(max_length=100, null=True, blank=True)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    # 1： 未付款 | 2： 已付款
    GENDER_CHOICES = (
        (0, u'未付款'),
        (1, u'已付款'),
        (2, u'已关闭'),
        (3, u'已退款'),
    )
    # F币价格/元
    F = models.IntegerField(default=0)
    # 折扣
    Z = models.FloatField(default=0)
    status = models.SmallIntegerField(choices=GENDER_CHOICES)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pay_order"
        app_label = "Pay"

    @staticmethod
    def add_order(data):
        # noinspection PyBroadException
        try:
            Order.objects.create(
                user_id=data['user_id'],
                orderNo=data['orderNo'],
                status=0,
                money=data['money'],
                F=data['F'],
                Z=data['Z']
            )
            return {"ret": 0}
        except:
            traceback.print_exc()
            return {'ret': 1}

    @staticmethod
    def modify_order(data):
        # noinspection PyBroadException
        try:
            orderNo = data['orderNo']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                orderLs = Order.objects.get(orderNo=orderNo)
            except ObjectDoesNotExist:
                traceback.print_exc()
                return {'ret': 1}

            orderLs.status = 1
            orderLs.save()
            return {'ret': 0, 'user_id': orderLs.user.id, 'money': orderLs.money}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '修改失败！'}

    @staticmethod
    def list_order(data):
        user_type = data['usertype']
        if user_type == 1:
            qs = Order.objects.values('id', 'user__username', 'orderNo', 'status', 'create_time', 'money',
                                      'status').order_by('-id')
        else:
            user_id = data['user_id']
            qs = Order.objects.filter(user__id=user_id).values().order_by('-id')

        search_items = data.get('search_items', {})
        if 'id' in search_items:
            qs = qs.filter(id=search_items['id'])
        if 'orderNo' in search_items:
            qs = qs.filter(orderNo=search_items['orderNo'])
        if 'user_id' in search_items:
            qs = qs.filter(user__id=search_items['user_id'])

        # 使用分页对象，设定每页多少条记录
        pageNt = Paginator(qs, data['pageSize'])

        # 从数据库中读取数据，指定读取其中第几页
        page = pageNt.page(data['pageNum'])

        # 将 QuerySet 对象 转化为 list 类型
        qs = list(page)

        for i in range(len(qs)):
            qs[i]['create_time'] = qs[i]['create_time'].strftime("%Y-%m-%d %H:%M:%S")
            qs[i]['status'] = Order.GENDER_CHOICES[qs[i]['status']][1]

        return {'ret': 0, 'retlist': qs, 'total': pageNt.count}


class CDK(models.Model):
    id = models.BigAutoField(primary_key=True)
    # cdk
    cdk = models.CharField(max_length=26, null=True, blank=True)
    # 结束时间
    endTime = models.DateTimeField()
    # 创建时间
    create_time = models.DateTimeField(default=datetime.datetime.now)
    # cdk数量
    num = models.IntegerField(default=0)
    # coin
    coins = models.IntegerField(default=0)
    # days
    days = models.IntegerField(default=0)
    # 状态
    status = models.BooleanField(default=True)
    # 备用
    tmp1 = models.CharField(max_length=100, null=True, blank=True)
    tmp2 = models.CharField(max_length=100, null=True, blank=True)
    tmp3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "pay_cdk"
        app_label = "Pay"

    @staticmethod
    def add(data):
        cdk_str = generate_random_str(10)
        # noinspection PyBroadException
        try:
            CDK.objects.create(
                cdk=cdk_str,
                endTime=data['endTime'],
                num=data['num'],
                coins=data['coins'],
                days=data['days']
            )
            return {"ret": 0}
        except Exception as e:
            traceback.print_exc()
            return {'ret': 1, 'msg': e}

    @staticmethod
    def modify(data):
        # noinspection PyBroadException
        try:
            cdk_id = data['cdk_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                cdk = CDK.objects.get(id=cdk_id)
            except ObjectDoesNotExist:
                traceback.print_exc()
                return {'ret': 1}

            if 'status' in data:
                cdk.status = data['status']
            if 'coins' in data:
                cdk.coins = data['coins']
            if 'days' in data:
                cdk.days = data['days']
            if 'num' in data:
                cdk.num = data['num']
            if 'endTime' in data:
                cdk.endTime = data['endTime']
            if 'minus' in data:
                cdk.num -= abs(data['minus'])

            cdk.save()

            return {'ret': 0}

        except Exception as e:
            return {'ret': 1, 'msg': e}

    @staticmethod
    def list(data):
        try:
            # .order_by('-id') 表示按照 id字段的值 倒序排列
            # 这样可以保证最新的记录显示在最前面
            qs = CDK.objects.values().order_by('-id')

            search_items = data['search_items']
            if 'cdk_id' in search_items:
                qs = qs.filter(id=search_items['cdk_id'])
            elif 'cdk' in search_items:
                qs = qs.filter(cdk=search_items['cdk'])
            elif 'status' in search_items:
                qs = qs.filter(status=search_items['status'])

            # 查看是否有 关键字 搜索 参数
            keywords = data.get('keywords', None)
            if keywords:
                conditions = [Q(username=one) for one in keywords.split(' ') if one]
                query = Q()
                for condition in conditions:
                    query &= condition
                qs = qs.filter(query)

            # 要获取的第几页 # 每页要显示多少条记录
            page_num = data.get('pageNum', 1)
            page_size = data.get('pageSize', 10)

            # 使用分页对象，设定每页多少条记录
            pgn = Paginator(qs, page_size)

            # 从数据库中读取数据，指定读取其中第几页
            page = pgn.page(page_num)

            # 将 QuerySet 对象 转化为 list 类型
            retlist = list(page)

            # total指定了 一共有多少数据
            return {'ret': 0, 'retlist': retlist, 'total': pgn.count}

        except EmptyPage:
            return {'ret': 0, 'retlist': [], 'total': 0}

        except KeyError:
            return {'ret': 1, 'msg': '参数错误'}

    @staticmethod
    def delete_cdk(data):
        # noinspection PyBroadException
        try:
            cdk_id = data['cdk_id']
            cdk = CDK.objects.get(id=cdk_id)
            cdk.delete()
            return {'ret': 0}
        except Exception as e:
            return {'ret': 1, 'msg': e}


class cdkUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    # cdk_id
    cdk_id = models.ForeignKey('Pay.CDK', on_delete=models.CASCADE)
    # user_id
    user_id = models.ForeignKey('Common.User', on_delete=models.CASCADE)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # coin
    coins = models.IntegerField(default=0)
    # days
    days = models.IntegerField(default=0)
    # 备用
    tmp1 = models.CharField(max_length=100, null=True, blank=True)
    tmp2 = models.CharField(max_length=100, null=True, blank=True)
    tmp3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "cdk_user"
        app_label = "Pay"

    @staticmethod
    def add(data):
        try:
            # noinspection PyBroadException
            try:
                cdk = CDK.objects.get(cdk=data['cdk'])
                if cdk.num == 0:
                    return {'ret': 1, 'msg': '你来晚了！cdk已被抢完！！！'}
                if cdk.endTime < datetime.datetime.now():
                    return {'ret': 1, 'msg': 'cdk已过期'}
            except:
                return {'ret': 1, 'msg': '无效cdk！'}

            if cdkUser.objects.filter(cdk_id__id=cdk.id, user_id__id=data['user_id']).exists():
                return {'ret': 1, 'msg': f'不能重复兑换!'}

            with transaction.atomic():
                cdkUser.objects.create(
                    cdk_id=cdk,
                    user_id_id=data['user_id'],
                    coins=cdk.coins,
                    days=cdk.days
                )
                CDK.modify({'minus': 1, 'cdk_id': cdk.id})
                PayConfig.modify({'user_id': data['user_id'], 'coins': cdk.coins, 'addDays': cdk.days})
            return {"ret": 0}
        except Exception as e:
            traceback.print_exc()
            return {'ret': 1, 'msg': e}
