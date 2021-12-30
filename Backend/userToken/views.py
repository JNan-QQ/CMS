import datetime
import json
from .models import userToken
from shara.shara import jsonResponse
from django.contrib.auth import authenticate, login, logout
import time


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


    # 判断是否激活
    def activation(self, request):
        # 获取设备码 cpu + 主板
        code = request.params['code']
        if request.session['is_login']:
            # 判断设备激活状态
            machineCode = userToken.objects.filter(user__id=request.session['user_id']).values()[0]
            machineCode1 = machineCode.get('machineCode1')
            machineCode2 = machineCode.get('machineCode2')
            machineCode3 = machineCode.get('machineCode3')
            # 未激活设备尝试写入设备码
            if code not in [machineCode1, machineCode2, machineCode3]:
                data = {'user_id': request.session['user_id']}
                if not machineCode1:
                    data['machineCode1'] = code
                elif not machineCode2:
                    data['machineCode2'] = code
                elif not machineCode3:
                    data['machineCode3'] = code
                else:
                    return jsonResponse({'ret': 1, 'msg': '一个账号只能激活三套设备，请使用已激活的设备！'})

                res = userToken.modifyToken(data)
                print(res)
                if res['ret'] != 0:
                    return jsonResponse({'ret': 1, 'msg': '设备激活失败'})

            # 判断是否过期
            endTime = machineCode.get('endTime', None)
            if str(endTime) < datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"):
                return jsonResponse({'ret': 1, 'msg': '已过期'})

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
        list1 = list(str1)
        str2 = ''
        for i in list1:
            if i.isalpha():
                str2 += str(ord(i) - 64)
            else:
                str2 += i
        return str2
