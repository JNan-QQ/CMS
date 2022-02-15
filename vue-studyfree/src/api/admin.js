
import request from "./request";

// webConfig 接口
export function WebConfigApi(data) {
    return request({
        url: 'my_admin/webconfig',
        method: 'post',
        data: data
    })
}

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

// notebook 接口
export function NoteBookApi(data) {
    return request({
        url: 'my_admin/notebook',
        method: 'post',
        data: data
    })
}

// 获取名人名言
export function CqApi(data) {
    return request({
        url: 'cq',
        method: 'post',
        data: data
    })
}

// 获取名人名言
export function FilesApi(data) {
    return request({
        url: 'my_admin/files',
        method: 'post',
        data: data
    })
}