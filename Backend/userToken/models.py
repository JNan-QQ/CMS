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
    endTime = models.DateTimeField()
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
                    endTime = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
                    userToken.objects.create(
                        user=user,
                        endTime=endTime
                    )
            return {'ret': 0}

        except:
            return {'ret': 1, 'msg': '添加用户信息失败！'}

    @staticmethod
    def modifyToken(data):
        try:
            user_id = data['user_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                userCode = userToken.objects.get(user__id=user_id)
            except:
                return {'ret': 1}
            if 'days' in data:
                if str(userCode.endTime) < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
                    userCode.endTime = (datetime.datetime.now() + datetime.timedelta(days=data['days'])).strftime(
                        "%Y-%m-%d %H:%M:%S")
                else:
                    userCode.endTime = (
                            datetime.datetime.strptime(userCode.endTime, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(
                                days=data['days'])).strftime("%Y-%m-%d %H:%M:%S")
                userCode.endTime = data
            if 'machineCode1' in data:
                userCode.machineCode1 = data['machineCode1']
            if 'machineCode2' in data:
                userCode.machineCode1 = data['machineCode2']
            if 'machineCode3' in data:
                userCode.machineCode1 = data['machineCode3']
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
    create_time = models.DateField(auto_now=True)

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
                product=data['product']
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
                orderLs = userToken.objects.get(orderNo=orderNo)
            except:
                return {'ret': 1}

            orderLs.status = 2
            orderLs.save()
            return {'ret': 0, 'user_id': orderLs.user, 'product': orderLs.product}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '修改失败！'}
