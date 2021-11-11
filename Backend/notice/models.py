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
    new_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "cms_news"

    @staticmethod
    def add_news(data):

        try:
            news = News.objects.create(
                title=data['title'],
                content=data['content'],
                author=data['id'],
                status=data['status'],
                new_type=data['new_type']
            )
            return {'ret': 0, 'news_id': news.id}
        except:
            return {'ret': 1, 'msg': '添加新闻失败！'}


