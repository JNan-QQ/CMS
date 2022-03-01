import json

from django.db import models


class webConfig(models.Model):
    # id
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    # config
    config = models.TextField(default={})

    class Meta:
        db_table = "study_webConfig"
        app_label = "Admin"

    @staticmethod
    def list(data):
        if 'id' in data:
            qs = webConfig.objects.filter(id=data['id']).values()
        elif 'title' in data:
            qs = webConfig.objects.filter(title=data['title']).values()
        else:
            qs = webConfig.objects.values()

        qs = list(qs)

        return {'ret': 0, 'retlist': qs}

    @staticmethod
    def add(data):
        webConfig.objects.create(
            title=data['title'],
            config=json.dumps(data['config'])
        )
        return {'ret': 0}

    @staticmethod
    def modify(data):
        try:
            web = webConfig.objects.get(id=data['webConfig_id'])
        except:
            return {'ret': 1, 'msg': '未找到数据'}

        if 'title' in data:
            web.title = data['title']
        if 'config' in data:
            web.config = json.dumps(data['config'])

        web.save()

        return {'ret': 0}
