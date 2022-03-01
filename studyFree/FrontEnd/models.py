import datetime
import traceback

from django.db import models
from django.db import transaction

from Common.models import User


# 文章标签
class Tags(models.Model):
    # 标签id
    id = models.BigAutoField(primary_key=True)
    # 标签名称
    tag_name = models.CharField(max_length=100, null=True, blank=True)
    # 子标签id （链接自身标签）
    tag_id = models.IntegerField(null=True, blank=True)
    # tag_id = models.ForeignKey('self', on_delete=models.CASCADE, blank=True)
    # 标签 type
    # 1:一级标签 | 2：二级标签 | 3：三级标签
    tag_type = models.PositiveIntegerField()

    # 标签 status
    # 1:正常 | 2：禁用
    status = models.PositiveIntegerField()

    class Meta:
        db_table = "study_tags"
        app_label = "FrontEnd"

    @staticmethod
    def admin_add(data):
        try:
            if data['tag_type'] == 1:
                data['tag_id'] = None
            with transaction.atomic():
                tag = Tags.objects.create(
                    tag_name=data['tag_name'],
                    tag_id=data['tag_id'],
                    tag_type=data['tag_type'],
                    status=data['status']
                )

                if data['tag_type'] == 3:
                    ArticleContent.objects.create(
                        tag_id_id=tag.id,
                        status=1
                    )

                return {'ret': 0, 'tag_id': tag.id}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '添加标签出错'}

    @staticmethod
    def list_tags(data):
        if 'tag' in data:
            qs = Tags.objects.filter(tag_type=1, status=1).values('id', 'tag_name')
            qs = list(qs)
        else:
            qs = Tags.objects.filter(tag_id=data['tage_id'], status=1, tag_type=2).values('id', 'tag_name')
            qs = list(qs)
            for i in qs:
                qs_content = Tags.objects.filter(tag_id=i['id'], status=1, tag_type=3).values('id', 'tag_name')
                index = qs.index(i)
                qs_content = list(qs_content)
                for ii in qs_content:
                    ret = ArticleContent.list({'tag_id': ii['id'], 'img': 0})
                    index1 = qs_content.index(ii)
                    qs_content[index1].update(ret)
                qs[index]['content'] = qs_content

        return {'ret': 0, 'retlist': qs}

    @staticmethod
    def admin_list():
        tags = Tags.objects.filter(tag_type=1).values('id', 'tag_name', 'status')
        tags = list(tags)
        for index, tag_one in enumerate(tags):
            tag2 = Tags.objects.filter(tag_id=tag_one['id'], tag_type=2).values('id', 'tag_name', 'status')
            tag2 = list(tag2)
            for index2, tag_two in enumerate(tag2):
                tag_3 = Tags.objects.filter(tag_id=tag_two['id'], tag_type=3).values('id', 'tag_name', 'status')
                tag_3 = list(tag_3)
                for index3, tag_three in enumerate(tag_3):
                    contentList = ArticleContent.objects.filter(tag_id__id=tag_three['id']).values()
                    if contentList:
                        tag_3[index3]['contentList'] = list(contentList)[0]
                    else:
                        tag_3[index3]['contentList'] = {}
                tag2[index2]['tag_child'] = tag_3
            tags[index]['tag_child'] = tag2
        return {'ret': 0, 'retlist': tags}

    @staticmethod
    def admin_modify(data):

        try:
            # 根据 id 从数据库中找到相应的记录
            tag = Tags.objects.get(id=data['id'])
        except:
            return {
                'ret': 1,
                'msg': '标签id不存在'
            }
        if 'tag_name' in data:
            tag.tag_name = data['tag_name']
        if 'tag_id' in data:
            tag.tag_id = data['tage_id']
        if 'tag_type' in data:
            tag.tag_type = data['tag_type']
        if 'status' in data:
            tag.status = data['status']

        tag.save()

        return {'ret': 0}

    @staticmethod
    def admin_delete(data):
        try:
            # 根据 id 从数据库中找到相应的客户记录
            tag = Tags.objects.get(id=data['id'])
        except:
            return {
                'ret': 1,
                'msg': f'标签不存在'
            }

        # delete 方法就将该记录从数据库中删除了
        tag.delete()

        return {'ret': 0}


