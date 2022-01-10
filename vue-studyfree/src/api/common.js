import request from "@/api/request";

// 获取名人名言
export function getCq() {
    return request({
        url: 'cq?action=list',
        method: 'get'
    })
}
