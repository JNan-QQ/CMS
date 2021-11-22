import json
from shara.shara import jsonResponse
from .models import News as newsMgr
from .models import MessageReceiver, Message


class News:
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

        if action == 'add':
            return self.addNews(request)
        elif action == 'delete':
            return self.deleteNews(request)
        elif action == 'list':
            return self.listNews(request)
        elif action == 'modify':
            return self.modifyNews(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def addNews(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        request.params['author_id'] = request.session['user_id']

        ret = newsMgr.add_news(request.params)

        return jsonResponse(ret)

    @staticmethod
    def deleteNews(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        ret = newsMgr.delete_news(request.params)

        return jsonResponse(ret)

    @staticmethod
    def listNews(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        # if request.session['usertype'] != 1:
        #     return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        request.params['usertype'] = request.session['usertype']

        ret = newsMgr.list_news(request.params)

        return jsonResponse(ret)

    @staticmethod
    def modifyNews(request):
        # 判断是否登录
        if 'is_login' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)

        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})

        ret = newsMgr.modify_news(request.params)

        return jsonResponse(ret)


# class MessageR:
#     def handler(self, request):
#
#         # 将请求参数统一放入request 的 params 属性中，方便后续处理
#         # GET请求 参数 在 request 对象的 GET属性中
#         if request.method == 'GET':
#             request.params = request.GET
#
#         # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
#         elif request.method in ['POST', 'PUT', 'DELETE']:
#             # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
#             request.params = json.loads(request.body)
#
#         # 根据不同的action分派给不同的函数进行处理
#         action = request.params['action']
#
#         if action == 'add':
#             return self.addMessage(request)
#         elif action == 'delete':
#             return self.deleteMessage(request)
#         elif action == 'list':
#             return self.listMessage(request)
#         elif action == 'modify':
#             return self.modifyMessage(request)
#         else:
#             return jsonResponse({'ret': 1, 'msg': 'action参数错误'})
#
#     @staticmethod
#     def addMessage(request):
#         # 判断是否登录
#         if 'is_login' not in request.session:
#             return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)
#
#         if request.session['usertype'] != 1:
#             return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})
#
#         request.params['author_id'] = request.session['user_id']
#
#         ret = newsMgr.add_news(request.params)
#
#         return jsonResponse(ret)
#
#     @staticmethod
#     def deleteNews(request):
#         # 判断是否登录
#         if 'is_login' not in request.session:
#             return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)
#
#         if request.session['usertype'] != 1:
#             return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})
#
#         ret = newsMgr.delete_news(request.params)
#
#         return jsonResponse(ret)
#
#     @staticmethod
#     def listNews(request):
#         # 判断是否登录
#         if 'is_login' not in request.session:
#             return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)
#
#         # if request.session['usertype'] != 1:
#         #     return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})
#
#         request.params['usertype'] = request.session['usertype']
#
#         ret = newsMgr.list_news(request.params)
#
#         return jsonResponse(ret)
#
#     @staticmethod
#     def modifyNews(request):
#         # 判断是否登录
#         if 'is_login' not in request.session:
#             return jsonResponse({'ret': 302, 'msg': '未登录'}, status=302)
#
#         if request.session['usertype'] != 1:
#             return jsonResponse({'ret': 1, 'msg': '请使用管理员账号进行该操作！'})
#
#         ret = newsMgr.modify_news(request.params)
#
#         return jsonResponse(ret)
