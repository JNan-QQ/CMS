import request from '../utils/request'
import {ElMessage} from "element-plus";

const api = `/notice/news`

// 根据data里的数据类型列出新闻
export function listNews(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'list'}, data)
    }).then(res => {
        if (res) {
            that.tableData = res['retlist']
        }
    })
}

// 根据data里的数据类型列出新闻类型
export function listNewsType(that) {
    return request({
        url: api,
        method: 'post',
        data: {action: 'listNewsType'}
    }).then(res => {
        if (res) {
            that.newsType = res['retlist']
        }
    })
}

// 根据data里的数据类型列出新闻首页轮播图
export function listNewsImg(that) {
    return request({
        url: api,
        method: 'post',
        data: {action: 'pageImg'}
    }).then(res => {
        if (res) {
            that.hotNewsData = res['retlist']
        }
    })
}


// 根据data里的数据类型列出新闻首页轮播图
export function listNewsHot(that) {
    return request({
        url: api,
        method: 'post',
        data: {action: 'pageNewsHot'}
    }).then(res => {
        if (res) {
            that.schoolTable = res['school_retlist']
            that.socTable = res['soc_retlist']
        }
    })
}


// 根据data里的数据修改新闻
export function modifyNews(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'modify'}, data)
    }).then(res => {
        if (res) {
            ElMessage({
                message: '修改新闻成功',
                type: 'success',
            })
            that.before()
        }
    })
}

// 根据data里的数据修改新闻轮播图
export function modifyNewsImg(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'modifyImg'}, data)
    }).then(res => {
        if (res) {
            if (that.baseImg !== '') {
                request.get('/api/files?action=delete&files_path=' + that.baseImg)
            }
            that.dialogVisible = false
            that.before()
        }
    })
}

// 根据data里的数据添加新闻
export function addNews(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'add'}, data)
    }).then(res => {
        if (res) {
            ElMessage({
                message: '添加新闻成功，id:' + res['news_id'],
                type: 'success',
            })
            that.before()
        }
    })
}

// 根据data里的数据添加新闻轮播图
export function addNewsImg(that) {
    return request({
        url: api,
        method: 'post',
        data: {action: 'addImg'}
    }).then(res => {
        if (res) {
            that.before()
        }
    })
}

// 根据data里的数据删除新闻
export function deleteNews(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'delete'}, data)
    }).then(res => {
        if (res) {
            ElMessage({
                message: '删除成功',
                type: 'success',
            })
            that.before()
        }
    })
}


// 根据data里的数据删除新闻轮播图
export function deleteNewsImg(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'deleteImg'}, data)
    }).then(res => {
        if (res) {
            that.before()
        }
    })
}

// 获取新闻详情
export function getOneNews(data, that) {
    return request({
        url: api,
        method: 'post',
        data: Object.assign({action: 'getOneNews'}, data)
    }).then(res => {
        if (res) {
            that.contents = res['retlist'][0]
        }

    })
}

