import datetime
import json
import os
import time

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.db.models import Q

from Pay.models import PayConfig
from .forms import handle_uploaded_file
from .lib.email_my import SendEmail
from .lib.shara import jsonResponse, generate_random_str
from .models import CelebrityQuotes, User, EmailCode


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
        elif action == 'register':
            return self.register(request)
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
                # 登录之后获取获取最新的session_key
                session_key = request.session.session_key
                # 删除非当前用户session_key的记录
                for session in Session.objects.filter(~Q(session_key=session_key),
                                                      expire_date__gte=datetime.datetime.now()):
                    data = session.get_decoded()
                    if data.get('_auth_user_id', None) == str(request.user.id):
                        session.delete()

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

    @staticmethod
    def register(request):
        email = request.params['email']
        code = request.params['code']
        res = EmailCode.checkCode(email, code)

        if res['ret'] == 1:
            return jsonResponse(res)
        data = {
            'username': request.params['username'],
            'password': request.params['password'],
            'email': request.params['email'],
            'usertype': 1000,
            'realName': ''
        }
        res = User.add_account(data)
        if res['ret'] == 1:
            return jsonResponse(res)

        user_id = res['id']
        res1 = PayConfig.add({'user_id': user_id})

        Login.signin(request)

        return jsonResponse(res1)


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


class Download:
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
        if action == 'free':
            return self.free(request)

    @staticmethod
    def free(request):
        try:
            price = request.params['price']
            res = PayConfig.modify(
                {'user_id': request.session['user_id'], 'coins': -int(price), 'exp': 10 * int(price)})
            return jsonResponse(res)
        except:
            return jsonResponse({'ret': 1, 'msg': '请先登录，再下载文章'})


class Others:
    def handler(self, request):

        action = None
        # 将请求参数统一放入request 的 params 属性中，方便后续处理
        # GET请求 参数 在 request 对象的 GET属性中
        if request.method == 'GET':
            request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        elif request.method in ['POST', 'PUT', 'DELETE']:
            # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
            try:
                request.params = json.loads(request.body)
            except:
                action = request.POST['action']

        # 根据不同的action分派给不同的函数进行处理
        if not action:
            action = request.params['action']

        # 添加新闻
        if action == 'qd':
            return self.qd(request)
        elif action == 'emailCode':
            return self.emailCode(request)
        elif action == 'uploadImg':
            return self.uploadImg(request)

    @staticmethod
    def qd(request):
        res = PayConfig.modify({'user_id': request.session['user_id'], 'exp': 500, 'coins': 50, 'qd': True})
        return jsonResponse(res)

    @staticmethod
    def emailCode(request):
        code = generate_random_str()
        res = SendEmail.sendEmail('【studyfree】 注册验证', f'你本次注册的六位验证码为：-> {code} <-,五分钟内有效。', [request.params['email']])
        if not res:
            return jsonResponse({'ret': 1, 'msg': '验证码邮件发送失败，请稍后重试'})
        res = EmailCode.add({'email': request.params['email'], 'code': code})
        return jsonResponse(res)

    @staticmethod
    def uploadImg(request):
        File = request.FILES.get("file", None)
        file_type = request.POST['file_type']
        file_name = request.POST['file_name']
        file_name = file_name.replace('timeR', str(int(time.time())))
        if File:
            f_path = os.path.join(settings.BASE_DIR, 'static/images', file_type, file_name)
            handle_uploaded_file(request.FILES['file'], f_path)
            return jsonResponse({'ret': 0, 'url': f'static/images/{file_type}/{file_name}'})
