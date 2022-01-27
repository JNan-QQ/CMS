
import request from "./request";


// account 接口
export function AccountApi(data) {
    return request({
        url: 'my_admin/account',
        method: 'post',
        data: data
    })
}

// order 接口
export function OrderApi(data) {
    return request({
        url: 'my_admin/order',
        method: 'post',
        data: data
    })
}

// article 接口
export function ArticleApi(data) {
    return request({
        url: 'my_admin/article',
        method: 'post',
        data: data
    })
}
