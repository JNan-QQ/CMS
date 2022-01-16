import json

from Common.lib.shara import jsonResponse
from Pay.models import PayConfig


class payConfig:
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
        if action == 'userConfig':
            return self.userConfig(request)

    @staticmethod
    def userConfig(request):
        if request.session.get('is_login', None):
            res = PayConfig.list({'user_id': request.session['user_id']})
            return jsonResponse(res)
        else:
            return jsonResponse({'ret': 0, 'retlist': []})
