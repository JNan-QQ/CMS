import request from "@/api/request";
import {ElMessage} from "element-plus";

// 获取名人名言
export function getCq() {
    return request({
        url: 'cq',
        method: 'get',
        params: {
            action: 'list'
        }
    })
}

// 签到
export function qianDao(that) {
    return request({
        url: 'common/other',
        method: 'get',
        params: {action: 'qd'}
    }).then(res => {
        if (res) {
            that.$store.commit('changeUserInfo', {qd: '已签到'})
            ElMessage({
                message: '签到成功，F币加50，经验加500',
                type: 'success',
            })
        }
    })
}

// 获取验证码
export function registerEmailCode(email,email_type, that) {
    that.btnCodeStatus = true
    return request({
        url: 'common/other',
        method: 'post',
        data: {action: 'emailCode', email: email, email_type: email_type}
    }).then(res => {
        if (res) {
            ElMessage({
                message: res['msg'],
                type: 'success',
            })
        }
        that.btnCodeStatus = false
    })
}

// send email code
export function sendEmailCode(email_type) {
    return request({
        url: 'common/other',
        method: 'post',
        data: {action: 'emailCode', email_type: email_type}
    }).then(res => {
        if (res) {
            ElMessage({
                message: res['msg'],
                type: 'success',
            })
        }
    })
}


// common 接口
export function CommonApi(data) {
    return request({
        url: 'common/other',
        method: 'post',
        data: data
    })
}


//消息接口
export function MessageApi(data) {
    return request({
        url: 'common/message',
        method: 'post',
        data: data
    })
}