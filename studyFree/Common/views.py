import datetime
import os
import time
import traceback

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from Admin.models import webConfig
from Common.forms import handle_uploaded_file, upLoadFile
from Common.lib.email_my import SendEmail
from Common.lib.handler import dispatcherBase
from Common.lib.mima import decipher
from Common.lib.shara import jsonResponse, generate_random_str, NOT_LOGIN, IS_LOGIN
from Common.models import CelebrityQuotes, User, EmailCode, Message, MessageNews
from Pay.models import PayConfig


class Login:
    def handler(self, request):
        Action2Handler = {
            'signin': self.signin,
            'signout': self.signout,
            'checkLogin': self.checkLogin,
            'register': self.register
        }

        return dispatcherBase(request, Action2Handler, NOT_LOGIN)

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

        res = User.add_account(data)

        self.signin(request)

        return jsonResponse(res)


class CQ:
    def handler(self, request):
        Action2Handler = {
            'list': self.list,
            'add': self.add,
            'listAll': self.listAll,
            'delete': self.delete_cq,
            'modify': self.modify
        }

        return dispatcherBase(request, Action2Handler, NOT_LOGIN)

    @staticmethod
    def list(request):
        ret = CelebrityQuotes.listQuotes()
        return jsonResponse(ret)

    @staticmethod
    def listAll(request):
        ret = CelebrityQuotes.listAll()
        return jsonResponse(ret)

    @staticmethod
    def add(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = CelebrityQuotes.add(request.params)
        return jsonResponse(res)

    @staticmethod
    def modify(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = CelebrityQuotes.modifyCq(request.params)
        return jsonResponse(res)

    @staticmethod
    def delete_cq(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = CelebrityQuotes.deleteCq(request.params)
        return jsonResponse(res)


class Download:
    def handler(self, request):

        Action2Handler = {
            'free': self.free
        }

        return dispatcherBase(request, Action2Handler, NOT_LOGIN)

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

        Action2Handler = {
            'qd': self.qd,  # 签到
            'emailCode': self.emailCode,  # 获取验证码
            'changePassword': self.changePassword,  # 修改密码 知道密码
            'resetPassword': self.resetPassword,  # 修改密码 不知道密码
            'changeUserInfo': self.changeUserInfo,  # 改变用户信息
            'uploadImg': self.uploadImg,  # 上传图片公共接口
            'listEmailAccount': self.listEmailAccount,  # 通过邮箱获取账号列表
            'list_webConfig': self.list_webConfig  # 部分网址配置
        }

        return dispatcherBase(request, Action2Handler, NOT_LOGIN)

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
        # File = request.FILES.get("file", None)
        file_type = request.POST['file_type']
        # file_name = request.POST['file_name']
        # file_name = file_name.replace('timeR', str(int(time.time())))
        # if File:
        #     f_path = os.path.join(settings.BASE_DIR, 'static/images', file_type, file_name)
        #     ret = handle_uploaded_file(request.FILES['file'], f_path)
        #     aviator_path = f'static/images/{file_type}/{file_name}'
        #     if ret:
        #         if file_type == 'aviator':
        #             User.modify_account({'user_id': request.session['user_id'], 'aviator': aviator_path})
        #         return jsonResponse({'ret': 0, 'url': aviator_path})
        #     else:
        #         return jsonResponse({'ret': 1, 'msg': '上传图像失败'})
        ret = upLoadFile.uploadImg(request)
        if file_type == 'aviator':
            User.modify_account({'user_id': request.session['user_id'], 'aviator': ret})
        return jsonResponse({'ret': 0, 'url': ret})

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
    def changeUserInfo(request):
        data = {'user_id': request.session['user_id']}

        if 'realName' in request.params:
            data['realName'] = request.params['realName']
        elif 'usertype' in request.params:
            if request.session['usertype'] != 1:
                data['usertype'] = 1005
            else:
                data['user_id'] = request.params['user_id']
                data['usertype'] = request.params['usertype']
        elif 'desc' in request.params:
            data['desc'] = request.params['desc']

        res = User.modify_account(data)

        return jsonResponse(res)

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

    @staticmethod
    def changePassword(request):
        try:
            user_id = request.session['user_id']
            userName = request.session['username']
            old_password = decipher(request.params['old_password'])
            new_password = decipher(request.params['new_password'])

            # 使用 Django auth 库里面的 方法校验用户名、密码
            user = authenticate(username=userName, password=old_password)
            # 如果能找到用户，并且密码正确
            if user is not None:
                res = User.modify_account({'user_id': user_id, 'password': new_password})
                return jsonResponse(res)
            else:
                return jsonResponse({'ret': 1, 'msg': '未找到该用户'})
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '参数错误！'})

    @staticmethod
    def list_webConfig(request):
        title = request.params['title']
        if title not in ['tools', 'pay']:
            return jsonResponse({'ret': 1, 'msg': '无权查看'})
        res = webConfig.list({'title': title})

        return jsonResponse(res)


# 通知
class MessageView:
    def handler(self, request):

        Action2Handler = {
            'list': self.list,  # 列出通知
            'add': self.add,  # 添加一个通知管理员操作
            'getOneMessage': self.getOneMessage,  # 获取通知内容 并 取消未读操作
            'modify': self.modify,  # 修改一个通知管理员操作
            'delete': self.deleteMessage,  # 删除通知
            'newMessageNum': self.newMessageNum,  # 获取未读消息个数
        }

        return dispatcherBase(request, Action2Handler, IS_LOGIN)

    @staticmethod
    def list(request):
        try:
            user_id = request.session['user_id']
            usertype = request.session['usertype']
            page_size = request.params.get('pageSize', 10)
            page_num = request.params.get('pageNum', 1)
            ret = Message.list(user_id, usertype, page_size, page_num)
            return jsonResponse(ret)
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '参数错误！'})

    @staticmethod
    def add(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = Message.add(request.params)
        return jsonResponse(res)

    @staticmethod
    def modify(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = Message.modify(request.params)
        return jsonResponse(res)

    @staticmethod
    def deleteMessage(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})
        res = Message.deleteMessage(request.params)
        return jsonResponse(res)

    @staticmethod
    def getOneMessage(request):
        user_id = request.session['user_id']
        message_id = request.params['message_id']
        res = MessageNews.deleteOne(user_id, message_id)
        return jsonResponse(res)

    @staticmethod
    def newMessageNum(request):
        user_id = request.session['user_id']
        num = MessageNews.objects.filter(user_id_id=user_id).count()
        return jsonResponse({'ret': 0, 'num': num})
