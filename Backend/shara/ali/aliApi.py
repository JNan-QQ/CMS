import json
from urllib.parse import parse_qs

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from userToken.models import order
from .alipay import AliPay
from ..shara import jsonResponse


class aliPay:
    obj = AliPay(
        appid="2021000118685158",  # 支付宝沙箱里面的APPID，需要改成你自己的
        app_notify_url="http://m4e1587419.qicp.vip:48011/update_order/",
        # 如果支付成功，支付宝会向这个地址发送POST请求（校验是否支付已经完成），此地址要能够在公网进行访问，需要改成你自己的服务器地址
        return_url="http://m4e1587419.qicp.vip:48011/result/",  # 如果支付成功，重定向回到你的网站的地址。需要你自己改，这里是我的服务器地址
        alipay_public_key_path=AliPay.ALIPAY_PUBLIC,  # 支付宝公钥
        app_private_key_path=AliPay.APP_PRIVATE,  # 应用私钥
        debug=True,  # 默认False,True表示使用沙箱环境测试
    )

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
        if action == 'createOrder':
            return self.createOrder(request)
        # elif action == 'payOrder':
        #     return self.payOrder(request)
        else:
            return jsonResponse({'ret': 1, 'msg': 'action参数错误'})

    def createOrder(self, request):
        # 实例化SDK里面的类AliPay
        alipay = self.obj

        # 对购买的数据进行加密
        orderNo = "20211230112"  # 商户订单号   # 订单号可以有多中生成方式，可以百度一下
        price = 100.00
        # 1. 在数据库创建一条数据：状态（待支付）

        query_params = alipay.direct_pay(
            desc="自动化服务购买",  # 商品简单描述 这里一般是从前端传过来的数据
            orderNo=orderNo,  # 商户订单号  这里一般是从前端传过来的数据
            price=price,  # 交易金额(单位: 元 保留俩位小数)   这里一般是从前端传过来的数据
        )
        # 拼接url，转到支付宝支付页面
        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)

        order.add_order({'user_id': request.session['user_id'], 'orderNo': orderNo})

        return jsonResponse({'ret': 0, 'payUrl': pay_url})


@csrf_exempt
def update_order(request):
    """
    支付成功后，支付宝向该地址发送的POST请求（用于修改订单状态）
    :param request:
    :return:
    """
    if request.method == 'POST':
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]

        alipay = aliPay()

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        if status:
            # 1.修改订单状态
            out_trade_no = post_dict.get('out_trade_no')
            print(out_trade_no)
            # 2. 根据订单号将数据库中的数据进行更新
            return HttpResponse('支付成功')
        else:
            return HttpResponse('支付失败')
    return HttpResponse('')


@csrf_exempt
def pay_result(request):
    """
    支付完成后，跳转回的地址
    :param request:
    :return:
    """
    params = request.GET.dict()
    sign = params.pop('sign', None)

    alipay = aliPay()

    status = alipay.verify(params, sign)

    if status:
        return HttpResponse('支付成功')
    return HttpResponse('支付失败')
