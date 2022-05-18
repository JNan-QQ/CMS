import os
import random
import time
import traceback

import requests
from django import forms
from django.conf import settings


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


def handle_uploaded_file(f, f_path):
    with open(f_path, 'wb') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return True


class UpLoad:
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
        'Connection': 'keep-alive',
        'Referer': 'https://www.waiyutong.org/',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Mode': 'cors'
    }
    userInfo = [{'username': 'phbed01', 'password': '9636029e8db4db2837329f09b68ba2f2'},
                {'username': 'phbed02', 'password': '9636029e8db4db2837329f09b68ba2f2'},
                {'username': 'phbed03', 'password': '9636029e8db4db2837329f09b68ba2f2'},
                {'username': 'phbed04', 'password': '9636029e8db4db2837329f09b68ba2f2'},
                {'username': 'phbed05', 'password': '9636029e8db4db2837329f09b68ba2f2'}]

    session = requests.Session()

    def __init__(self, mode):
        if mode != 'NO_LOGIN':
            url = 'https://www.waiyutong.org/User/login.html'
            user = random.choice(self.userInfo)
            data = {'username': user['username'], 'password': user['password'], 'act': 'auto'}
            self.session.post(url, data, headers=self.headers)

    def uploadImg(self, request):
        # 图片content
        File = request.FILES.get("file", None)
        # 图片类型 ，当oss上传失败时保存到本地
        file_type = request.POST['file_type']
        # 图片名称
        file_name = request.POST['file_name'].replace('timeR', str(int(time.time())))

        # oss
        # 构建消息体
        files = {'image': (file_name, File, 'image/png')}
        # 上传地址
        url = 'https://student.waiyutong.org/Practice/compositionUploadImg.html'
        # 上传结果
        resUpload = self.session.post(url, files=files, headers=self.headers)

        if resUpload.status_code == 200:
            return resUpload.json()['info']['imageUrl']
        else:
            return self.saveFile(File, file_type, file_name)

    @staticmethod
    def saveFile(f, file_type, file_name):
        # 保存到本地的文件路径
        if file_type in ['article', 'aviator', 'notebook']:
            dirName = 'static/images'
        else:
            dirName = 'static/md'
        f_path = os.path.join(settings.BASE_DIR, dirName, file_type, file_name)
        with open(f_path, 'wb') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return f'{dirName}/{file_type}/{file_name}'


upLoadFile = UpLoad('NO_LOGIN')
