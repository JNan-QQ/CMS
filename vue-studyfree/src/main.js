import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

// 全局样式
import './styles/index.less'
import VueParticles from 'vue-particles'

// element ui 逐渐库
import ElementPlus from 'element-plus'

// 加载element 逐渐库 样式
import 'element-plus/dist/index.css'

createApp(App).use(store).use(ElementPlus).use(router).use(VueParticles).mount('#app')
