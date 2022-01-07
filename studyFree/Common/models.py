import traceback

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.paginator import Paginator, EmptyPage
from django.db import models
# 可以通过 命令 python  manage.py createsuperuser 来创建超级管理员
# 就是在这User表中添加记录
from django.db.models import Q


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)

    # 用户类型
    # 1： 超管 | 100： 教师  | 1000：学生 | 10：产品用户
    usertype = models.PositiveIntegerField()

    # 真实姓名
    realName = models.CharField(max_length=30, db_index=True)

    # 真实姓名
    phone = models.CharField(max_length=11, null=True, blank=True)

    # aviator
    aviator = models.CharField(max_length=500, null=True, blank=True)

    # 备注描述
    desc = models.CharField(max_length=500, null=True, blank=True)

    REQUIRED_FIELDS = ['usertype', 'realName']

    class Meta:
        db_table = "study_user"

    # 直接在Model中用静态方法定义数据操作
    @staticmethod
    def add_account(data):
        try:
            username = data['username']
            if User.objects.filter(username=username).exists():
                return {'ret': 1, 'msg': f'登录名 {username} 已经存在'}

            if 'desc' not in data:
                data['desc'] = '无评价'
            if 'password' not in data:
                data['password'] = '123456'

            user = User.objects.create(
                username=username,
                password=make_password(data['password']),
                usertype=data['usertype'],
                realName=data['realName'],
                phone=data['phone'],
                desc=data['desc']
            )

            return {'ret': 0, 'id': user.id}
        except:
            return {'ret': 1, 'msg': '添加用户信息失败！'}

    @staticmethod
    def modify_account(data):
        try:
            account_id = data['user_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                account = User.objects.get(id=account_id)
            except:
                return {
                    'ret': 1,
                    'msg': f'id 为`{account_id}`的用户不存在'
                }
            username = data.get('username', None)
            if username and username != account.username:
                if User.objects.filter(username=username).exists():
                    return {'ret': 1, 'msg': f'登录名 {username} 已经存在,请重新命名'}
                else:
                    account.username = username
            if 'realName' in data:
                account.realName = data['realName']
            if 'desc' in data:
                account.desc = data['desc']
            if 'phone' in data:
                account.desc = data['phone']
            if 'password' in data:
                account.password = make_password(data['password'])
            # 注意，一定要执行save才能将修改信息保存到数据库
            account.save()
            return {'ret': 0}
        except:
            return {'ret': 1, 'msg': '修改用户信息失败！'}

    @staticmethod
    def delete_account(data):
        account_id = data['user_id']

        try:
            # 根据 id 从数据库中找到相应的客户记录
            account = User.objects.get(id=account_id)
        except:
            return {
                'ret': 1,
                'msg': f'id 为`{account_id}`的用户不存在'
            }

        # delete 方法就将该记录从数据库中删除了
        account.delete()

        return {'ret': 0}

    @staticmethod
    def list_account(data):
        try:
            # .order_by('-id') 表示按照 id字段的值 倒序排列
            # 这样可以保证最新的记录显示在最前面
            qs = User.objects.values('id', 'username', 'realName', 'phone').order_by('-id')

            search_items = data['search_items']
            if 'usertype' in search_items:
                qs = qs.filter(usertype=search_items['usertype'])
            if 'id' in search_items:
                qs = qs.filter(id=search_items['id'])
            if 'username' in search_items:
                qs = qs.filter(username=search_items['username'])
            if 'realName' in search_items:
                qs = qs.filter(realName=search_items['realName'])
            if 'phone' in search_items:
                qs = qs.filter(realName=search_items['phone'])
            # 查看是否有 关键字 搜索 参数
            keywords = data.get('keywords', None)
            if keywords:
                conditions = [Q(username=one) for one in keywords.split(' ') if one]
                query = Q()
                for condition in conditions:
                    query &= condition
                qs = qs.filter(query)

            # 要获取的第几页 # 每页要显示多少条记录
            pagenum = data.get('pagenum', None)
            pagesize = data.get('pagesize', None)
            if not pagesize or not pagenum:
                pagesize = 1000
                pagenum = 1

            # 使用分页对象，设定每页多少条记录
            pgnt = Paginator(qs, pagesize)

            # 从数据库中读取数据，指定读取其中第几页
            page = pgnt.page(pagenum)

            # 将 QuerySet 对象 转化为 list 类型
            retlist = list(page)

            # total指定了 一共有多少数据
            return {'ret': 0, 'retlist': retlist, 'total': pgnt.count}

        except EmptyPage:
            return {'ret': 0, 'retlist': [], 'total': 0}

        except:
            return {'ret': 2, 'msg': f'未知错误\n{traceback.format_exc()}'}
