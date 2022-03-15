import datetime
import os.path
import random
import traceback

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage
from django.db import models, transaction
from django.db.models import Q

from Pay.models import PayConfig
from config.settings import BASE_DIR


class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)

    # 用户类型
    # 1： 超管 | 100： 教师  | 1000：学生 | 10：产品用户
    usertype = models.PositiveIntegerField()

    # 真实姓名
    realName = models.CharField(max_length=30, db_index=True)

    # 邮箱
    email = models.CharField(max_length=30, null=True, blank=True)

    # aviator
    aviator = models.CharField(max_length=500, null=True, blank=True)

    # 备注描述
    desc = models.CharField(max_length=500, null=True, blank=True)

    REQUIRED_FIELDS = ['usertype', 'realName']

    class Meta:
        db_table = "study_user"
        app_label = "Common"

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
            if 'usertype' not in data:
                data['usertype'] = 1000

            with transaction.atomic():
                user = User.objects.create(
                    username=username,
                    password=make_password(data['password']),
                    usertype=data['usertype'],
                    realName=data['realName'],
                    email=data['email'],
                    desc=data['desc']
                )
                PayConfig.objects.create(
                    user_id=user
                )

            return {'ret': 0, 'id': user.id}
        except 1:
            traceback.print_exc()
            return {'ret': 1, 'msg': '添加用户信息失败！'}

    @staticmethod
    def modify_account(data):
        try:
            account_id = data['user_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                account = User.objects.get(id=account_id)
            except ObjectDoesNotExist:
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
            if 'email' in data:
                account.email = data['email']
            if 'password' in data:
                account.password = make_password(data['password'])
            if 'usertype' in data:
                account.usertype = data['usertype']
            if 'aviator' in data:
                account.aviator = data['aviator']
            # 注意，一定要执行save才能将修改信息保存到数据库
            account.save()
            return {'ret': 0}
        except KeyError:
            return {'ret': 1, 'msg': '无法获取用户id'}

    @staticmethod
    def delete_account(data):
        account_id = data['user_id']

        try:
            # 根据 id 从数据库中找到相应的客户记录
            account = User.objects.get(id=account_id)
        except ObjectDoesNotExist:
            return {
                'ret': 1,
                'msg': f'id 为`{account_id}`的用户不存在'
            }

        # 删除用户头像
        if account.aviator:
            os.remove(os.path.join(BASE_DIR, account.aviator))

        # delete 方法就将该记录从数据库中删除了
        account.delete()

        return {'ret': 0}

    @staticmethod
    def list_account(data):
        try:
            # .order_by('-id') 表示按照 id字段的值 倒序排列
            # 这样可以保证最新的记录显示在最前面
            qs = User.objects.values('id', 'username', 'usertype', 'realName', 'email', 'aviator').order_by('-id')

            search_items = data['search_items']
            if 'usertype' in search_items:
                qs = qs.filter(usertype=search_items['usertype'])
            if 'id' in search_items:
                qs = qs.filter(id=search_items['id'])
            if 'username' in search_items:
                qs = qs.filter(username=search_items['username'])
            if 'realName' in search_items:
                qs = qs.filter(realName=search_items['realName'])
            if 'email' in search_items:
                qs = qs.filter(email=search_items['email'])
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

        except KeyError:
            return {'ret': 1, 'msg': '参数错误'}


# 名人名言
class CelebrityQuotes(models.Model):
    # 名言id
    id = models.BigAutoField(primary_key=True)
    # 名言内容
    content = models.CharField(max_length=100, null=True, blank=True)
    # 作者
    author = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "study_cq"
        app_label = "Common"

    @staticmethod  # 随机列出已经名言
    def listQuotes():
        retlist = random.choice(list(CelebrityQuotes.objects.values()))
        # total指定了 一共有多少数据
        return {'ret': 0, 'retlist': retlist}

    @staticmethod
    def add(data):
        CelebrityQuotes.objects.create(
            content=data['content'],
            author=data['author']
        )
        return {'ret': 0}

    @staticmethod
    def listAll():
        qs = CelebrityQuotes.objects.values()
        qs = list(qs)
        return {'ret': 0, 'retlist': qs}

    @staticmethod
    def deleteCq(data):
        cq = CelebrityQuotes.objects.get(id=data['cq_id'])
        cq.delete()
        return {'ret': 0}


# 验证码
class EmailCode(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)
    # code
    code = models.CharField(max_length=100, null=True, blank=True, default='123456')
    # 状态
    status = models.PositiveIntegerField(default=1)
    # email
    email = models.CharField(max_length=100, null=True, blank=True)
    # time
    time = models.DateTimeField(auto_now=datetime.datetime.now)

    class Meta:
        db_table = "study_email_code"
        app_label = "Common"

    @staticmethod
    def add(data):
        # noinspection PyBroadException
        try:
            if EmailCode.objects.filter(email=data['email']).exists():
                data['status'] = 1
                res = EmailCode.modify(data)
                return res
            else:
                emailCode = EmailCode.objects.create(
                    email=data['email'],
                    code=data['code']
                )
                return {'ret': 0, 'code_id': emailCode.id, 'msg': '6位验证码，已发送到你的邮箱'}
        except Exception as e:
            return {'ret': 1, 'msg': f'{e}'}

    @staticmethod
    def modify(data):
        try:
            if 'flg' not in data:
                data['flg'] = True
            email = EmailCode.objects.get(email=data['email'])
            if (email.time + datetime.timedelta(seconds=300)) >= datetime.datetime.now() and data['flg']:
                return {'ret': 1, 'msg': '请五分钟后在发送，注册'}
            if 'code' in data:
                email.code = data['code']
            if 'status' in data:
                email.status = data['status']

            email.save()

            return {'ret': 0, 'msg': '6位验证码，已发送到你的邮箱'}
        except ObjectDoesNotExist:
            return {'ret': 1, 'msg': '邮箱与验证码不匹配'}
        except KeyError:
            return {'ret': 1, 'msg': '未获取到数据'}

    @staticmethod
    def checkCode(email, code):
        # noinspection PyBroadException
        try:
            if EmailCode.objects.filter(email=email, code=code, status=1).exists():
                res = EmailCode.modify({'status': 2, 'email': email, 'flg': False})
                return res
            else:
                return {'ret': 1, 'msg': '验证码错误，请重新输入'}
        except:
            return {'ret': 1, 'msg': '验证码可能已过期'}


# 通知
class Message(models.Model):
    # 通知id
    id = models.BigAutoField(primary_key=True)

    # 通知标题
    title = models.CharField(max_length=100, null=True, blank=True)

    # 通知内容
    content = models.TextField(null=True, blank=True)

    # 接收类型
    # 1005： vip通知 | 1000： free通知  | 1006：个人通知  | 1007：暂时不选
    group_type = models.PositiveIntegerField()

    # 通知类型
    #
    message_type = models.PositiveIntegerField()

    # 个人通知用户id
    user = models.CharField(max_length=100, null=True, blank=True)

    # status
    status = models.BooleanField(default=True)

    # 创建时间
    creat_time = models.DateTimeField(auto_now=datetime.datetime.now)

    class Meta:
        db_table = "study_message"
        app_label = "Common"

    @staticmethod
    def add(data):
        # noinspection PyBroadException
        try:
            group_type = data['group_type']
            if group_type == 1006:
                user_str = f"|{'|'.join(data['user_list'])}|"
            else:
                user_str = ''

            # 事务
            with transaction.atomic():
                message = Message.objects.create(
                    title=data['title'],
                    content=data['content'],
                    group_type=group_type,
                    user=user_str
                )

                if group_type == 1007:
                    batch = []
                elif group_type == 1006:
                    batch = [MessageNews(message_id_id=message.id, user_id_id=user_id) for user_id in data['user_list']]
                else:
                    batch = [MessageNews(message_id_id=message.id, user_id=user) for user in
                             User.objects.filter(usertype=data['group_type'])]

                #  在多对多关系表中 添加了 多条关联记录
                MessageNews.objects.bulk_create(batch)
            return {'ret': 0}

        except Exception as e:
            return {'ret': 1, 'msg': f'{e}'}

    @staticmethod
    def list(user_id, usertype, page_size=10, page_num=1):
        if usertype == 1:
            qs = Message.objects.values().order_by('-id')
        else:
            qs = Message.objects.filter(Q(group_type=usertype) | Q(user__contains=f'|{user_id}|')).values().order_by(
                '-id')

            # 使用分页对象，设定每页多少条记录
        page_nt = Paginator(qs, page_size)

        # 从数据库中读取数据，指定读取其中第几页
        page = page_nt.page(page_num)

        # 将 QuerySet 对象 转化为 list 类型
        retlist = list(page)

        # total指定了 一共有多少数据
        return {'ret': 0, 'retlist': retlist, 'total': page_nt.count}


# 新通知
class MessageNews(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)

    # 通知id
    message_id = models.ForeignKey(Message, on_delete=models.CASCADE)

    # 用户id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    # 创建时间
    creat_time = models.DateTimeField(auto_now=datetime.datetime.now)

    class Meta:
        db_table = "study_message_new"
        app_label = "Common"
