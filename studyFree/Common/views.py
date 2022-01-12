import json
import os

from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from .lib.shara import jsonResponse
from .models import CelebrityQuotes


class Login:
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
        elif action == 'checkLogin':
            return self.checkLogin(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def signin(request):
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
                request.session['realName'] = user.realName
                request.session['aviator'] = str(user.aviator)
                request.session['username'] = user.username

                return jsonResponse(
                    {'ret': 0, 'usertype': user.usertype, 'user_id': user.id, 'realName': user.realName,
                     'username': user.username})
            else:
                return jsonResponse({'ret': 0, 'msg': '用户已经被禁用'})

        # 否则就是用户名、密码有误
        else:
            return jsonResponse({'ret': 1, 'msg': '用户名或者密码错误'})

    @staticmethod
    def signout(request):
        # 使用登出方法
        logout(request)
        return jsonResponse({'ret': 0})

    @staticmethod
    def checkLogin(request):
        if request.session.get('is_login', False):
            return jsonResponse({'ret': 0, 'id': request.session['user_id'], 'usertype': request.session['usertype'],
                                 'realName': request.session['realName'], 'aviator': request.session['aviator'],
                                 'username': request.session['username']})
        else:
            return jsonResponse({'ret': 302, 'msg': '未登录'})


class CQ:
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
        if action == 'list':
            return self.list()

    @staticmethod
    def list():
        ret = CelebrityQuotes.listQuotes()
        return jsonResponse(ret)


class FileStream:
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
        if action == 'list':
            return self.list(request)

    @staticmethod
    def list(request):

        filetype = request.params['type']
        filePath = os.path.join(settings.BASE_DIR, 'static', filetype, request.params['filename'])
        try:
            with open(filePath, 'r', encoding='utf8') as f:
                mdContent = f.read()
            return jsonResponse({'ret': 0, 'mdContent': mdContent})
        except KeyError:
            return jsonResponse({'ret': 1})
