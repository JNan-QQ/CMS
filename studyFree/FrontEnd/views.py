import json

from django.shortcuts import render

# Create your views here.
from Common.lib.shara import jsonResponse
from FrontEnd.models import Tags


class Article:
    def handler(self, request):
        # 将请求参数统一放入request 的 params 属性中，方便后续处理
        # GET请求 参数 在 request 对象的 GET属性中
        if request.method == 'GET':
            request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        elif request.method in ['POST', 'PUT', 'DELETE']:
            # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
            request.params = json.loads(request.body)

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']

        # 添加新闻
        if action == 'slideTags':
            return self.listSlideTags(request)
        elif action == 'contentTags':
            return self.listContentTags(request)

    @staticmethod
    def listSlideTags(request):
        data = ['tag']
        ret = Tags.list_tags(data)
        return jsonResponse(ret)

    @staticmethod
    def listContentTags(request):
        data = {'tage_id': request.params['tag_id']}
        ret = Tags.list_tags(data)
        return jsonResponse(ret)
