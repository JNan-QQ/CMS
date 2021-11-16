import traceback
from django.core.paginator import Paginator, EmptyPage
from django.db import models
from django.db.models import Q
from account.models import User


class News(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 新闻标题
    title = models.CharField(max_length=100, null=True, blank=True)
    # 新闻内容
    content = models.TextField()
    # 创建时间
    create_time = models.DateField(auto_now=True)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 状态
    # 0:禁用  1：发布   2：热度
    status = models.PositiveIntegerField()
    # 类型
    news_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "cms_news"

    @staticmethod
    def add_news(data):

        try:
            news = News.objects.create(
                title=data['title'],
                content=data['content'],
                author=User.objects.get(id=data['author_id']),
                status=data['status'],
                news_type=data['news_type']
            )
            return {'ret': 0, 'news_id': news.id}
        except:
            return {'ret': 1, 'msg': '添加新闻失败！'}

    @staticmethod
    def modify_news(data):
        try:
            news_id = data['news_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                news = News.objects.get(id=news_id)
            except:
                return {
                    'ret': 1,
                    'msg': f'id 为`{news_id}`的新闻不存在'
                }

            if 'title' in data:
                news.title = data['title']
            if 'content' in data:
                news.content = data['content']
            if 'author' in data:
                news.author = data['author']
            if 'status' in data:
                news.status = data['status']
            if 'news_type' in data:
                news.news_type = data['news_type']

            # 注意，一定要执行save才能将修改信息保存到数据库
            news.save()
            return {'ret': 0}
        except:
            return {'ret': 1, 'msg': '修改新闻信息失败！'}

    @staticmethod
    def delete_news(data):
        news_id = data['news_id']

        try:
            # 根据 id 从数据库中找到相应的客户记录
            news = News.objects.get(id=news_id)
        except:
            return {
                'ret': 1,
                'msg': f'id 为`{news_id}`的用户不存在'
            }

        # delete 方法就将该记录从数据库中删除了
        news.delete()

        return {'ret': 0}

    @staticmethod
    def list_news(data):

        try:
            if data['news_type'] == 'ALL':
                qs = News.objects.values().order_by('-id')
            else:
                qs = News.objects.values().order_by('-id').filter(news_type=data['news_type'])
            if data['usertype'] != 1:
                qs = qs.filter(Q(status=1) | Q(status=2))

            # 要获取的第几页 # 每页要显示多少条记录
            pagenum = data.get('pagenum', None)
            pagesize = data.get('pagesize', None)
            if not pagesize or not pagenum:
                pagesize = 5
                pagenum = 1

            # 返回一个 QuerySet 对象 ，包含所有的表记录
            # qs = User.objects.values()

            # 使用分页对象，设定每页多少条记录
            pgnt = Paginator(qs, pagesize)

            # 从数据库中读取数据，指定读取其中第几页
            page = pgnt.page(pagenum)

            # 将 QuerySet 对象 转化为 list 类型
            retlist = list(page)

            # total指定了 一共有多少数据
            return {'ret': 0, 'retlist': retlist, 'total': pgnt.count}

        except:
            return {'ret': 2, 'msg': f'未知错误\n{traceback.format_exc()}'}


class Message(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 通知标题
    title = models.CharField(max_length=100, null=True, blank=True)
    # 通知内容
    content = models.TextField()
    # 创建时间
    create_time = models.DateField(auto_now=True)
    # 作者
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 状态
    # 0:禁用  1：发布   2：热度
    status = models.PositiveIntegerField()
    # 接收者
    receiver = models.ManyToManyField(User, through='cms_Message_User')

    class Meta:
        db_table = "cms_message"

    @staticmethod
    def add_message(data):

        try:
            message = Message.objects.create(
                title=data['title'],
                content=data['content'],
                author=User.objects.get(id=data['author_id']),
                status=data['status'],
                receiver=data['user_Objects']
            )
            return {'ret': 0, 'news_id': message.id}
        except:
            return {'ret': 1, 'msg': '添加通知失败！'}

    @staticmethod
    def modify_message(data):
        try:
            message_id = data['message_id']
            try:
                # 根据 id 从数据库中找到相应的客户记录
                message = Message.objects.get(id=message_id)
            except:
                return {
                    'ret': 1,
                    'msg': f'id 为`{message_id}`的新闻不存在'
                }

            if 'title' in data:
                message.title = data['title']
            if 'content' in data:
                message.content = data['content']
            if 'author' in data:
                message.author = User.objects.get(id=data['author_id'])
            if 'status' in data:
                message.status = data['status']
            if 'news_type' in data:
                message.receiver = data['user_Objects']

            # 注意，一定要执行save才能将修改信息保存到数据库
            message.save()
            return {'ret': 0}
        except:
            return {'ret': 1, 'msg': '修改通知信息失败！'}

    @staticmethod
    def delete_news(data):
        message_id = data['message_id']

        try:
            # 根据 id 从数据库中找到相应的客户记录
            message = Message.objects.get(id=message_id)
        except:
            return {
                'ret': 1,
                'msg': f'id 为`{message_id}`的用户不存在'
            }

        # delete 方法就将该记录从数据库中删除了
        message.delete()

        return {'ret': 0}

    @staticmethod
    def list_news(data):

        try:
            if data['news_type'] == 'ALL':
                qs = News.objects.values().order_by('-id')
            else:
                qs = News.objects.values().order_by('-id').filter(news_type=data['news_type'])
            if data['usertype'] != 1:
                qs = qs.filter(Q(status=1) | Q(status=2))

            # 要获取的第几页 # 每页要显示多少条记录
            pagenum = data.get('pagenum', None)
            pagesize = data.get('pagesize', None)
            if not pagesize or not pagenum:
                pagesize = 5
                pagenum = 1

            # 返回一个 QuerySet 对象 ，包含所有的表记录
            # qs = User.objects.values()

            # 使用分页对象，设定每页多少条记录
            pgnt = Paginator(qs, pagesize)

            # 从数据库中读取数据，指定读取其中第几页
            page = pgnt.page(pagenum)

            # 将 QuerySet 对象 转化为 list 类型
            retlist = list(page)

            # total指定了 一共有多少数据
            return {'ret': 0, 'retlist': retlist, 'total': pgnt.count}

        except:
            return {'ret': 2, 'msg': f'未知错误\n{traceback.format_exc()}'}
