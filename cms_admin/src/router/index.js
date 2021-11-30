import {createRouter, createWebHashHistory} from 'vue-router'
import Login from '@/views/login/'
import Home from '@/views/home/'
import Front from '../views/home/front.vue'
import Admin from '@/views/admin/index/'


const routes = [
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/admin',
        name: 'admin',
        component: Admin
    },
    {
        path: '/',
        name: 'home',
        component: Home,
        children: [
        {
          path: 'front',
          component: Front
        },
        ]
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes
})

export default router
