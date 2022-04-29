import request from './request'


// 登录函数
export function sign(data,that='') {
    return request({
        url: 'sign',
        method: 'post',
        data: data
    })
}

// 检查是否登录
export function checkLogin(that) {
    return request({
        url: 'sign',
        method: 'post',
        data: {action:'checkLogin'}
    }).then(res => {
        if (res){
            res['isLogin'] = true
            that.$store.commit('changeUserInfo', res)
        } else{
            that.userdata = {}
            that.$store.commit('deleteUserInfo')
        }
    })
}
