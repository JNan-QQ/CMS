import datetime
import json
import time
import traceback

from Common.lib.shara import jsonResponse
from Pay.ali.aliApi import aliPay
from Pay.models import PayConfig, Order, Products


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

        if action == 'userConfig':
            return self.userConfig(request)
        elif action == 'listServerConfig':
            return self.listServerConfig(request)
        elif action == 'listWebUrl':
            return self.listWebUrl(request)
        elif action == 'modify':
            return self.modify(request)
        elif action == 'checkActive':
            return self.checkActive(request)

    @staticmethod
    def userConfig(request):
        if request.session.get('is_login', None):
            res = PayConfig.list({'user_id': request.session['user_id']})
            return jsonResponse(res)
        else:
            return jsonResponse({'ret': 0, 'retlist': []})

    @staticmethod
    def listServerConfig(request):
        if request.session.get('is_login', None):
            if request.session['usertype'] not in [1, 1005]:
                return jsonResponse({'ret': 0, 'ServerConfig': ''})
            res = PayConfig.listServerConfig({'user_id': request.session['user_id']})
            return jsonResponse(res)
        else:
            return jsonResponse({'ret': 0, 'ServerConfig': ''})

    @staticmethod
    def listWebUrl(request):
        if request.session.get('is_login', None):
            if request.session['usertype'] not in [1, 1005]:
                return jsonResponse({'ret': 0, 'web_url': ''})
            res = PayConfig.listWebUrl({'user_id': request.session['user_id']})
            return jsonResponse(res)
        else:
            return jsonResponse({'ret': 0, 'web_url': ''})

    @staticmethod
    def modify(request):
        request.params['user_id'] = request.session['user_id']
        res = PayConfig.modify(request.params)

        return jsonResponse(res)

    @staticmethod
    def cipherTable():
        k = '105201314'
        str2 = ''
        str1 = str(time.time())[0:8]
        for i, j in zip(str1, k):
            if i.isalpha():
                str2 += str(ord(i) - 64 + ord(j))
            else:
                str2 += str(int(i) + int(j))
        return str2

    def checkActive(self, request):
        try:
            ret = PayConfig.list({'user_id': request.session['user_id']})
            if ret['ret'] == 0:
                deadline: datetime.datetime = ret['retlist'][0]['deadline']
                if deadline < datetime.datetime.now():
                    return jsonResponse({'ret': 1, 'msg': f'套餐服务已过期：{deadline.strftime("%Y-%m-%d %H:%M:%S")}'})
                else:
                    code = self.cipherTable()
                    return jsonResponse({'ret': 0, 'code': code})
            else:
                return jsonResponse(ret)
        except:
            traceback.print_exc()
            return jsonResponse({'ret': 1, 'msg': '未找到用户记录'})


class payOrder:
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

        if action == 'list':
            return self.listOrder(request)
        elif action == 'add':
            return self.addOrder(request)
        elif action == 'modify':
            return self.modifyOrder(request)
        elif action == 'createOrder':
            return aliPay().createOrder(request)

    @staticmethod
    def listOrder(request):
        try:
            user_id = request.session['user_id']
            usertype = request.session['usertype']
            ret = Order.list_order({'user_id': user_id, 'usertype': usertype})
            return jsonResponse(ret)
        except:
            traceback.print_exc()
            return jsonResponse({'ret': 1, 'msg': '未登陆'})

    @staticmethod
    def modifyOrder(request):
        pass

    @staticmethod
    def addOrder(request):
        pass


class payProduct:
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

        if action == 'list':
            return self.listProduct(request)
        elif action == 'addTime':
            return self.addTime(request)

    @staticmethod
    def listProduct(request):
        res = Products.list_products({'usertype': request.session['usertype']})
        return jsonResponse(res)

    @staticmethod
    def addTime(request):
        product_id = request.params['product_id']
        product = Products.objects.get(id=product_id)
        res = PayConfig.modify({'user_id': request.session['user_id'], 'coins': -product.price, 'exp': product.price,
                                'addDays': product.timeDays})
        return jsonResponse(res)
