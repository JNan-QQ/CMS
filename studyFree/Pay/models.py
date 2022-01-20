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
                pay_config.userServerConfig = data['userServerConfig']

            # 注意，一定要执行save才能将修改信息保存到数据库
            pay_config.save()
            return {'ret': 0}
        except:
            return {'ret': 1, 'msg': '修改用户信息失败！'}
