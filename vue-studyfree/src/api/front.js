import request from "@/api/request";

// 技巧Api
export function skillApi(data) {
    return request({
        url: 'frontEnd/skill',
        method: 'post',
        data: data
    })
}

// 获取笔记页面content内容
export function noteContent(data) {
    return request({
        url: 'frontEnd/notebook',
        method: 'post',
        data: data
    })
}

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
export function getArticleContentTags(data) {
    return request({
        url: 'frontEnd/article',
        method: 'post',
        data: data
    })
}

// 获取文章页面content内容
export function getArticleContent(data) {
    return request({
        url: 'frontEnd/article',
        method: 'get',
        params: data
    })
}