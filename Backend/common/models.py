from django.db import models
import random


# 名人名言
class CelebrityQuotes(models.Model):
    # 名言id
    id = models.BigAutoField(primary_key=True)
    # 名言内容
    content = models.CharField(max_length=100, null=True, blank=True)
    # 作者
    author = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "cms_celebrityQuotes"

    @staticmethod  # 随机列出已经名言
    def listQuotes():
        retlist = random.choice(list(CelebrityQuotes.objects.values()))
        # total指定了 一共有多少数据
        return {'ret': 0, 'retlist': retlist}
