module.exports = {
    publicPath: './',
    devServer: {
        proxy: {
            '/api': {
                target: 'http://127.0.0.1:8210',
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/api': ''
                }
            },
            '/api_file': {
                target: 'http://127.0.0.1:8210',
                changeOrigin: true,
                ws: true,
                pathRewrite: {
                    '^/api_file': ''
                }
            }
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
