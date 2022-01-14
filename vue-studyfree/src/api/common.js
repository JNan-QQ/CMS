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
export function getContentTags(data) {
    return request({
        url: 'frontEnd/article',
        method: 'post',
        data: data
    })
}

// 获取文章页面content名称
export function getContent(data) {
    return request({
        url: 'frontEnd/article',
        method: 'get',
        params: data
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

// 下载文章扣费
export function qianDao() {
    return request({
        url: 'common/qd',
        method: 'get',
        params: {action: 'qd'}
    }).then(res => {
        if (res) {
            ElMessage({
                message: '签到成功，F币加50，经验加500',
                type: 'success',
            })
        }
    })
}
