import request from "@/api/request";

// 获取名人名言
export function getCq() {
    return request({
        url: 'cq',
        method: 'get',
        params:{
            action: 'list'
        }
    })
}

// 获取文章页面tags
export function getSlideTags() {
    return request({
        url: 'frontEnd/article',
        method: 'get',
        params:{
            action:'slideTags'
        }
    })
}

// 获取文章页面content名称
export function getContentTags(data) {
    return request({
        url: 'frontEnd/article',
        method: 'post',
        data:data
    })
}

// 获取文章页面content名称
export function getContent(data) {
    return request({
        url: 'frontEnd/article',
        method: 'get',
        params:data
    })
}
