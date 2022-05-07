import json
import time
import traceback
from urllib.parse import parse_qs

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from Common.lib.shara import jsonResponse
from Admin.models import webConfig
from Pay.ali.alipay import AliPay
from Pay.models import Order, PayConfig
from django.shortcuts import redirect


class aliPay:
    # noinspection PyBroadException
    try:
        ailiConfig = webConfig.list({'title': 'aliPay'})['retlist'][0]['config']
        ailiConfig = json.loads(ailiConfig)
    except:
        ailiConfig = {
            "appid": "2021000118685158",
            "app_notify_url": "http://m4e1587419.qicp.vip/pay/success",
            "return_url": "http://m4e1587419.qicp.vip/pay/result",
            "ALIPAY_PUBLIC": "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAiB94AMC1zsRcML475bDibE7nt44HBt1nTFKvFr56lCbYddIOEKCVb+Hlamot952Av4fV9H+SdC/J6tjvAg5iRTsef/dHa7tAOqiER+JI8I7OC4yWgy3lxKGH5PDWihoK4rvil046X25bb0Wf3kfl6TLRvdIMOSFRzJ5XH4dA/2/hpCuxznRqK6qx2NBxornx4pmaQMK1c/umatYirxWBSJ1qEqD7olxapuUaX9DWDA5Jb7Jme6IHqqzspikCwQ9D0rRf7v91O3Swf7RMHbl56dkdRPdQdKxGe4hLJbzY8k4VoLmQOHM1m4dUHEchgC+kNad8AOTqzzOrkRgCifUlKQIDAQAB\n-----END PUBLIC KEY-----",
            "APP_PRIVATE": "-----BEGIN PUBLIC KEY-----\nMIIEpQIBAAKCAQEAp9ZJuTylblSLLyKSM/zU5iG+aAEmqUCYY/6kDmzLiXwqYKVwnE/dzdafcKExthhWCvIMrLRYkRX3NXkGURcVQoPvHBS+Zd8kJ36xnqOLhoFtzlmOjFI5koLipR0Zu5mmY/oSSopVKJBoLAUCFfoU/rtbTM/MhELyTwgGE9vW7jl1w189MScPB1kNGyMhIxMNbXWxE7TelOlaaIanUduJWcssYiqoboqBBGsCzkCX9IU8sChXV6ugtEPLqZXIoOpKj9QG24xMp3uSYGWVhRAaObn96tpWzkp2+fOIrBBeDtjgMcDhyHkLey6JowdOUrqgmdpUDrPwqo6sZjNiwPdc6wIDAQABAoIBAQCm8CvQRZQ+k3UFYxuM/jQ82t9qz4pG2us4urUva+NfUtNL4gKKV55E+O8Jtiud9cLPjEYzGgbl+LU0yLYRviX1TQluIuvmo/ZwGkJNilpjZSV1E/sHc1m0ct9AYBuST5gC5V+AKOvfNxOGhUy301FCtdRwKFhCTdx54384DXhQ5dWNyMLCLOHm03fDo5wE9glH+xSZqcnUCQGpFD85g/M+UwCmQUgZAw1EGV4pbIS2ghsLNjauOr/sR2TI2uqsc56O43DH7vNHbfcQ8/h7yuF6PM7AZ4K1NkDf+KfVGqODZU2JqMKXAfziw3oJV99tnRso0ce4kXQ0eYWtuMB2GzfRAoGBANigClc83zrC5b2p0TEUJOvnyWnQua8iRigOasmLqLGsFuwtgYkwHC8MeSncoHSziePaevJ/H7uV0oTdZbWeI9I6ucW61D9ms2Fbi7GZ+91UZY145oEZcG6glcc24xC/hxRX9yc1hoJaEu7Mk/033QZnhmwFMuicmphHX14fJ429AoGBAMZYDKilhoPk2z7zqsXaqJw7bGdaHGtkxWdslTdg8Ts3hGvXDzh6o3xgxol4LWpFDBYrNxUzNmwb+JS4eWvCvqKcZbqle9W2d9itJvPXFYlmzy1C4znjGEtiyx0qzSU6fH9MKc2tS/uGwjfURGw4c4RilPBomd8+OloLLrp3jlvHAoGBAMFeUvy+jLHCahvcq6y4w6CFXkiDlkzcNm3pOK/CaAp5iFi44kmY1X+2Da4tkFm8LlljnJ48lhH30lzh2Lm/eVBfNZdoh7A0t+kvM8qMnsRaYvBfPLt+/trxo+GZgCViIm0pfKjWYcSYLRBXM780j6r43IguN9xmdqV6CIpXGxKtAoGAHWbiAYIADb84LP3L++ZtBjPc3vlBqz3V8X3sJLhvKhsRuza3H+U2JPLnm2tAODeiEgs38CGWWLJQyCMMhMfqoIpUnjV3xPd2jp0kYBMrMyIVZh07N9KNQGeVum4k2Pbxi6FLtRySXefdFI+X0P8RSLegYn7vCGPeHIj51VRxuvMCgYEAtHwrnSLQWy819h4yo4u9dEeOxhXs96/uyi8TuFkeqjbKVjSQ3pVBsKqKuvm/CTOVZjErGgikipbEomKvzvYv8wsZ3i8b+7wzQg44HK45BwrIc5wfMFqVXpK24dMVfQrdKcL4NGvUM9ar3Hkk+SFlRwLXP6V9/oyvJmfRh4i+o/Q=\n-----END PUBLIC KEY-----",
            "debug": True
        }

    obj = AliPay(
        # 支付宝沙箱里面的APPID，需要改成你自己的
        # appid="2021000118685158",
        appid=ailiConfig['appid'],
        # 如果支付成功，支付宝会向这个地址发送POST请求（校验是否支付已经完成），此地址要能够在公网进行访问，需要改成你自己的服务器地址
        app_notify_url=ailiConfig['app_notify_url'],
        # 如果支付成功，重定向回到你的网站的地址。需要你自己改，这里是我的服务器地址
        return_url=ailiConfig['return_url'],
        alipay_public_key_path=ailiConfig['ALIPAY_PUBLIC'],  # 支付宝公钥
        app_private_key_path=ailiConfig['APP_PRIVATE'],  # 应用私钥
        debug=ailiConfig['debug'],  # 默认False,True表示使用沙箱环境测试
    )

    def createOrder(self, request):
        # 实例化SDK里面的类AliPay
        alipay = self.obj

        # 对购买的数据进行加密
        # 商户订单号
        orderNo = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + \
                  str(time.time()).replace('.', '')[-4:]
        money = request.params['money']

        # 1. 在数据库创建一条数据：状态（待支付）

        query_params = alipay.direct_pay(
            subject=f'自动化服务 - F币充值',  # 商品简单描述
            out_trade_no=orderNo,  # 商户订单号
            total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
        )
        # 拼接url，转到支付宝支付页面
        pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)

        FZ = json.loads(webConfig.list({'title': 'pay'})['retlist'][0]['config'])
        res = Order.add_order({'user_id': request.session['user_id'], 'orderNo': orderNo, 'money': money,
                               'F': int(FZ['F']), 'Z': float(FZ['Z'])})
        if res['ret'] == 1:
            return jsonResponse(res)

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
                res_order = Order.modify_order({'orderNo': out_trade_no})
                if res_order['ret'] == 1:
                    return jsonResponse({'支付成功，订单更新失败'})

                # 获取折扣信息
                FZ = json.loads(webConfig.list({'title': 'pay'})['retlist'][0]['config'])

                res_config = PayConfig.modify(
                    {'user_id': res_order['user_id'], 'exp': int(res_order['money']) * 50,
                     'coins': int(int(res_order['money']) * int(FZ['F']) * (float(FZ['Z']) + 1))})

                if res_config['ret'] == 1:
                    return HttpResponse('支付成功，F币更新失败')

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
            # return HttpResponse('支付成功')
            return redirect('http://localhost:8080/PaySuccess')
        # return HttpResponse('支付失败')
        return redirect('http://localhost:8080/PayError')
