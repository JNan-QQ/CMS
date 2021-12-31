import {createRouter, createWebHashHistory} from 'vue-router'
import Login from '@/views/login/'
import Home from '@/views/home/'
import Order from '@/views/order/'
import Front from '../views/home/front.vue'
import Admin from '@/views/admin/index/'
import News from '../views/admin/news.vue'
import Account from '../views/admin/account.vue'
import Homepage from '../views/admin/homepage.vue'
import ContentView from '../views/home/contentView.vue'
import CS from '../views/home/index-1'
import ExcelData from '../components/excelsData.vue'

const routes = [
    {
        path: '/login',
        name: 'login',
        component: Login
    },{
        path: '/order',
        name: 'order',
        component: Order
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
            },{
                path: 'addMost',
                component: ExcelData
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
    },
    {
        path: '/cs',
        name: 'cs',
        component: CS,
        children: []
    },
]

const router = createRouter(
    {
        history: createWebHashHistory(),
        routes
    })

export default router
