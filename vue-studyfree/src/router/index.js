import {createRouter, createWebHistory} from 'vue-router'

import Login from '@/views/login'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: ''
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
