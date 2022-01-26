
import request from "./request";


// account 接口
export function AccountApi(data) {
    return request({
        url: 'my_admin/account',
        method: 'post',
        data: data
    })
}