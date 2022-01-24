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

// 获取文章页面tags
export function getSlideTags() {
    return request({
        url: 'frontEnd/article',
        method: 'get',
        params: {
            action: 'slideTags'
        }
    })
}

// 获取文章页面content名称
export function getArticleContentTags(data) {
    return request({
        url: 'frontEnd/article',
        method: 'post',
        data: data
    })
}

// 获取文章页面content内容
export function getArticleContent(data) {
    return request({
        url: 'frontEnd/article',
        method: 'get',
        params: data
    })
}

// 获取笔记页面content内容
export function noteContent(data) {
    return request({
        url: 'frontEnd/notebook',
        method: 'post',
        data: data
    })
}

// 下载文章扣费
export function downloadFree(price) {
    return request({
        url: 'download',
        method: 'get',
        params: {price: price, action: 'free'}
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
export function registerEmailCode(email, that) {
    that.btnCodeStatus = true
    return request({
        url: 'common/other',
        method: 'post',
        data: {action: 'emailCode', email: email}
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
export function sendEmailCode() {
    return request({
        url: 'common/other',
        method: 'post',
        data: {action: 'emailCode'}
    }).then(res => {
        if (res) {
            ElMessage({
                message: res['msg'],
                type: 'success',
            })
        }
    })
}

// 账号接口
export function AccountApi(data) {
    return request({
        url: 'common/account',
        method: 'post',
        data: data
    }).then(res => {
        if (res) {
            ElMessage({
                type: 'success',
                message: '操作成功!',
            })
            return res
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
