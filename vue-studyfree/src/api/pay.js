// 获取文章页面content名称
import request from "@/api/request";

export function getUserConfig(that) {
    return request({
        url: 'pay/user',
        method: 'get',
        params:{action:'userConfig'}
    }).then(res => {
        if (res){
            that.$store.commit('changeUserInfo', res['retlist'][0])
        } else{
            that.$store.commit('deleteUserInfo')
        }
    })
}
