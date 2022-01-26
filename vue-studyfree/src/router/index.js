import {createRouter, createWebHistory} from 'vue-router'

import Login from '@/views/login'
import Index from '@/views/home'
import home from '@/views/home/home.vue'
import article from "@/views/home/articleView.vue"
import note from "@/views/home/noteView.vue"
import skill from "@/views/home/skillView.vue"
import tool from "@/views/home/toolView.vue"
import markdownView from "@/components/markdownView.vue"
import myCenter from "@/views/mycenter"
import pay from "@/views/pay"
import admin from '@/views/admin'
import account from "@/views/admin/account.vue"


const routes = [
    {
        path: '/',
        name: 'Index',
        component: Index,
        children: [
            {
                path: 'home',
                component: home
            },{
                path: 'Article',
                component: article
            },{
                path: 'Note',
                component: note
            },{
                path: 'Skill',
                component: skill
            },{
                path: 'Tool',
                component: tool
            },
        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/md',
        name: 'MarkDownView',
        component: markdownView
    },
    {
        path: '/myCenter',
        name: 'myCenter',
        component: myCenter
    },
    {
        path: '/pay',
        name: 'pay',
        component: pay
    },
    {
        path: '/admin',
        name: 'admin',
        component: admin,
        children: [
            {
                path: '/admin/account',
                component: account
            }
        ]
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
