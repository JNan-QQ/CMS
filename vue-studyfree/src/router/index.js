import {createRouter, createWebHistory} from 'vue-router'

import Login from '@/views/login'
import Index from '@/views/home'
import home from '@/views/home/home.vue'
import article from "@/views/home/articleView.vue";


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
            },
        ]
    },{
        path: '/login',
        name: 'Login',
        component: Login
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router
