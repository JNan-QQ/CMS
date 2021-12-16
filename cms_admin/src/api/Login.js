import request from '../utils/request'
import {ElMessage} from "element-plus"
import {ref} from "vue";

const api = '/api/sign/'

// 登录函数
function signin(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'signin'}, data)
    }).then(res => {
        if (res['ret'] === 0) {
            ElMessage({
                message: '登陆成功！欢迎您：' + res['realName'],
                type: 'success',
            })
            // 跳转到首页
            that.$router.push('/')
        }
    })
}

// 登出函数
function signout() {
    return request({
        url: api,
        method: 'post',
        data: {action: 'signout'}
    })
}

// 判断是否登录函数
function checklogin(that) {
    return request({
        url: api,
        method: 'post',
        data: {action: 'checkLogin'}
    }).then(res => {
        if ('path' in res) {
            that.userdata = {
                realName: '未登录',
                aviator: '',
                id: 0,
                usertype: 0
            }
            that.$router.push(res.path)
        } else {
            that.userdata = res
        }
    })
}

// 登录函数
export function loginMain(action = '', that = '', data = {}) {
    switch (action) {
        case "signin": //登录
            return signin(data, that)
        case "signout": //登出
            return signout()
        case "checkLogin": //检查是否登录
            return checklogin(that)
    }

}
