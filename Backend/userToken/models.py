import datetime
import traceback

from django.contrib.auth.hashers import make_password
from django.db import models, transaction

from account.models import User


class userToken(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 有效时间
    endTime = models.DateTimeField('结束时间', default=datetime.datetime.now)
    # 机器码
    machineCode1 = models.CharField(max_length=100, null=True, blank=True)
    machineCode2 = models.CharField(max_length=100, null=True, blank=True)
    machineCode3 = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "cms_Token"

    @staticmethod
    def addUser(data):
        try:
            username = data['username']
            if not User.objects.filter(username=username, usertype=10).exists():
                with transaction.atomic():
                    user = User.objects.create(
                        username=username,
                        password=make_password(data['password']),
                        usertype=10,
                    )
                    endTime = datetime.datetime.now() + datetime.timedelta(days=1)
                    userToken.objects.create(
                        user=user,
                        endTime=endTime
                    )
            return {'ret': 0}

        except:
            return {'ret': 1, 'msg': '添加用户信息失败！'}

    @staticmethod
    def listUser(data):
        user_id = data['user_id']
        qs = userToken.objects.filter(user__id=user_id).values('user__username', 'endTime', 'machineCode1',
                                                               'machineCode2', 'machineCode3')
        qs = list(qs)
        if qs:
            retlist = qs[0]
            for i in ['1', '2', '3']:
                if retlist[f'machineCode{i}'] is None:
                    retlist[f'machineCode{i}'] = '未绑定'
                else:
                    retlist[f'machineCode{i}'] = '已绑定'
            retlist['endTime'] = str(retlist['endTime']).replace('T', ' ')
            return {'ret': 0, 'retlist': retlist}
        else:
            return {'ret': 0}

    @staticmethod
    def modifyToken(data):
        try:
            user_id = data['user_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                userCode = userToken.objects.get(user__id=user_id)
            except:
                traceback.print_exc()
                return {'ret': 1}
            if 'days' in data:
                if userCode.endTime < datetime.datetime.now():
                    userCode.endTime = datetime.datetime.now() + datetime.timedelta(days=data['days'])
                else:
                    userCode.endTime = userCode.endTime + datetime.timedelta(days=data['days'])
            if 'machineCode1' in data:
                userCode.machineCode1 = data['machineCode1']
            if 'machineCode2' in data:
                userCode.machineCode2 = data['machineCode2']
            if 'machineCode3' in data:
                userCode.machineCode3 = data['machineCode3']
            # 注意，一定要执行save才能将修改信息保存到数据库
            userCode.save()
            return {'ret': 0}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '修改失败！'}


class order(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    orderNo = models.CharField(max_length=100, null=True, blank=True)
    money = models.CharField(max_length=100, null=True, blank=True)
    # 1： 未付款 | 2： 已付款
    status = models.PositiveIntegerField()
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)

    product = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "cms_Order"

    @staticmethod
    def add_order(data):
        try:
            order.objects.create(
                user=User.objects.get(id=data['user_id']),
                orderNo=data['orderNo'],
                status=1,
                product=data['product'],
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
                orderLs = order.objects.get(orderNo=orderNo)
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
            qs = order.objects.values().order_by('-id')
        else:
            qs = order.objects.filter(user__id=user_id).values().order_by('-id')

        qs = list(qs)

        for i in range(len(qs)):
            qs[i]['create_time'] = qs[i]['create_time'].strftime("%Y-%m-%d %H:%M:%S")

        return {'ret': 0, 'retlist': qs}


class products(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 用户
    price = models.FloatField(null=True, blank=True)
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
        db_table = "cms_products"

    @staticmethod
    def add_products(data):
        try:
            products.objects.create(
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
                product = products.objects.get(id=product_id)
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
            qs = products.objects.filter(id=data['product_id']).values()
            return list(qs)[0]
        user_type = data['usertype']
        if user_type == 1:
            qs = products.objects.values().order_by('-id')
        else:
            qs = products.objects.filter(status=1).values().order_by('-id')

        qs = list(qs)

        return {'ret': 0, 'retlist': qs}
