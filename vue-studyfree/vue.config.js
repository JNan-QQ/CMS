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
            // ts转发
            '/upload_file': {
                target: 'https://student.waiyutong.org',
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/upload_file': ''
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
    configureWebpack: {
        module: {
            rules: [
                // 配置读取 *.md 文件的规则
                {
                    test: /\.md$/,
                    use: [
                        {loader: "html-loader"},
                        {loader: "markdown-loader", options: {}}
                    ]
                }
            ]
        }
    }
}
