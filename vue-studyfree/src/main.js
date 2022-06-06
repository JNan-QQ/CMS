import {createApp} from 'vue'
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

import directives from "@/tools/directives";

const app = createApp(App)
app.use(store)
app.use(ElementPlus)
app.use(router)
app.use(VueParticles)
app.use(MdEditorV3)
directives(app)
app.mount('#app')