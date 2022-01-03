/**
 * 基于 axios 的 请求模块
 */
import axios from 'axios'
import {ElMessage} from "element-plus"

// 创建一个 axios 实例
const request = axios.create({
    // 基础地址 host
    baseURL: 'api',
    // request 超时时间
    timeout: 300000
})

// 请求拦截器
request.interceptors.request.use(
    config => {
        return config
    },
    error => {
        // 请求错误 控制台输出信息
        // for debug
        console.log(error)
        return Promise.reject(error)
    }
)

// 响应拦截器
request.interceptors.response.use(
    response => {
        const res = response.data
        // 后台返回 标识 ret = {0:成功，1：失败，302：未登录}

        if (res['ret'] === 302) {
            ElMessage({
                message: '未登录，请先登录',
                type: 'warning',
            })
            return {path:'front'}
        } else if (res['ret'] === 1) {
            ElMessage({
                message: res['msg'],
                type: 'warning',
            })
        } else {
            return res
        }
    },
    error => {
        console.log('err' + error) // for debug
        ElMessage.error('服务器错误')
        return Promise.reject(error)
    }
)

export default request
