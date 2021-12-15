import request from '../utils/request'
import {ElMessage} from "element-plus";

const api = `/api/common`

// 根据data里的数据类型列出新闻
export function listCq(that) {
    return request({
        url: api+'/CQ',
        method: 'post',
        data: {action: 'list'}
    }).then(res => {
        if (res) {
            that.CQ = res['retlist']
        }
    })
}
