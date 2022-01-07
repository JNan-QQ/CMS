import request from './request'
import {ElMessage} from "element-plus"


// 登录函数
export function sign(data) {
    let returnData = ''
    request({
        url: 'sign',
        method: 'post',
        data: data
    }).then(res => {
        if (res['ret'] === 0){
            returnData = res
        }
    })

    return returnData
}

