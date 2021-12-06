import {createRouter, createWebHashHistory} from 'vue-router'
import Login from '@/views/login/'
import Home from '@/views/home/'
import Front from '../views/home/front.vue'
import Admin from '@/views/admin/index/'
import News from '../views/admin/news.vue'
import Account from '../views/admin/account.vue'

const routes = [
    {
        path: '/login',
        name: 'login',
        component: Login
    },
    {
        path: '/admin',
        name: 'admin',
        component: Admin,
        children: [
            {
                path: 'news',
                component: News
            }, {
                path: 'account',
                component: Account
            },
        ]
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
