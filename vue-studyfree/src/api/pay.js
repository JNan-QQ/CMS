// 获取文章页面content名称
import request from "@/api/request";

export function getUserConfig(that) {
    return request({
        url: 'pay/user',
        method: 'get',
        params: {action: 'userConfig'}
    }).then(res => {
        if (res) {
            that.$store.commit('changeUserInfo', res['retlist'][0])
        } else {
            that.$store.commit('deleteUserInfo')
        }
    })
}

export function UserConfigApi(data) {
    return request({
        url: 'pay/user',
        method: 'post',
        data: data
    })
}

export function orderApi(data) {
    return request({
        url: 'pay/order',
        method: 'post',
        data: data
    })
}

export function productApi(data) {
    return request({
        url: 'pay/product',
        method: 'post',
        data: data
    })
}

export function cdkApi(data) {
    return request({
        url: 'pay/cdk',
        method: 'post',
        data: data
    })
}