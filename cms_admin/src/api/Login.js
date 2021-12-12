import request from '../utils/request'
import {ElMessage} from "element-plus";

const api = '/api/sign/'
// 登录函数
export function signin(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'signin'}, data)
    }).then(res => {
        console.log(res)
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
export function signout() {
    return request({
        url: api,
        method: 'post',
        data: {action: 'signout'}
    })
}

// 判断是否登录函数
export function checklogin(that) {
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
