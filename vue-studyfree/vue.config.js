const baseApi = 'http://127.0.0.1:8210'

// 是否为生产环境
const isProduction = process.env.NODE_ENV !== 'development'

// 本地环境是否需要使用cdn
const devNeedCdn = true


const cdn = {
    // cdn：模块名称和模块作用域命名（对应window里面挂载的变量名称）
    externals: {
        'vue': 'Vue',
        'vue-router': 'VueRouter',
        'vuex': 'Vuex',
        'axios': 'axios',
        // 'element-plus': 'ElementPlus',
        'highlight.js': 'hljs',
    },

    css: [
        'https://unpkg.com/@highlightjs/cdn-assets@11.5.1/styles/atom-one-dark.min.css',
        // 'https://unpkg.com/element-plus@2.2.2/dist/index.css',
        'https://unpkg.com/md-editor-v3@2.0.1/lib/style.css',
    ],
    js: [
        'https://unpkg.com/vue@3.2.33/dist/vue.global.js',
        'https://unpkg.com/vue-router@4.0.15/dist/vue-router.global.js',
        'https://unpkg.com/vuex@4.0.2/dist/vuex.global.js',
        'https://unpkg.com/axios@0.27.2/dist/axios.min.js',
        // 'https://unpkg.com/element-plus@2.2.2/dist/index.full.js',
        'https:////unpkg.com/@highlightjs/cdn-assets@11.5.1/highlight.min.js',
        'https://unpkg.com/md-editor-v3@2.0.1/lib/md-editor-v3.umd.js'

    ]

}

module.exports = {
    publicPath: './',
    productionSourceMap: false,
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

    chainWebpack: config => {
        // ============压缩图片 start============
        config.module
            .rule('images')
            .use('image-webpack-loader')
            .loader('image-webpack-loader')
            .options({bypassOnDebug: true})
            .end()
        // ============压缩图片 end============

        // ============注入cdn start============
        config.plugin('html').tap(args => {
            // 生产环境或本地需要cdn时，才注入cdn
            if (isProduction || devNeedCdn)
                args[0].cdn = cdn
            return args
        })
        // ============注入cdn start============
    },

    configureWebpack: config => {
        // 用cdn方式引入，则构建时要忽略相关资源
        if (isProduction || devNeedCdn) config.externals = cdn.externals
    }
}
