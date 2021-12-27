import request from '../utils/request'
import {ElMessage} from "element-plus";

// 根据data里的数据类型列出账号
function listAccount(data, that) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'list'}, data)
    }).then(res => {
        that.accountData = res['retlist']
    })
}

// 修改账号
function modifyAccount(data, that) {
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
function addAccount(data, that) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'add'}, data)
    }).then(res => {
        if (that !== ''){
            ElMessage({message: '添加用户信息成功,id:' + res['id'], type: 'success',})
        that.before()
        }else {
            return res
        }
    })
}

// 删除账号
function deleteAccount(data, that) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'delete'}, data)
    }).then(res => {
        ElMessage({message: '用户删除成功！', type: 'success',})
        that.before()
    })
}

// 删除账号
function checkAccount(data) {
    return request({
        url: `/api/account/`,
        method: 'post',
        data: Object.assign({action: 'checkInfo'}, data)
    })
}

// 账号操作
export function accountMain(action='', that='',data={}) {
    switch (action) {
        case "list": //列出账号
            return listAccount(data, that)
        case "modify": //修改账号
            return modifyAccount(data, that)
        case "add": //添加账号
            return addAccount(data,that)
        case "delete": // 删除账号
            return deleteAccount(data,that)
        case "check":
            return checkAccount(data)
    }
}
