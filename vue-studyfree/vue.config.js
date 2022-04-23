const baseApi = 'http://127.0.0.1:8210'

module.exports = {
    publicPath: './',
    devServer: {
        proxy: {
            // 静态文件转发
            '/api_file': {
                target: baseApi,
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/api_file': ''
                }
            },
            // api转发
            '/api': {
                target: baseApi,
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
        }
    },

}
