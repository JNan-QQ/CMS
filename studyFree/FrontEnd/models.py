import datetime
import glob
import os.path
import traceback
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db import transaction

from Common.models import User
# 文章标签
from config.settings import BASE_DIR


class Tags(models.Model):
    # 标签id
    id = models.BigAutoField(primary_key=True)
    # 标签名称
    tag_name = models.CharField(max_length=100, null=True, blank=True)
    # 子标签id （链接自身标签）
    tag_id = models.IntegerField(null=True, blank=True)
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
        # noinspection PyBroadException
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
                        status=1,
                        user_id_id=1,
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
            for index, item in enumerate(qs):
                qs_content = Tags.objects.filter(tag_id=item['id'], status=1, tag_type=3).values('id', 'tag_name')
                qs_content = list(qs_content)
                for index1, item1 in enumerate(qs_content):
                    ret = ArticleContent.list({'tag_id': item1['id'], 'img': 0})
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
        except ObjectDoesNotExist:
            return {'ret': 1, 'msg': '未查询到标签对应的数据'}
        except KeyError:
            return {'ret': 1, 'msg': '请输入标签id'}
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
        except ObjectDoesNotExist:
            return {'ret': 1, 'msg': f'未查询到标签对应的数据'}
        except KeyError:
            return {'ret': 1, 'msg': '请输入标签id'}

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
    # 点击量
    clicks = models.IntegerField(default=0)
    # 作者
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "study_articleContent"
        app_label = "FrontEnd"

    @staticmethod
    def list(data):
        # noinspection PyBroadException
        try:
            tag_id = data['tag_id']
            if 'img' in data:
                qs = ArticleContent.objects.filter(tag_id__id=tag_id, status=1) \
                    .values('images', 'clicks', 'user_id__realName')
            else:
                qs = ArticleContent.objects.filter(tag_id__id=tag_id, status=1) \
                    .values('filePath', 'tag_id__tag_name', 'user_id__realName')
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
        except ObjectDoesNotExist:
            return {'ret': 1, 'msg': '标签id未查询到对应数据'}
        except KeyError:
            return {'ret': 1, 'msg': '请输入标签id'}

        if 'images' in data:
            article.images = data['images']
        if 'filePath' in data:
            article.filePath = data['filePath']
        if 'user_id' in data:
            article.user_id_id = data['user_id']

        article.save()

        return {'ret': 0}

    @staticmethod
    def addClicks(tag_id):
        try:
            # 根据 id 从数据库中找到相应的记录
            article = ArticleContent.objects.get(tag_id__id=tag_id)
            article.clicks += 1

            article.save()

            return {'ret': 0}
        except ObjectDoesNotExist:
            return {'ret': 1, 'msg': '标签id未查询到对应数据'}
        except KeyError:
            return {'ret': 1, 'msg': '请输入标签id'}


class NoteBook(models.Model):
    # 笔记id
    id = models.BigAutoField(primary_key=True)
    # 标签 status
    # 1:正常 | 2：禁用
    status = models.PositiveIntegerField()
    # title
    title = models.CharField(max_length=100, null=True, blank=True, default='默认标题')
    # content
    content = models.TextField(null=True, blank=True, default='请在此输入内容，支持markdown语法，不要输入保密信息！')
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
        # noinspection PyBroadException
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
        # noinspection PyBroadException
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
        except ObjectDoesNotExist:
            return {
                'ret': 1,
                'msg': f'id 为`{note_id}`的笔记不存在'
            }
        if note.user_id.id == data['user_id']:
            note.delete()

        # 删除笔记里的图片存储
        for note_img in glob.glob(os.path.join(BASE_DIR, 'static/images/notebook', f'img_notebook_{note_id}_*.png')):
            os.remove(note_img)

        return {'ret': 0}

    @staticmethod
    def modify(data):
        note_id = data['note_id']
        try:
            # 根据 id 从数据库中找到相应的客户记录
            note = NoteBook.objects.get(id=note_id)
        except ObjectDoesNotExist:
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
        try:
            qs = NoteBook.objects.values('id', 'status', 'title', 'content', 'time', 'user_id__username')
            qs = list(qs)
            for i in range(len(qs)):
                qs[i]['time'] = qs[i]['time'].strftime('%Y-%m-%d %H:%M:%S')
            return {'ret': 0, 'retlist': qs}
        except Exception as e:
            print(e)


