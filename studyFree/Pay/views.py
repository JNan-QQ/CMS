import datetime
import json
import time
import traceback

from Common.lib.handler import dispatcherBase
from Common.lib.shara import jsonResponse, NOT_LOGIN, IS_LOGIN
from Pay.ali.aliApi import aliPay
from Pay.models import PayConfig, Order, Products, cdkUser


class payConfig:
    def handler(self, request):
        Action2Handler = {
            'userConfig': self.userConfig,  # 获取用户pay信息
            'listServerConfig': self.listServerConfig,  # 获取用户服务器配置
            'listWebUrl': self.listWebUrl,  # 获取url
            'modify_config': self.modify_config,  # 修改用户服务器配置
            'modify_webUrl': self.modify_webUrl,  # 修改用户链接配置
            'checkActive': self.checkActive  # 检查是否激活
        }

        return dispatcherBase(request, Action2Handler, NOT_LOGIN)

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
                return jsonResponse({'ret': 0, 'userServerConfig': ''})
            res = PayConfig.listServerConfig({'user_id': request.session['user_id']})
            return jsonResponse(res)
        else:
            return jsonResponse({'ret': 0, 'userServerConfig': ''})

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
    def modify_webUrl(request):
        try:
            web_url = request.params['web_url']
            user_id = request.session['user_id']
            res = PayConfig.modify({'user_id': user_id, 'web_url': web_url})
            return jsonResponse(res)
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '参数错误'})

    @staticmethod
    def modify_config(request):
        try:
            user_id = request.session['user_id']
            userServerConfig = request.params['userServerConfig']
            res = PayConfig.modify({'user_id': user_id, 'userServerConfig': userServerConfig})
        except KeyError:
            res = {'ret': 1, 'msg': '请先登录'}

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
        Action2Handler = {
            'list': self.listOrder,  # 列出订单
            'createOrder': aliPay().createOrder,  # 创建一个订单
        }

        return dispatcherBase(request, Action2Handler, NOT_LOGIN)

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


class payProduct:
    def handler(self, request):
        Action2Handler = {
            'list': self.listProduct,  # 获取用户pay信息
            'addTime': self.addTime,  # 获取用户服务器配置
        }

        return dispatcherBase(request, Action2Handler, IS_LOGIN)

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


class cdk_view:
    def handler(self, request):
        Action2Handler = {
            'useCdk': self.useCdk,  # 获取用户pay信息
        }

        return dispatcherBase(request, Action2Handler, IS_LOGIN)

    @staticmethod
    def useCdk(request):
        res = cdkUser.add({'cdk': request.params['cdk'], 'user_id': request.session['user_id']})
        return jsonResponse(res)
