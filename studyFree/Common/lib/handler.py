# -*- coding:utf-8 -*-
# @FileName  :handler.py
# @Time      :2022/4/1 15:13
# @Author    :JN
import json
import traceback

from Common.lib.shara import jsonResponse, IS_LOGIN, IS_MGR, MGR


def dispatcherBase(request, action2HandlerTable, LOGIN_STATUS=None):
    # 登录信息判断
    # 要求登录
    if LOGIN_STATUS == IS_LOGIN:
        if 'usertype' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'})
    # 要求管理员
    elif LOGIN_STATUS == IS_MGR:
        if 'usertype' not in request.session:
            return jsonResponse({'ret': 302, 'msg': '未登录'})
        if request.session['usertype'] != MGR:
            return jsonResponse({'ret': 1, 'msg': '请使用管理员账号操作'})

    actionFormData = None

    # 将请求参数统一放入request 的 params 属性中，方便后续处理
    # GET请求 参数 在 request 对象的 GET属性中
    if request.method == 'GET':
        request.params = request.GET

    # POST/PUT/DELETE 请求 参数 从 request 对象的 body 属性中获取
    elif request.method in ['POST', 'PUT', 'DELETE']:
        # 根据接口，POST/PUT/DELETE 请求的消息体都是 json格式
        # noinspection PyBroadException
        try:
            request.params = json.loads(request.body)
        except:
            actionFormData = request.POST.get('action', None)

    # 根据不同的action分派给不同的函数进行处理
    if actionFormData is None:
        action = request.params['action']
    else:
        action = actionFormData

    # 根据不同的action分派给不同的函数进行处理
    if action in action2HandlerTable:
        handlerFunc = action2HandlerTable[action]
        return handlerFunc(request)

    else:
        return jsonResponse({'ret': 1, 'msg': 'action参数错误'})
