import {createRouter, createWebHistory} from 'vue-router'

import Login from '@/views/login'
import rpa from '@/views/login/rPA.vue'

import Index from '@/views/home'
import home from '@/views/home/home.vue'
import article from "@/views/home/articleView.vue"
import note from "@/views/home/noteView.vue"
import noteTest from "@/views/home/noteView_test.vue"
import skill from "@/views/home/skillView.vue"
import tool from "@/views/home/toolView.vue"

import markdownView from "@/components/articleViewPage/markdownView.vue"

import myCenter from "@/views/mycenter"

import pay from "@/views/pay"
import errorPay from "@/views/pay/error.vue"
import successPay from "@/views/pay/success.vue"

import admin from '@/views/admin'

import page404 from "@/components/error-page/404.vue"
import {ElMessage} from "element-plus";


const routes = [
    {
        path: '/',
        name: 'Index',
        component: Index,
        redirect: '/home',
        children: [
            {
                path: 'home',
                component: home
            }, {
                path: 'Article',
                component: article
            }, {
                path: 'Note',
                component: note
            }, {
                path: 'Skill',
                component: skill
            }, {
                path: 'Tool',
                component: tool
            },{
                path: 'NoteTest',
                component: noteTest
            }
        ]
    },
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/forget',
        name: 'rPa',
        component: rpa
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
        component: pay,
        meta: {isLogin: true},     //这个参数 true 代表可以进入这个页面
    },
    {
        path: '/PayError',
        name: 'error',
        component: errorPay,
    },
    {
        path: '/PaySuccess',
        name: 'success',
        component: successPay,
    },
    {
        path: '/admin',
        name: 'admin',
        component: admin,
        meta: {isMgr: true}     //这个参数 true 代表可以进入这个页面
    },
    {
        path: '/404',
        name: '404',
        component: page404
    },
    {
        path: '/:pathMatch(.*)',
        redirect: '/404'
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.meta['isMgr']) {
        const usertype = JSON.parse(localStorage.getItem('userdata')).usertype
        if (usertype === 1) {
            next()
        } else {
            next({path: '/404'})
        }
    } else if (to.meta['isLogin']) {
        const isLogin = JSON.parse(localStorage.getItem('userdata')).isLogin
        if (isLogin) {
            next()
        } else {
            next({path: '/home'})
            ElMessage.warning('请先登录┗|｀O′|┛ 嗷~~')
        }
    } else {
        next()
    }
})


export default router
