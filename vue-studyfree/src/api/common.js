import request from "@/api/request";

// 获取名人名言
export function getCq() {
    return request({
        url: 'cq?action=list',
        method: 'get'
    })
}

// 获取文章页面tags
export function getSlideTags() {
    return request({
        url: 'frontEnd/article?action=slideTags',
        method: 'get'
    })
}

// 获取文章页面content
export function getContentTags(data) {
    return request({
        url: 'frontEnd/article',
        method: 'post',
        data:data
    })
}
