import json
from shara.shara import jsonResponse
from .models import User as userAccount


class Account:
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
        if action == 'register':
            return self.register(request)
        elif action == 'add':
            return self.addAccount(request)
        elif action == 'delete':
            return self.deleteAccount(request)
        elif action == 'list':
            return self.listAccount(request)
        elif action == 'modify':
            return self.modifyAccount(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def register(request):
        usertype = request.params.get('usertype')

        if usertype not in ['100', '1000', 100, 1000]:
            return jsonResponse({'ret': 1, 'msg': '你没有权限注册该类账号！'})

        ret = userAccount.add_account(request.params)

        return jsonResponse(ret)

    @staticmethod
    def addAccount(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        usertype = request.params.get('usertype')

        if usertype not in ['1', '100', '1000', 1, 100, 1000]:
            return jsonResponse({'ret': 1, 'msg': '账号类型不存在！'})

        ret = userAccount.add_account(request.params)

        return jsonResponse(ret)

    @staticmethod
    def deleteAccount(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        ret = userAccount.delete_account(request.params)

        return jsonResponse(ret)

    @staticmethod
    def listAccount(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        ret = userAccount.list_account(request.params)

        return jsonResponse(ret)

    @staticmethod
    def modifyAccount(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] == 1:
            ret = userAccount.modify_account(request.params)
            return jsonResponse(ret)

        else:
            if request.params['user_id'] != request.session['user_id']:
                return jsonResponse({'ret': 1, 'msg': '不能修改别人的信息！'})

            else:
                if 'studentNo' in request.params or 'gradeNo' in request.params or 'classNo' in request.params or 'major' in request.params:
                    return jsonResponse({'ret': 1, 'msg': '请联系管理员修改！'})

                ret = userAccount.modify_account(request.params)

                return jsonResponse(ret)
