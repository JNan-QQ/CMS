import datetime
import json
import os
import time
import traceback

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from Common.forms import handle_uploaded_file
from Common.lib.email_my import SendEmail
from Common.lib.mima import decipher
from Common.lib.shara import jsonResponse, generate_random_str
from Common.models import CelebrityQuotes, User, EmailCode
from Pay.models import PayConfig


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
        passWord = decipher(request.params.get('password'))

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
                request.session['email'] = user.email

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
            user = User.objects.get(id=request.session['user_id'])
            request.session['usertype'] = user.usertype
            request.session['realName'] = user.realName
            request.session['aviator'] = str(user.aviator)
            request.session['username'] = user.username
            request.session['email'] = user.email
            return jsonResponse({'ret': 0, 'id': request.session['user_id'], 'usertype': request.session['usertype'],
                                 'realName': request.session['realName'], 'aviator': request.session['aviator'],
                                 'username': request.session['username'], 'email': request.session['email']})
        else:
            return jsonResponse({'ret': 302, 'msg': '未登录'})

    def register(self, request):
        email = request.params['email']
        code = request.params['code']
        res = EmailCode.checkCode(email, code)

        if res['ret'] == 1:
            return jsonResponse(res)
        data = {
            'username': request.params['username'],
            'password': decipher(request.params['password']),
            'email': request.params['email'],
            'usertype': 1000,
            'realName': ''
        }
        print(data)
        res = User.add_account(data)

        self.signin(request)

        return jsonResponse(res)


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
        if action == 'add':
            return self.add(request)
        if action == 'listAll':
            return self.listAll()
        if action == 'delete':
            return self.delete_cq(request)

    @staticmethod
    def list():
        ret = CelebrityQuotes.listQuotes()
        return jsonResponse(ret)

    @staticmethod
    def listAll():
        ret = CelebrityQuotes.listAll()
        return jsonResponse(ret)

    @staticmethod
    def add(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = CelebrityQuotes.add(request.params)
        return jsonResponse(res)

    @staticmethod
    def delete_cq(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = CelebrityQuotes.deleteCq(request.params)
        return jsonResponse(res)


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
        # noinspection PyBroadException
        try:
            price = request.params['price']
            res = PayConfig.modify(
                {'user_id': request.session['user_id'], 'coins': -abs(int(price)), 'exp': 10 * int(price)})
            return jsonResponse(res)
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '请先登录，再下载文章'})
        except:
            traceback.print_exc()
            return jsonResponse({'ret': 1, 'msg': '其他异常'})


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
            # noinspection PyBroadException
            try:
                request.params = json.loads(request.body)
            except:
                action = request.POST['action']

        # 根据不同的action分派给不同的函数进行处理
        if not action:
            action = request.params['action']

        # 签到
        if action == 'qd':
            return self.qd(request)
        # 获取邮箱验证码
        elif action == 'emailCode':
            return self.emailCode(request)
        # 核对邮箱验证码
        elif action == 'checkEmailCode':
            return self.checkEmailCode(request)
        # 重置密码
        elif action == 'resetPassword':
            return self.resetPassword(request)
        # 上传图片公共接口
        elif action == 'uploadImg':
            return self.uploadImg(request)
        # 通过邮箱获取账号列表
        elif action == 'listEmailAccount':
            return self.listEmailAccount(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def qd(request):
        res = PayConfig.modify({'user_id': request.session['user_id'], 'exp': 500, 'coins': 50, 'qd': True})
        return jsonResponse(res)

    @staticmethod
    def emailCode(request):
        # 获取信息
        code = generate_random_str()
        email = request.params.get('email', None)
        email_type = request.params.get('email_type', None)
        username = ''
        if not email:
            try:
                email = request.session['email']
                username = request.session['username']
            except KeyError:
                return jsonResponse({'ret': 1, 'msg': '请填写正确的邮箱'})
        res = EmailCode.add({'email': email, 'code': code})
        if res['ret'] == 1:
            return jsonResponse(res)
        res1 = SendEmail.sendEmail(email_type=email_type, receivers=[email], username=username, code=code)
        if not res1:
            return jsonResponse({'ret': 1, 'msg': '验证码邮件发送失败，请稍后重试'})
        return jsonResponse(res)

    @staticmethod
    def uploadImg(request):
        File = request.FILES.get("file", None)
        file_type = request.POST['file_type']
        file_name = request.POST['file_name']
        file_name = file_name.replace('timeR', str(int(time.time())))
        if File:
            f_path = os.path.join(settings.BASE_DIR, 'static/images', file_type, file_name)
            ret = handle_uploaded_file(request.FILES['file'], f_path)
            aviator_path = f'static/images/{file_type}/{file_name}'
            if ret:
                if file_type == 'aviator':
                    User.modify_account({'user_id': request.session['user_id'], 'aviator': aviator_path})
                return jsonResponse({'ret': 0, 'url': aviator_path})
            else:
                return jsonResponse({'ret': 1, 'msg': '修改头像失败'})

    @staticmethod
    def checkEmailCode(request):
        email = request.session['email']
        ret = EmailCode.checkCode(email, request.params['code'])
        return jsonResponse(ret)

    @staticmethod
    def resetPassword(request):
        email = request.params['email']
        code = request.params['code']
        username = request.params['username']
        password = request.params['password']
        ret = EmailCode.checkCode(email, code)
        if ret['ret'] == 0:
            try:
                user = User.objects.get(username=username, email=email)
                ret = User.modify_account({'user_id': user.id, 'password': password})
            except ObjectDoesNotExist:
                return jsonResponse({'ret': 1, 'msg': '未找到邮箱对应账号'})
        return jsonResponse(ret)

    @staticmethod
    def listEmailAccount(request):
        try:
            email = request.params['email']
            code = request.params['code']
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '邮箱信息获取失败'})
        if not EmailCode.objects.filter(email=email, code=code, status=1).exists():
            return jsonResponse({'ret': 1, 'msg': '邮箱验证失败，请重试'})
        res = User.list_account({'search_items': {'email': email}})
        usernameList = []
        for i in res['retlist']:
            usernameList.append(i['username'])

        return jsonResponse({'ret': 0, 'usernameList': usernameList})


class Accounts:
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
        if action == 'modify':
            return self.modify_account(request)

    @staticmethod
    def modify_account(request):
        try:
            user_id = request.session['user_id']
            usertype = request.session['usertype']
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '请先登录'})
        if usertype != 1 and 'usertype' in request.params:
            request.params['usertype'] = 1005
        request.params['user_id'] = user_id
        ret = User.modify_account(request.params)

        return jsonResponse(ret)
