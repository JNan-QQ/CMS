import { createApp } from 'vue'
import App from './App.vue'

// 路由表
import router from './router'

// 全局样式
import './styles/index.less'

// element ui 逐渐库
import ElementPlus from 'element-plus'

// 加载element 逐渐库 样式
import 'element-plus/dist/index.css'

import 'default-passive-events'




createApp(App).use(router).use(ElementPlus).mount('#app')

