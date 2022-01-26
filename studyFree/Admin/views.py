import json

from Common.lib.shara import jsonResponse
from Common.models import User


class Account:
    def handler(self, request):

        # 将请求参数统一放入request 的 params 属性中，方便后续处理
        # GET请求 参数 在 request 对象的 GET属性中
        if request.method == 'GET':
            request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        elif request.method in ['POST', 'PUT', 'DELETE']:
            # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
            request.params = json.loads(request.body)

        # 判断账号类型
        usertype = request.session.get('usertype', None)
        is_login = request.session.get('is_login', None)
        if usertype != 1 or not is_login:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号访问'})

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']
        if action == 'list':
            return self.list(request)
        elif action == 'modify':
            return self.modify(request)
        elif action == 'add':
            return self.add(request)
        elif action == 'delete':
            return self.delete(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def list(request):
        res = User.list_account(request.params)
        return jsonResponse(res)

    @staticmethod
    def modify(request):
        res = User.modify_account(request.params)
        return jsonResponse(res)

    @staticmethod
    def add(request):
        res = User.add_account(request.params)
        return jsonResponse(res)

    @staticmethod
    def delete(request):
        res = User.delete_account(request.params)
        return jsonResponse(res)
