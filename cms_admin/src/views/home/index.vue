<template>
    <div class="home-container">
        <div class="avatar" @click="toLogin">
            <el-avatar :src="avatar_src" size="medium" class="avatar_img" fit="fill"></el-avatar>
            <div class="user">{{ realName }}</div>
        </div>
        <el-container>
            <el-header>
                <el-menu :default-active="activeIndex2" class="header"
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
                    <el-menu-item index="5" v-if="p_center">个人中心</el-menu-item>
                </el-menu>
            </el-header>
            <el-main>Main</el-main>
            <el-footer>Footer</el-footer>
        </el-container>
    </div>
</template>

<script>
import {ElMessage} from "element-plus";
import request from "../../utils/request";

export default {
    name: "HomeIndex",
    data() {
        return {
            activeIndex2: 1,
            p_center: false,
            realName: '未登录',
            avatar_src: '',
            userdata: {},
        }
    },
    mounted() {
        this.getUserInfo()

    },
    methods: {
        getUserInfo() {
            const userdata = this.$route.params
            if ('ret' in userdata) {
                console.log(123456)
                this.userdata = userdata
                this.realName = userdata['realName']
                this.p_center = true
            }
        },


        handleSelect(key, keyPath) {
            console.log(key, keyPath)
        },

        toLogin() {
            if (this.realName === '未登录') {
                this.$router.push('/login')
            }
        }
    },
}
</script>

<style lang="less">
.home-container {
    width: 65%;
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
    }

    .el-header {
        padding-left: 0;
        padding-right: 0;
        margin-top: 5px;
    }
}


</style>
