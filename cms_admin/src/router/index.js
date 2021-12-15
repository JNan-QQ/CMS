import {createRouter, createWebHashHistory} from 'vue-router'
import Login from '@/views/login/'
import Home from '@/views/home/'
import Front from '../views/home/front.vue'
import Admin from '@/views/admin/index/'
import News from '../views/admin/news.vue'
import Account from '../views/admin/account.vue'
import Homepage from '../views/admin/homepage.vue'
import ContentView from '../views/home/contentView.vue'

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
            }, {
                path: 'homepage',
                component: Homepage
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
            },{
                path: 'contentView',
                component: ContentView
            },
        ]
    }
]

const router = createRouter(
    {
        history: createWebHashHistory(),
        routes
    })

export default router
