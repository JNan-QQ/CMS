import json
import os
import shutil
import time
import traceback

from Admin.models import webConfig
from Common.forms import handle_uploaded_file
from Common.lib.shara import jsonResponse
from Common.models import User
from FrontEnd.models import Tags, ArticleContent, NoteBook
from Pay.models import Order, PayConfig
from config.settings import BASE_DIR


class WebConfigs:
    def handler(self, request):

        # 将请求参数统一放入request 的 params 属性中，方便后续处理
        # GET请求 参数 在 request 对象的 GET属性中
        if request.method == 'GET':
            request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        elif request.method in ['POST', 'PUT', 'DELETE']:
            # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
            request.params = json.loads(request.body)

        # 判断账号类型
        usertype = request.session.get('usertype', None)
        is_login = request.session.get('is_login', None)
        if usertype != 1 or not is_login:
            if request.params['action'] != 'admin_list_webConfig':
                return jsonResponse({'ret': 1, 'msg': '请使用管理员账号访问'})

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']
        if action == 'admin_list_webConfig':
            return self.admin_list_webConfig(request)
        elif action == 'admin_add_webConfig':
            return self.admin_add_webConfig(request)
        elif action == 'admin_modify_webConfig':
            return self.admin_modify_webConfig(request)

    @staticmethod
    def admin_list_webConfig(request):
        res = webConfig.list(request.params)
        return jsonResponse(res)

    @staticmethod
    def admin_add_webConfig(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '不是管理员'})
        res = webConfig.add(request.params)
        return jsonResponse(res)

    @staticmethod
    def admin_modify_webConfig(request):
        if request.session['usertype'] != 1:
            return jsonResponse({'ret': 1, 'msg': '不是管理员'})
        res = webConfig.modify(request.params)
        return jsonResponse(res)


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

        # 判断账号类型
        usertype = request.session.get('usertype', None)
        is_login = request.session.get('is_login', None)
        if usertype != 1 or not is_login:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号访问'})

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']
        if action == 'list':
            return self.list(request)
        elif action == 'modify':
            return self.modify(request)
        elif action == 'add':
            return self.add(request)
        elif action == 'delete':
            return self.delete(request)
        elif action == 'modify_payconfig':
            return self.modify_payconfig(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def list(request):
        res = User.list_account(request.params)
        user_info = []
        if res['ret'] == 0:
            try:
                for i in res['retlist']:
                    ret = PayConfig.list({'user_id': i['id']})
                    if ret['ret'] == 0:
                        i.update(ret['retlist'][0])
                        user_info.append(i)
                res['retlist'] = user_info
            except:
                traceback.print_exc()
        return jsonResponse(res)

    @staticmethod
    def modify(request):
        res = User.modify_account(request.params)
        return jsonResponse(res)

    @staticmethod
    def add(request):
        res = User.add_account(request.params)
        # user_id = res['id']
        # res1 = PayConfig.add({'user_id': user_id})
        return jsonResponse(res)

    @staticmethod
    def delete(request):
        res = User.delete_account(request.params)
        return jsonResponse(res)

    @staticmethod
    def modify_payconfig(request):
        ret = PayConfig.modify(request.params)
        return jsonResponse(ret)


class Orders:
    def handler(self, request):

        # 将请求参数统一放入request 的 params 属性中，方便后续处理
        # GET请求 参数 在 request 对象的 GET属性中
        if request.method == 'GET':
            request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        elif request.method in ['POST', 'PUT', 'DELETE']:
            # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
            request.params = json.loads(request.body)

        # 判断账号类型
        usertype = request.session.get('usertype', None)
        is_login = request.session.get('is_login', None)
        if usertype != 1 or not is_login:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号访问'})

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']
        if action == 'list':
            return self.list(request)
        elif action == 'modify':
            return self.modify(request)
        elif action == 'add':
            return self.add(request)
        elif action == 'delete':
            return self.delete(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def list(request):
        request.params['usertype'] = 1
        res = Order.list_order(request.params)
        return jsonResponse(res)

    @staticmethod
    def modify(request):
        res = User.modify_account(request.params)
        return jsonResponse(res)

    @staticmethod
    def add(request):
        res = User.add_account(request.params)
        return jsonResponse(res)

    @staticmethod
    def delete(request):
        res = User.delete_account(request.params)
        return jsonResponse(res)


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

        # 判断账号类型
        usertype = request.session.get('usertype', None)
        is_login = request.session.get('is_login', None)
        if usertype != 1 or not is_login:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号访问'})

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']
        if action == 'list':
            return self.list(request)
        elif action == 'modify':
            return self.modify(request)
        elif action == 'add':
            return self.add(request)
        elif action == 'delete':
            return self.delete(request)
        elif action == 'img_md':
            return self.imgMd()
        elif action == 'modify_content':
            return self.modify_content(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def list(request):
        res = Tags.admin_list()
        return jsonResponse(res)

    @staticmethod
    def modify(request):
        res = Tags.admin_modify(request.params)
        return jsonResponse(res)

    @staticmethod
    def add(request):
        res = Tags.admin_add(request.params)
        return jsonResponse(res)

    @staticmethod
    def delete(request):
        res = Tags.admin_delete(request.params)
        return jsonResponse(res)

    @staticmethod
    def imgMd():
        img = []
        md = []
        for i in os.listdir(f'{BASE_DIR}/static/images/article'):
            img.append({
                'img_name': i,
                'img_path': f'images/article/{i}'
            })

        for i in os.listdir(f'{BASE_DIR}/static/md'):
            md.append({
                'md_name': i,
                'md_path': f'md/{i}'
            })

        return jsonResponse({'ret': 0, 'images': img, 'md': md})

    @staticmethod
    def modify_content(request):
        res = ArticleContent.admin_modify(request.params)
        return jsonResponse(res)


class NoteBooks:
    def handler(self, request):

        # 将请求参数统一放入request 的 params 属性中，方便后续处理
        # GET请求 参数 在 request 对象的 GET属性中
        if request.method == 'GET':
            request.params = request.GET

        # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
        elif request.method in ['POST', 'PUT', 'DELETE']:
            # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
            request.params = json.loads(request.body)

        # 判断账号类型
        usertype = request.session.get('usertype', None)
        is_login = request.session.get('is_login', None)
        if usertype != 1 or not is_login:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号访问'})

        # 根据不同的action分派给不同的函数进行处理
        action = request.params['action']
        if action == 'list':
            return self.list()
        elif action == 'modify':
            return self.modify(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def list():
        res = NoteBook.admin_list()
        return jsonResponse(res)

    @staticmethod
    def modify(request):
        request.params['user_id'] = 1
        request.params['usertype'] = request.session['usertype']
        res = NoteBook.modify(request.params)
        return jsonResponse(res)


class FileManage:
    def handler(self, request):

        actionFormData = None

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
                actionFormData = request.POST.get('action', None)

        # 判断账号类型
        usertype = request.session.get('usertype', None)
        is_login = request.session.get('is_login', None)
        if usertype != 1 or not is_login:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号访问'})

        # 根据不同的action分派给不同的函数进行处理
        if actionFormData is None:
            action = request.params['action']
        else:
            action = actionFormData

        if action == 'list':
            return self.list(request)
        elif action == 'addfile':
            return self.addfile(request)
        elif action == 'addDir':
            return self.addDir(request)
        elif action == 'delete':
            return self.deleteFD(request)
        elif action == 'modify':
            return self.modifyFD(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    @staticmethod
    def list(request):
        file_path = request.params['file_path']
        file_path = os.path.join(BASE_DIR, file_path)
        if not os.path.exists(file_path):
            return jsonResponse({'ret': 1, 'msg': '文件路径不存在'})

        dirList = []
        fileList = []
        for i in os.listdir(file_path):
            if os.path.isfile(os.path.join(file_path, i)):
                fileList.append({
                    'type': 'file', 'name': i,
                    'size': os.path.getsize(os.path.join(file_path, i)),
                    'time': time.ctime(os.path.getmtime(os.path.join(file_path, i)))
                })
            else:
                dirList.append({
                    'type': 'dir', 'name': i,
                    'path': f'static{os.path.join(file_path, i).split("static")[-1]}'})
        files = dirList + fileList
        return jsonResponse({'ret': 0, 'retlist': files})

    @staticmethod
    def addfile(request):
        file = request.FILES.get("file", None)
        file_path = request.POST.get("file_path", None)
        file_name = str(file)

        if file_path:
            full_file_path = os.path.join(BASE_DIR, file_path, file_name)
        else:
            return jsonResponse({'ret': 1, 'msg': '没有获取到上传的文件的路径'})

        if file is None:
            return jsonResponse({'ret': 1, 'msg': '没有获取到上传的文件'})
        else:
            res = handle_uploaded_file(file, full_file_path)
            if res:
                return jsonResponse({'ret': 0})
            else:
                return jsonResponse({'ret': 1, 'msg': '上传文件失败'})

    @staticmethod
    def addDir(request):
        dir_path: str = request.params['dir_path']
        base_dir = request.params['base_path']
        if not dir_path.startswith('static'):
            dir_path = os.path.join(base_dir, dir_path)
        if os.path.isfile(dir_path):
            return jsonResponse({'ret': 1, 'msg': '请输入正确的目录'})
        os.makedirs(os.path.join(BASE_DIR, dir_path), exist_ok=True)
        return jsonResponse({'ret': 0})

    @staticmethod
    def deleteFD(request):
        path = request.params['path']
        full_path = os.path.join(BASE_DIR, path)
        if os.path.isfile(full_path) and os.path.exists(full_path):
            os.remove(full_path)
        elif os.path.isdir(full_path) and os.path.exists(full_path):
            shutil.rmtree(full_path)
        else:
            return jsonResponse({'ret': 1, 'msg': '未找到改文件，无法删除'})

        return jsonResponse({'ret': 0})

    @staticmethod
    def modifyFD(request):
        path = request.params['path']
        new_path = request.params['new_path']
        full_path = os.path.join(BASE_DIR, path)
        full_new_path = os.path.join(BASE_DIR, new_path)
        if os.path.exists(full_path) and not os.path.exists(full_new_path):
            os.rename(full_path, full_new_path)
            return jsonResponse({'ret': 0})
        else:
            return jsonResponse({'ret': 1, 'msg': '名称可能重复'})
