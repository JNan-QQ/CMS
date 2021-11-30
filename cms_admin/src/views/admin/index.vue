<template>
    <div style="display: flex">
        <el-row class="tac left">
            <el-col>
                <div style="display: flex;background-color: #545c64;margin-bottom: 1px;">
                    <el-image style="width: auto; height: 80px;margin-left: auto" src="./favicon.ico"
                              fit="fit"></el-image>
                    <span style="line-height: 80px;margin-left: 5px;margin-right: auto">CMS-ADMIN</span>
                </div>
                <el-menu active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo"
                         default-active="2" text-color="#fff" @select="handleSelect">
                    <el-menu-item index="1">
                        <el-icon>
                            <setting/>
                        </el-icon>
                        <span>首页配置</span>
                    </el-menu-item>
                    <el-sub-menu index="2">
                        <template #title>
                            <el-icon>
                                <user/>
                            </el-icon>
                            <span>账号管理</span>
                        </template>
                        <el-menu-item index="2-1">
                            <el-icon>
                                <headset/>
                            </el-icon>
                            学生
                        </el-menu-item>
                        <el-menu-item index="2-2">
                            <el-icon>
                                <notebook/>
                            </el-icon>
                            教师
                        </el-menu-item>
                        <el-menu-item index="2-3">
                            <el-icon>
                                <flag/>
                            </el-icon>
                            管理员
                        </el-menu-item>

                    </el-sub-menu>
                    <el-menu-item index="3">
                        <el-icon>
                            <notification/>
                        </el-icon>
                        <span>新闻管理</span>
                    </el-menu-item>
                    <el-menu-item index="4">
                        <el-icon>
                            <message/>
                        </el-icon>
                        <span>通知管理</span>
                    </el-menu-item>
                </el-menu>
            </el-col>
        </el-row>
        <div class="right">
            <el-row class="top" style="display: flex;flex-flow: row nowrap;flex-direction: row;align-items: center;">
                <el-col>
                    <el-icon>
                        <d-arrow-left/>
                    </el-icon>
                    <el-breadcrumb :separator-icon="ArrowRight">
                        <el-breadcrumb-item v-for="page in index_page">{{ page }}</el-breadcrumb-item>
                    </el-breadcrumb>
                </el-col>
            </el-row>
        </div>
    </div>
</template>

<script>
import {DArrowLeft, Flag, Headset, Message, Notebook, Notification, Setting, User,ArrowRight} from "@element-plus/icons"
import request from "../../utils/request";
import {ElMessage, ElMessageBox} from "element-plus";

export default {
    name: 'admin',
    data() {
        return {
            userdata: {},
            ArrowRight,
            activeIndex:1,
            index_page:[]
        }
    },
    components: {User, Setting, Notebook, Headset, Flag, Message, Notification, DArrowLeft,ArrowRight},

    mounted() {
        this.before()
    },

    methods: {
        before() {
            const that = this
            request.post('/api/sign/', {action: 'checkLogin'}).then(res => {
                if (res.data['ret'] === 0) {
                    this.userdata = res.data
                    if (res.data['usertype'] !== 1) {
                        ElMessageBox.confirm('你登录的不是管理员账号，无法访问此页面奥！', 'Warning',
                            {
                                confirmButtonText: '登录',
                                cancelButtonText: '取消',
                                type: 'warning',
                            }).then(() => {
                            ElMessage({
                                type: 'success',
                                message: '进入登录界面',
                            })
                            that.$router.push('/login')
                        }).catch(() => {
                            ElMessage({
                                type: 'success',
                                message: '进入首页',
                            })
                            that.$router.push('/')
                        })
                    }
                }
            })
        },

        handleSelect(key, keyPath) {
            this.activeIndex = key
            const pages = {
                '1':['首页配置'],
                '2-1':['账号管理','学生'],
                '2-2':['账号管理','教师'],
                '2-3':['账号管理','管理员'],
                '3':['新闻管理'],
                '4':['通知管理'],
            }
            this.index_page = pages[key]
        },
    }

}
</script>

<style lang="less" scoped>
.tac {
    width: 260px;
}

.right {
    width: 100%;
    margin-left: 8px;

    .top {
        height: 80px;
        background-color: #ffffff;
    }

}
</style>
