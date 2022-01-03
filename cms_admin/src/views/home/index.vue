<template>
    <div class="home-container">
        <el-dropdown>
            <div class="avatar" @click="toLogin">
                <el-avatar :src="userdata.aviator" size="medium" class="avatar_img" fit="fill"></el-avatar>
                <div class="user">{{ userdata.realName }}</div>
                <el-icon>
                    <arrow-down class="zk"/>
                </el-icon>
            </div>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item v-if="userdata.realName !== '未登录'" @click="toLogout">退出登录</el-dropdown-item>
                    <el-dropdown-item v-else @click="toLogin">登录</el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
        <el-container>
            <el-header>
                <el-menu :default-active="activeIndex" class="header"
                         mode="horizontal" background-color="#545c64"
                         text-color="#fff" active-text-color="#ffd04b"
                         @select="handleSelect">
                    <el-menu-item index="1">首页</el-menu-item>
                    <el-sub-menu index="2">
                        <template #title>校园新闻</template>
                        <el-menu-item index="2-1">学校介绍</el-menu-item>
                        <el-menu-item index="2-2">疫情防控</el-menu-item>
                        <el-menu-item index="2-3">校园活动</el-menu-item>
                        <el-menu-item index="2-4">学校荣誉</el-menu-item>
                    </el-sub-menu>
                    <el-menu-item index="3">社会热点</el-menu-item>
                    <el-menu-item index="4">失物招领</el-menu-item>
                    <el-menu-item index="5" v-if="userdata.realName !== '未登录'">个人中心</el-menu-item>
                </el-menu>
            </el-header>
            <el-main>
                <router-view/>
            </el-main>
            <el-footer><span>{{ CQ.content }} -- {{ CQ.author }}</span></el-footer>
        </el-container>
    </div>
</template>

<script>
import {loginMain} from "../../api/Login"
import {ElMessage} from "element-plus"
import {ArrowDown} from "@element-plus/icons"
import {markRaw} from "vue"
import userdata from '../../utils/gloab'
import {listCq} from "../../api/common";

export default {
    name: "HomeIndex",
    data() {
        return {
            activeIndex: '1',
            userdata,
            router_index: {
                '1': '/front',
                '5': '/common',
            },
            CQ: {},
        }
    },
    // 注册组件
    components: {ArrowDown: markRaw(ArrowDown)},
    // 进入页面执行函数
    mounted() {
        this.before()
        this.changeCq()

    },
    // 监听
    watch: {
        activeIndex() {
            if (this.activeIndex in this.router_index) {
                this.$router.push(this.router_index[this.activeIndex])
            } else {
                ElMessage('该页面还未配置奥！')
            }
        }
    },

    // 函数定义
    methods: {
        // 加载函数
        before() {
            loginMain('checkLogin', this).then(() => {
                if (this.userdata['usertype'] === 1) {
                    this.router_index["5"] = '/admin'
                } else if (this.userdata['usertype'] === 10) {
                    this.$router.push('/order')
                }
                this.$router.push('/front')
            })
        },

        // 导航栏点击函数
        handleSelect(key, keyPath) {
            this.activeIndex = key
        },

        // 点击登录函数
        toLogin() {
            if (this.userdata.realName === '未登录') {
                this.$router.push('/login')
            }
        },

        // 退出登录函数
        toLogout() {
            loginMain('signout')
            this.userdata = {
                realName: '未登录',
                aviator: '',
                id: 0,
                usertype: 0
            }
        },

        // 随机名言
        changeCq() {
            listCq(this)
        },
    },
}
</script>

<style lang="less">
.home-container {
    width: 55%;
    min-height: 900px;
    margin: 0 auto;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);

    .avatar {
        display: flex;
        height: 50px;

        .user {
            line-height: 50px;
            margin-right: 10px;
        }

        .avatar_img {
            margin: auto 10px;
        }

        .el-icon {
            margin: auto 0;
        }
    }

    .el-header {
        padding-left: 0;
        padding-right: 0;
        margin-top: 5px;
    }

    .el-footer {
        text-align: center;
        margin-bottom: 0;
    }
}


</style>
