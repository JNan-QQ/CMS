import json
import os
import random
import string
import time

from django.conf import settings
from django.contrib.auth import authenticate, login, logout

from shara.shara import jsonResponse


# Create your views here.

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

                return jsonResponse(
                    {'ret': 0, 'usertype': user.usertype, 'user_id': user.id, 'realName': user.realName})
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
                                 'realName': request.session['realName'], 'aviator': request.session['aviator']})
        else:
            return jsonResponse({'ret': 302, 'msg': '未登录'})


class FilesUpDown:
    def handler(self, request):

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        if request.method == 'POST':
            # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
            action = request.POST['action']
        elif request.method == 'GET':
            action = request.GET['action']
        else:
            action = None

        # 根据不同的action分派给不同的函数进行处理
        if action == 'upload':
            return self.upload(request)
        elif action == 'download':
            return self.download(request)
        elif action == 'delete':
            return self.deleteFiles(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def upload(request, _in=False):
        """保存上传文件"""
        # 1.获取上传的文件
        files = request.FILES['files']

        # 2.判断文件类型
        files_name = files.name
        file_type = files_name.split('.')[-1]
        new_file_name = str(int(round(time.time() * 1000))) + '_' + ''.join(
            random.sample(string.ascii_letters + string.digits, 4)) + f'.{file_type}'
        print(files_name, file_type, new_file_name)

        # 3.创建文件
        if file_type in ['png', 'jpg', 'gif', 'jpeg']:
            save_path = f'{settings.MEDIA_ROOT}/images/{new_file_name}'
        else:
            save_path = f'{settings.MEDIA_ROOT}/files/{new_file_name}'
        with open(save_path, 'wb') as f:
            # 获取上传文件的内容并写到创建文件中
            # pic.chunks():分块的返回文件
            for content in files.chunks():
                f.write(content)

        # 4.返回响应
        if _in:
            return new_file_name
        else:
            return jsonResponse({'ret': 0, 'file_url': f'{settings.MEDIA_URL}images/{new_file_name}'})

    @staticmethod
    def download(request):
        pass

    @staticmethod
    def deleteFiles(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        filePath = request.GET['files_path']
        if os.path.exists(f'{settings.BASE_DIR}{filePath}'):
            os.remove(f'{settings.BASE_DIR}{filePath}')
