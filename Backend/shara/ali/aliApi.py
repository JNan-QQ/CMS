import time
from urllib.parse import parse_qs

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from userToken.models import order, userToken, products
from .alipay import AliPay
from ..shara import jsonResponse


class aliPay:
    obj = AliPay(
        appid="2021000118685158",  # 支付宝沙箱里面的APPID，需要改成你自己的
        app_notify_url="http://m4e1587419.qicp.vip/api/up_order",
        # 如果支付成功，支付宝会向这个地址发送POST请求（校验是否支付已经完成），此地址要能够在公网进行访问，需要改成你自己的服务器地址
        return_url="http://m4e1587419.qicp.vip/api/result",  # 如果支付成功，重定向回到你的网站的地址。需要你自己改，这里是我的服务器地址
        alipay_public_key_path=AliPay.ALIPAY_PUBLIC,  # 支付宝公钥
        app_private_key_path=AliPay.APP_PRIVATE,  # 应用私钥
        debug=True,  # 默认False,True表示使用沙箱环境测试
    )

    def createOrder(self, request):
        # 实例化SDK里面的类AliPay
        alipay = self.obj

        # 对购买的数据进行加密
        # 商户订单号
        orderNo = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + \
                  str(time.time()).replace('.', '')[-4:]
        product_id = request.params['product_id']

        ret = products.list_products({'product_id': product_id})
        title = ret['title']
        price = ret['price']

        # 1. 在数据库创建一条数据：状态（待支付）

        query_params = alipay.direct_pay(
            subject=f'自动化服务 - {title}',  # 商品简单描述
            out_trade_no=orderNo,  # 商户订单号
            total_amount=price,  # 交易金额(单位: 元 保留俩位小数)
        )
        # 拼接url，转到支付宝支付页面
        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)

        order.add_order({'user_id': request.session['user_id'], 'orderNo': orderNo, 'money': price, 'product': 1})

        # return redirect("https://openapi.alipaydev.com/gateway.do?{}".format(query_params))

        return jsonResponse({'ret': 0, 'url': pay_url})

    @csrf_exempt
    def update_order(self, request):
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

            sign = post_dict.pop('sign', None)
            status = self.obj.verify(post_dict, sign)
            if status:
                # 1.修改订单状态
                out_trade_no = post_dict.get('out_trade_no')
                # 2. 根据订单号将数据库中的数据进行更新
                res = order.modify_order({'orderNo': out_trade_no})
                if res['ret'] == 1:
                    return jsonResponse({'支付成功，订单更新失败'})
                user_id = res['user_id']
                product = res['product']
                if product == '1':
                    days = 30
                else:
                    days = 366

                res = userToken.modifyToken({'user_id': user_id, 'days': days})
                if res['ret'] == 1:
                    return HttpResponse('支付成功，套餐更新失败')

                return HttpResponse('支付成功')
            else:
                return HttpResponse('支付失败')
        return HttpResponse('')

    @csrf_exempt
    def pay_result(self, request):
        """
        支付完成后，跳转回的地址
        :param request:
        :return:
        """
        params = request.GET.dict()
        sign = params.pop('sign', None)

        status = self.obj.verify(params, sign)

        if status:
            return HttpResponse('支付成功')
        return HttpResponse('支付失败')
