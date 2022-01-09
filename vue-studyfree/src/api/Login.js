import request from './request'


// 登录函数
export function sign(data,that='') {
    return request({
        url: 'sign',
        method: 'post',
        data: data
    })
}

// 登录函数
export function checkLogin(that) {
    return request({
        url: 'sign',
        method: 'post',
        data: {action:'checkLogin'}
    }).then(res => {
        that.$store.commit('changeUserInfo', res)
    })
}
