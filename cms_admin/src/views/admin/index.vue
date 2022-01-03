<template>
    <div style="display: flex">
        <el-row class="tac left">
            <el-col>
                <div style="display: flex;background-color: #545c64;margin-bottom: 1px;">
                    <el-image style="width: auto; height: 80px;margin-left: auto" src="./favicon.ico"
                              fit="fill"></el-image>
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
            <el-row class="top"
                    style="display: flex;flex-flow: row nowrap;flex-direction: row;align-items: center;justify-content: space-between">
                <div style="display:flex">
                    <el-icon>
                        <d-arrow-left style="width: 20px;height: 20px"/>
                    </el-icon>
                    <el-breadcrumb :separator-icon="ArrowRight" style="margin-left: 10px;font-size: 20px">
                        <el-breadcrumb-item v-for="page in index_page">{{ page }}</el-breadcrumb-item>
                    </el-breadcrumb>
                </div>
                <el-dropdown>
                    <div class="avatar" style="align-items: center; margin-right: 10px">
                        <el-avatar :src="userdata['aviator']" size="medium" class="avatar_img" fit="fill"></el-avatar>
                        <div class="user" style="margin-left: 10px">{{ userdata['realName'] }}</div>
                        <el-icon style="margin-left: 10px">
                            <arrow-down/>
                        </el-icon>
                    </div>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item @click="this.$router.push('/')">返回首页</el-dropdown-item>
                            <el-dropdown-item @click="toLogout">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>

            </el-row>
            <el-tag v-for="tag in index_table" :key="tag" closable :type="tps[Math.round(Math.random() * tps.length)]"
                    @close="handleClose(tag)" style="margin: 5px" @click="tagChange(tag)">
                {{ tag }}
            </el-tag>
            <router-view/>
        </div>
    </div>
</template>

<script>
import {
    ArrowDown,
    ArrowRight,
    Close,
    DArrowLeft,
    Flag,
    Headset,
    Message,
    Notebook,
    Notification,
    Setting,
    User
} from "@element-plus/icons"
import {loginMain} from "../../api/Login"
import {markRaw} from "vue"
import {ElMessage} from "element-plus"
import userdata from '../../utils/gloab'

export default {
    name: 'admin',
    data() {
        return {
            userdata,
            ArrowRight,
            activeIndex: 1,
            tps: ['success', '', 'danger', 'warning', 'info'],
            // 面包学导航
            index_page: [],
            // 标签页
            index_table: [],
            activeName: '',
        }
    },
    components: {
        User: markRaw(User),
        Setting: markRaw(Setting),
        Notebook: markRaw(Notebook),
        Headset: markRaw(Headset),
        Flag: markRaw(Flag),
        Message: markRaw(Message),
        Notification: markRaw(Notification),
        DArrowLeft: markRaw(DArrowLeft), ArrowRight: markRaw(ArrowRight),
        ArrowDown: markRaw(ArrowDown),
        Close: markRaw(Close),
    },

    // 加载函数
    mounted() {
        this.before()
    },

    // 监听函数
    watch: {
        activeIndex() {
            const pages = {
                '1': ['首页配置'],
                '2-1': ['账号管理', '学生'],
                '2-2': ['账号管理', '教师'],
                '2-3': ['账号管理', '管理员'],
                '3': ['新闻管理'],
                '4': ['通知管理'],
            }
            this.index_page = pages[this.activeIndex]
            this.index_table.push(pages[this.activeIndex][pages[this.activeIndex].length - 1])
            this.index_table = Array.from(new Set(this.index_table))
            const page_path = {
                '1': '/admin/homepage',
                '2-1': '/admin/account?type=student',
                '2-2': '/admin/account?type=teacher',
                '2-3': '/admin/account?type=mgr',
                '3': '/admin/news',
                '4': '',
            }
            this.$router.push(page_path[this.activeIndex])

        },
    },

    methods: {
        before() {
            loginMain('checkLogin', this).then(() => {
                    if (this.userdata.usertype === 1) {
                        this.$router.push('/admin/homepage')
                    } else {
                        ElMessage({
                            message: '请使用管理员账号登陆',
                            type: 'warning',
                        })
                        this.$router.push('/')
                    }
                }
            )


        },

        handleSelect(key, keyPath) {
            this.activeIndex = key
        },

        // 动态编辑标签
        handleClose(tag) {
            this.index_table.splice(this.index_table.indexOf(tag), 1)
        },

        // 点击标签
        tagChange(tag) {
            const pages = {
                '首页配置': '1',
                '学生': '2-1',
                '教师': '2-2',
                '管理员': '2-3',
                '新闻管理': '3',
                '通知管理': '4',
            }
            this.activeIndex = pages[tag]
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
            this.$router.push('/login')
        }
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
        border-width: 2px;
        border-bottom-style: inset;
    }

    .avatar {
        display: flex;
        margin-right: 10px;
        line-height: 80px;
        font-size: 16px;
    }

}
</style>