class Skill(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)
    # title
    title = models.CharField(max_length=100, null=True, blank=True, default='默认标题')
    # content
    content = models.TextField(null=True, blank=True, default='请在此输入内容，支持markdown语法，不要输入保密信息！')
    # time
    time = models.DateTimeField(auto_now=datetime.datetime.now)
    # author
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 点击量
    clicks = models.IntegerField(default=0)
    # 评分
    rate = models.DecimalField(default=3.0, max_digits=2, decimal_places=1)
    # status
    # 0 禁用，1 正常,2 暂存，3 待审核
    status = models.PositiveIntegerField(default=2)
    # 收藏数
    collection = models.IntegerField(default=0)

    class Meta:
        db_table = "study_skill"
        app_label = "FrontEnd"

    @staticmethod
    def add(data):
        skill = Skill.objects.create(
            author_id=data['user_id'],
            title=data['title'],
            content=data['content'],
            status=data['status']
        )
        return {'ret': 0, 'skill_id': skill.id}

    @staticmethod
    def modify(data):
        user_id = data['user_id']
        skill_id = data['skill_id']

        if Skill.objects.filter(author_id=user_id, id=skill_id).exists():
            skill = Skill.objects.filter(author_id=user_id, id=skill_id).get()
            skill.title = data['title']
            skill.content = data['content']
            skill.status = data['status']
            skill.save()
            return {'ret': 0}
        else:
            return {'ret': 1, 'msg': '参数错误'}

    @staticmethod
    def deleteSkill(data):
        user_id = data['user_id']
        skill_id = data['skill_id']
        print(user_id,skill_id)
        if Skill.objects.filter(author_id=user_id, id=skill_id).exists():
            Skill.objects.filter(author_id=user_id, id=skill_id).delete()
            return {'ret': 0}
        else:
            return {'ret': 1, 'msg': '参数错误'}

    @staticmethod
    def list(data):
        # 获取用户id，未登录为none
        user_id = data['user_id']

        # 确定排序方法
        if data['mode'] == 'all':
            order_by_mode = '-time'
        else:
            order_by_mode = '-clicks'

        if data['mode'] == 'my-collection':
            qs = list(Skill.objects.filter(status=1, skill_collection_user__user__id=user_id).values(
                'id', 'title', 'time', 'author__aviator', 'rate', 'clicks', 'author__realName').order_by(order_by_mode))
            for index, item in enumerate(qs):
                qs[index]['isCollect'] = True
        elif data['mode'] == 'myself':
            qs = list(Skill.objects.filter(author__id=user_id).values('id', 'title', 'time', 'rate', 'clicks', 'status',
                                                                      'collection'))
        else:
            qs = list(Skill.objects.filter(status=1).values('id', 'title', 'time', 'author__aviator', 'rate', 'clicks',
                                                            'author__realName').order_by(order_by_mode))
            if user_id:
                collection_list = [i['skill_id'] for i in
                                   list(Collection.objects.filter(user_id=user_id).values('skill_id'))]
                for index, item in enumerate(qs):
                    qs[index]['isCollect'] = item['id'] in collection_list

        return {'ret': 0, 'retlist': qs}

    @staticmethod
    def listAdmin(data):
        pass

    @staticmethod
    def get_content(data):
        skill_id = data['skill_id']
        user_id = data['user_id']
        skill = list(Skill.objects.filter(id=skill_id).values('title', 'content', 'id'))[0]
        if user_id:
            rate = Rate.objects.filter(user_id=user_id, skill_id=skill_id).values('rate')
            if rate:
                skill['rate'] = rate[0]['rate']
            else:
                skill['rate'] = 0
        return {'ret': 0, 'retlist': skill}


class Rate(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)
    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # skill
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill_rate_user')
    #
    rate = models.DecimalField(default=3.0, max_digits=2, decimal_places=1)

    class Meta:
        db_table = "study_skill_rate"
        app_label = "FrontEnd"

    @staticmethod
    def add(data):
        user_id = data['user_id']
        skill_id = data['skill_id']
        try:
            if user_id and skill_id and not Rate.objects.filter(user_id=user_id, skill_id=skill_id).exists():
                Rate.objects.create(
                    user_id=user_id,
                    skill_id=skill_id,
                    rate=data['rate']
                )
            else:
                return {'ret': 1, 'msg': '参数错误'}
        except:
            traceback.print_exc()

    @staticmethod
    def modify(data):
        user_id = data['user_id']
        skill_id = data['skill_id']
        if user_id and skill_id:
            try:
                rate = Rate.objects.filter(user_id=user_id, skill_id=skill_id).get()
                rate.rate = data['rate']
                rate.save()
                return {'ret': 0}
            except ObjectDoesNotExist:
                ret = Rate.add(data)
                traceback.print_exc()
                return ret
        else:
            return {'ret': 1, 'msg': '参数错误'}


class Collection(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)
    # user
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # skill
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill_collection_user')

    class Meta:
        db_table = "study_skill_collection"
        app_label = "FrontEnd"

    @staticmethod
    def changeCollection(data):
        user_id = data.get('user_id', None)
        skill_id = data.get('skill_id', None)
        if user_id and skill_id:
            if Collection.objects.filter(user_id=user_id, skill_id=skill_id).exists():
                Collection.objects.filter(user_id=user_id, skill_id=skill_id)[0].delete()
            else:
                Collection.objects.create(
                    user_id=user_id,
                    skill_id=skill_id
                )
            return {'ret': 0}
        else:
            return {'ret': 1, 'msg': '参数错误'}
