import json
import os.path
import traceback
from Common.lib.shara import jsonResponse
from FrontEnd.models import Tags, ArticleContent, NoteBook
from config import settings


class Article:
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
        if action == 'slideTags':
            return self.listSlideTags(request)
        elif action == 'contentTags':
            return self.listContentTags(request)
        elif action == 'markdownContent':
            return self.list_md_content(request)
        else:
            return jsonResponse({'ret': 1, "msg": 'action参数错误'})

    @staticmethod
    def listSlideTags(request):
        data = ['tag']
        ret = Tags.list_tags(data)
        return jsonResponse(ret)

    @staticmethod
    def listContentTags(request):
        data = {'tage_id': request.params['tag_id']}
        ret = Tags.list_tags(data)
        return jsonResponse(ret)

    @staticmethod
    def list_md_content(request):
        tag_id = request.params['tag_id']

        # noinspection PyBroadException
        try:
            filePathDict = ArticleContent.list({'tag_id': tag_id})
            filePath = os.path.join(settings.BASE_DIR, 'static', filePathDict['filePath'])
            if filePathDict:
                with open(filePath, 'r', encoding='utf8') as f:
                    mdContent = f.read()
                return jsonResponse({'ret': 0, 'mdContent': mdContent, 'title': filePathDict['tag_id__tag_name']})
            else:
                return jsonResponse({'ret': 0, 'mdContent': '没有找到该文章，请联系管理员添加！'})
        except:
            traceback.print_exc()
            return jsonResponse({'ret': 0, 'mdContent': '404'})


class Note:
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
        if action == 'addNoteBook':
            return self.addNoteBook(request)
        elif action == 'listNoteBook':
            return self.listNoteBook(request)
        elif action == 'deleteNoteBook':
            return self.deleteNoteBook(request)
        elif action == 'modifyNoteBook':
            return self.modifyNoteBook(request)
        else:
            return jsonResponse({'ret': 1, "msg": 'action参数错误'})

    @staticmethod
    def addNoteBook(request):
        try:
            user_id = request.session['user_id']
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '未登录，请先登录'})

        ret = NoteBook.add({'user_id': user_id})

        return jsonResponse(ret)

    @staticmethod
    def listNoteBook(request):
        try:
            user_id = request.session['user_id']
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '未登录，请先登录'})

        ret = NoteBook.list({'user_id': user_id})

        return jsonResponse(ret)

    @staticmethod
    def deleteNoteBook(request):
        try:
            user_id = request.session['user_id']
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '未登录，请先登录'})

        ret = NoteBook.delete_note({'user_id': user_id, 'note_id': request.params['note_id']})

        return jsonResponse(ret)

    @staticmethod
    def modifyNoteBook(request):
        try:
            request.params['user_id'] = request.session['user_id']
        except KeyError:
            return jsonResponse({'ret': 1, 'msg': '未登录，请先登录'})

        ret = NoteBook.modify(request.params)

        return jsonResponse(ret)
