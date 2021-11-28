/**
 * 基于 axios 的 请求模块
 */
import axios from 'axios'

// 创建一个 axios 实例
const request = axios.create({
    // 基础地址 host
    // baseURL: 'http://127.0.0.1:8210'
})

export default request
