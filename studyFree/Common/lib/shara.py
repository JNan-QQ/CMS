# -*- coding:utf-8 -*-
# @FileName  :shara.py
# @Time      :2021/11/11 9:12
# @Author    :姜楠
# @Tool      :PyCharm
from django.http import JsonResponse


def jsonResponse(response, status=0):
    if status:
        return JsonResponse({'ret': 1, 'msg': 'action参数错误'}, status=status, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


if __name__ == "__main__":
    run_code = 0
