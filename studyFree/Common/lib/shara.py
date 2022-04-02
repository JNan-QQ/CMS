# -*- coding:utf-8 -*-
# @FileName  :shara.py
# @Time      :2021/11/11 9:12
# @Author    :姜楠
# @Tool      :PyCharm
import random

from django.http import JsonResponse


def jsonResponse(response, status=0):
    if status:
        return JsonResponse({'ret': 1, 'msg': 'action参数错误'}, status=status, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


def generate_random_str(random_length=6):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789'
    length = len(base_str) - 1
    for i in range(random_length):
        random_str += base_str[random.randint(0, length)]
    return random_str


# 公共参数

# 登录状态
NOT_LOGIN = 0
IS_LOGIN = 100
IS_MGR = 1

# 用户类型
MGR = 1
FREE = 1000
VIP = 1005

if __name__ == "__main__":
    a = generate_random_str()
    print(a)
