import request from '../utils/request'
import {ElMessage} from "element-plus";

// 根据data里的数据类型列出账号
export function listAccount(data, that) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'list'}, data)
    }).then(res => {
        that.accountData = res['retlist']
    })
}

// 修改账号
export function modifyAccount(data, that) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'modify'}, data)
    }).then(() => {
        ElMessage({message: '修改用户信息成功', type: 'success',})
        that.before()
    })
}

// 添加账号
export function addAccount(data, that) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'add'}, data)
    }).then(res => {
        ElMessage({message: '添加用户信息成功,id:' + res['id'], type: 'success',})
        that.before()
    })
}

// 删除账号
export function deleteAccount(data, that) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'delete'}, data)
    }).then(res => {
        ElMessage({message: '用户删除成功！', type: 'success',})
        that.before()
    })
}