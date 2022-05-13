import os.path
import traceback

from Common.lib.handler import dispatcherBase
from Common.lib.shara import jsonResponse, NOT_LOGIN, IS_LOGIN
from FrontEnd.models import Tags, ArticleContent, NoteBook
from Pay.models import PayConfig
from config import settings


class Article:
    def handler(self, request):
        Action2Handler = {
            'slideTags': self.listSlideTags,  # 文章类别标签
            'contentTags': self.listContentTags,  # 文章小结标签
            'markdownContent': self.list_md_content,  # 获取文章内容
        }

        return dispatcherBase(request, Action2Handler, NOT_LOGIN)

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
        ArticleContent.addClicks(tag_id)
        # noinspection PyBroadException
        try:
            filePathDict = ArticleContent.list({'tag_id': tag_id})
            filePath = os.path.join(settings.BASE_DIR, 'static', filePathDict['filePath'])
            if filePathDict:
                with open(filePath, 'r', encoding='utf8') as f:
                    mdContent = f.read()
                return jsonResponse({'ret': 0, 'mdContent': mdContent, 'title': filePathDict['tag_id__tag_name'],
                                     'author': filePathDict['user_id__username']})
            else:
                return jsonResponse({'ret': 0, 'mdContent': '没有找到该文章，请联系管理员添加！'})
        except:
            traceback.print_exc()
            return jsonResponse({'ret': 0, 'mdContent': '404'})


class Note:
    def handler(self, request):

        Action2Handler = {
            'addNoteBook': self.addNoteBook,  # 添加笔记
            'listNoteBook': self.listNoteBook,  # 获取笔记
            'deleteNoteBook': self.deleteNoteBook,  # 删除笔记
            'modifyNoteBook': self.modifyNoteBook,  # 修改笔记
        }

        return dispatcherBase(request, Action2Handler, IS_LOGIN)

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