class ArticleContent(models.Model):
    # 文章id
    id = models.BigAutoField(primary_key=True)
    # 3级标签id
    tag_id = models.ForeignKey(Tags, on_delete=models.CASCADE)
    # 标签 status
    # 1:正常 | 2：禁用
    status = models.PositiveIntegerField()
    # 展示图片
    images = models.CharField(max_length=100, null=True, blank=True, default='images/python-default.png')
    # markdown文件路径
    filePath = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "study_articleContent"
        app_label = "FrontEnd"

    @staticmethod
    def list(data):
        tag_id = data['tag_id']
        try:
            if 'img' in data:
                qs = ArticleContent.objects.filter(tag_id__id=tag_id, status=1).values('images')
            else:
                qs = ArticleContent.objects.filter(tag_id__id=tag_id, status=1).values('filePath', 'tag_id__tag_name')
            qs = list(qs)
            return qs[0]
        except:
            traceback.print_exc()
            return {}

    @staticmethod
    def admin_modify(data):

        try:
            # 根据 id 从数据库中找到相应的记录
            article = ArticleContent.objects.get(id=data['id'])
        except:
            return {
                'ret': 1,
                'msg': '标签id不存在'
            }

        if 'images' in data:
            article.images = data['images']
        if 'filePath' in data:
            article.filePath = data['filePath']

        article.save()

        return {'ret': 0}


class NoteBook(models.Model):
    # 笔记id
    id = models.BigAutoField(primary_key=True)
    # 标签 status
    # 1:正常 | 2：禁用
    status = models.PositiveIntegerField()
    # title
    title = models.CharField(max_length=100, null=True, blank=True, default='默认标题')
    # content
    content = models.TextField(null=True, blank=True, default='请在此输入内容，支持markdown语法')
    # time
    time = models.DateTimeField(auto_now=datetime.datetime.now)
    # user_id
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "study_notebook"
        app_label = "FrontEnd"

    @staticmethod
    def add(data):
        user_id = data['user_id']
        try:
            qs = NoteBook.objects.filter(user_id__id=user_id)
            if len(qs) == 10:
                return {'ret': 1, 'msg': '你已经拥有10个笔记，为了减轻服务器压力，暂时无法增加'}
            note = NoteBook.objects.create(
                user_id_id=user_id,
                status=1
            )
            return {'ret': 0, 'note_id': note.id}
        except:
            traceback.print_exc()
            return {'ret': 1, 'msg': '服务器错误！'}

    @staticmethod
    def list(data):
        try:
            qs = NoteBook.objects.filter(user_id__id=data['user_id'], status=1).values().order_by('-id')
            qs = list(qs)
            return {'ret': 0, 'retlist': qs}
        except:
            return {'ret': 1, 'msg': '获取笔记列表失败'}

    @staticmethod
    def delete_note(data):
        note_id = data['note_id']
        try:
            # 根据 id 从数据库中找到相应的客户记录
            note = NoteBook.objects.get(id=note_id)
        except:
            return {
                'ret': 1,
                'msg': f'id 为`{note_id}`的笔记不存在'
            }
        if note.user_id.id == data['user_id']:
            note.delete()
        return {'ret': 0}

    @staticmethod
    def modify(data):
        note_id = data['note_id']
        try:
            # 根据 id 从数据库中找到相应的客户记录
            note = NoteBook.objects.get(id=note_id)
        except:
            return {
                'ret': 1,
                'msg': f'id 为`{note_id}`的笔记不存在'
            }
        if note.user_id.id == data['user_id'] or data['usertype'] == 1:
            if 'title' in data:
                note.title = data['title']
            if 'content' in data:
                note.content = data['content']
            if 'status' in data:
                note.status = data['status']

            note.save()
            return {'ret': 0}
        return {'ret': 1, 'msg': '不能修改别人的笔记'}

    @staticmethod
    def admin_list():
        qs = NoteBook.objects.values('id', 'status', 'title', 'content', 'time', 'user_id__username')
        qs = list(qs)
        for i in range(len(qs)):
            qs[i]['time'] = qs[i]['time'].strftime('%Y-%m-%d %H:%M:%S')
        return {'ret': 0, 'retlist': qs}
