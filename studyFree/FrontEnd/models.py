from django.db import models


# Create your models here.
# 文章标签
class Tags(models.Model):
    # 标签id
    id = models.BigAutoField(primary_key=True)
    # 标签名称
    tag_name = models.CharField(max_length=100, null=True, blank=True)
    # 子标签id （链接自身标签）
    tag_id = models.IntegerField(null=True, blank=True)
    # 标签 type
    # 1:一级标签 | 2：二级标签 | 3：三级标签
    tage_type = models.PositiveIntegerField()

    # 标签 status
    # 1:正常 | 2：禁用
    status = models.PositiveIntegerField()

    class Meta:
        db_table = "study_tags"

    @staticmethod  # 随机列出已经名言
    def list_tags(data):
        if 'tag' in data:
            qs = Tags.objects.filter(tage_type=1, status=1).values('id', 'tag_name')
            qs = list(qs)
        else:
            qs = Tags.objects.filter(tag_id=data['tage_id'], status=1, tage_type=2).values('id', 'tag_name')
            qs = list(qs)
            for i in qs:
                qs_content = Tags.objects.filter(tag_id=i['id'], status=1, tage_type=3).values('id', 'tag_name')
                index = qs.index(i)
                qs[index]['content'] = list(qs_content)

        return {'ret': 0, 'retlist': qs}
