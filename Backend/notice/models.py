import traceback

from django.core.paginator import Paginator
from django.db import models, transaction
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

    @staticmethod
    def pagenews():
        qs = News.objects.values('title', 'create_time', 'author__realName')
        retlist = list(qs)
        return {'ret': 0, 'retlist': retlist}


class NewsImg(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 新闻id
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    # 新闻图片
    img = models.ImageField(upload_to='images/',
                            null=True, blank=True)

    @staticmethod
    def list_img():
        qs = NewsImg.objects.values('news__title', 'img')
        # 将 QuerySet 对象 转化为 list 类型
        retlist = list(qs)

        # total指定了 一共有多少数据
        return {'ret': 0, 'retlist': retlist}


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

    class Meta:
        db_table = "cms_message"


class MessageReceiver(models.Model):
    id = models.BigAutoField(primary_key=True)
    # 通知id
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    # 作者id
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    # 接收者id
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    # status
    status = models.PositiveIntegerField()

    class Meta:
        db_table = "cms_receiver"

    @staticmethod
    def add_message(data):
        try:
            with transaction.atomic():
                message = Message.objects.create(
                    title=data['title'],
                    content=data['content'],
                    author=User.objects.get(id=data['author_id']),
                    status=data['status'],
                )
            for i in data['receiver_user_id']:
                MessageReceiver.objects.create(
                    message=message,
                    author=User.objects.get(id=data['author_id']),
                    receiver=User.objects.get(id=i),
                    status=1,
                )
            return {'ret': 0, 'message_id': message.id}
        except:
            return {'ret': 1, 'msg': '添加通知失败！'}

    @staticmethod
    def modify_message(data):
        try:
            with transaction.atomic():
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
                if 'status' in data:
                    message.status = data['status']
                if 'receiver_user_id' in data:
                    message_list = list(MessageReceiver.objects.values('receiver').filter(message=message_id))
                    for i in data['receiver_user_id']:
                        if i in message_list:
                            continue
                        else:
                            MessageReceiver.objects.create(
                                message=message,
                                author=User.objects.get(id=data['author_id']),
                                receiver=User.objects.get(id=i),
                                status=1,
                            )
                            message_list.remove(i)
                    if message_list:
                        for ii in message_list:
                            MessageReceiver.objects.get(receiver=ii).delete()
                # 注意，一定要执行save才能将修改信息保存到数据库
                message.save()
            return {'ret': 0}
        except:
            return {'ret': 1, 'msg': '修改通知信息失败！'}

    @staticmethod
    def check_message(data):
        message_id = data['message_id']
        user_id = data['user_id']
        try:
            # 根据 id 从数据库中找到相应的客户记录
            message_receiver = MessageReceiver.objects.filter(message=message_id, receiver=user_id)
        except:
            return {
                'ret': 1,
                'msg': f'id 为`{message_id}`的通知不存在'
            }
        message_receiver.status = 0
        message_receiver.save()

    @staticmethod
    def delete_message(data):
        message_id = data['message_id']

        try:
            # 根据 id 从数据库中找到相应的客户记录
            message = Message.objects.get(id=message_id)
        except:
            return {
                'ret': 1,
                'msg': f'id 为`{message_id}`的通知不存在'
            }

        # delete 方法就将该记录从数据库中删除了
        message.delete()

        return {'ret': 0}

    # @staticmethod
    # def list_message(data):
    #
    #     try:
    #         if data['usertype'] == 1:
    #             qs = Message.objects.values().order_by('-id')
    #         elif data['usertype'] == 10:
    #             qs = Message.objects.values().order_by('-id').filter(author=data['user_id'])
    #         elif data['usertype'] != 100:
    #             qs = Message.objects.values().order_by('-id').filter(receiver=data['user_id'])
    #
    #         # 要获取的第几页 # 每页要显示多少条记录
    #         pagenum = data.get('pagenum', None)
    #         pagesize = data.get('pagesize', None)
    #         if not pagesize or not pagenum:
    #             pagesize = 5
    #             pagenum = 1
    #
    #         # 返回一个 QuerySet 对象 ，包含所有的表记录
    #         # qs = User.objects.values()
    #
    #         # 使用分页对象，设定每页多少条记录
    #         pgnt = Paginator(qs, pagesize)
    #
    #         # 从数据库中读取数据，指定读取其中第几页
    #         page = pgnt.page(pagenum)
    #
    #         # 将 QuerySet 对象 转化为 list 类型
    #         retlist = list(page)
    #
    #         # total指定了 一共有多少数据
    #         return {'ret': 0, 'retlist': retlist, 'total': pgnt.count}
    #
    #     except:
    #         return {'ret': 2, 'msg': f'未知错误\n{traceback.format_exc()}'}
