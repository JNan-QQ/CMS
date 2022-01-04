import datetime
import json

from django.contrib.auth import authenticate, login, logout

from shara.ali.aliApi import aliPay as Ap
from shara.shara import jsonResponse
from .models import userToken, order, products, machineCodes


class user_Token:
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
        if action == 'signin':
            return self.signin(request)
        elif action == 'signout':
            return self.signout(request)
        elif action == 'machineCode':
            return self.activation(request)
        elif action == 'userInfo':
            return self.userInfo(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod  # 登录
    def signin(request):
        res = userToken.addUser(request.params)
        if res['ret'] == 0:
            # 从 HTTP POST 请求中获取用户名、密码参数
            userName = request.params.get('username')
            passWord = request.params.get('password')

            # 使用 Django auth 库里面的 方法校验用户名、密码
            user = authenticate(username=userName, password=passWord)

            # 如果能找到用户，并且密码正确
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # 在session中存入用户类型
                    request.session['usertype'] = user.usertype
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    return jsonResponse(
                        {'ret': 0, 'usertype': user.usertype, 'user_id': user.id, 'realName': user.realName})
                else:
                    return jsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

            # 否则就是用户名、密码有误
            else:
                return jsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})
        else:
            return jsonResponse(res)

    @staticmethod
    def signout(request):
        # 使用登出方法
        logout(request)
        return jsonResponse({'ret': 0})

    @staticmethod
    def userInfo(request):
        ret = userToken.listUser({'user_id': request.session['user_id']})
        ret1 = machineCodes.list_code({'user_id': request.session['user_id']})
        ret['retlist'].update(ret1)
        return jsonResponse(ret)

    # 判断是否激活
    def activation(self, request):
        # 获取设备码 cpu + 主板
        code = request.params['code']
        if request.session['is_login']:
            # 判断设备激活状态
            if not machineCodes.objects.filter(user__id=request.session['user_id'], machineCode=code).exists():
                res = machineCodes.add_code({'user_id': request.session['user_id'], 'machineCode': code})
                if res['ret'] == 1:
                    return jsonResponse(res)

            # 判断设备激活状态
            user_token = userToken.objects.filter(user__id=request.session['user_id']).values()[0]

            # 判断是否过期
            endTime = user_token.get('endTime', None)
            if str(endTime) < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
                return jsonResponse({'ret': 1, 'msg': '账号套餐已过期', 'activeCode': '', 'endTime': str(endTime)})

            # 还回校验码
            now_time = datetime.datetime.now().strftime("%Y%m%d%H%M")
            activeCode = code[0:2] + now_time[10:] + code[2:4] + now_time[6:8] + code[4:6] + now_time[0:2] + \
                         code[6:9] + now_time[8:10] + code[9:10] + now_time[2:4] + code[10:]
            activeCode = self.cipherTable(activeCode)

            return jsonResponse({'ret': 0, 'activeCode': activeCode, 'endTime': endTime})

        else:
            return jsonResponse({'ret': 1, 'msg': '未登录'})

    @staticmethod  # 密码表 A - Z = 1 - 26
    def cipherTable(str1):
        k = '105201314'
        k = k + k + k + k + k + k
        str2 = ''
        for i, j in zip(str1, k):
            if i.isalpha():
                str2 += str(ord(i) - 64 + ord(j))
            else:
                str2 += i
        return str2


class aliPayView:
    alipay = Ap()

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
        if action == 'createOrder':
            return self.alipay.createOrder(request)
        elif action == 'listOrder':
            return self.listOrder(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def listOrder(request):
        ret = order.list_order({'user_id': request.session['user_id'], 'usertype': request.session['usertype']})
        return jsonResponse(ret)


class Product:
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
        if action == 'listProducts':
            return self.listProducts(request)
        elif action == 'addProduct':
            return self.addProduct(request)
        elif action == 'modifyProduct':
            return self.modifyProduct(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def listProducts(request):
        ret = products.list_products({'usertype': request.session['usertype']})
        return jsonResponse(ret)

    @staticmethod
    def addProduct(request):
        ret = products.add_products(request.params)
        return jsonResponse(ret)

    @staticmethod
    def modifyProduct(request):
        ret = products.modify_products(request.params)
        return jsonResponse(ret)
