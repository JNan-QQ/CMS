import {createRouter, createWebHashHistory} from 'vue-router'
import Login from '@/views/login/'
import Home from '@/views/home/'
import Front from '../views/home/front.vue'


const routes = [
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    // {
    //     path: '/front',
    //     name: 'front',
    //     component: Front
    // },
    {
        path: '/',
        name: 'home',
        component: Home,
        children: [
        {
          path: 'front',
          component: Front
        }]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
