<template>
    <div class="admin-view">
        <div class="tac left">
            <div class="sf">SF-ADMIN</div>
            <el-menu active-text-color="#ffd04b" background-color="#545c64" :collapse="isCollapse"
                     text-color="#fff" @select="handleSelect" :default-active="activeIndex">
                <el-menu-item index="1">
                    <el-icon>
                        <setting/>
                    </el-icon>
                    <template #title>网站配置</template>
                </el-menu-item>
                <el-menu-item index="2">
                    <el-icon>
                        <user/>
                    </el-icon>
                    <template #title>账号管理</template>
                </el-menu-item>
                <el-menu-item index="3">
                    <el-icon>
                        <notification/>
                    </el-icon>
                    <template #title>订单管理</template>
                </el-menu-item>
                <el-menu-item index="4">
                    <el-icon>
                        <message/>
                    </el-icon>
                    <template #title>通知管理</template>
                </el-menu-item>
                <el-menu-item index="5">
                    <el-icon>
                        <document/>
                    </el-icon>
                    <template #title>文章管理</template>
                </el-menu-item>
                <el-menu-item index="6">
                    <el-icon>
                        <notebook/>
                    </el-icon>
                    <template #title>笔记管理</template>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="right">
            <div class="top">
                <div style="display:flex">
                    <el-icon @click="this.isCollapse=!this.isCollapse">
                        <d-arrow-left style="width: 20px;height: 20px"/>
                    </el-icon>
                    <el-breadcrumb :separator-icon="ArrowRight" style="margin-left: 10px;font-size: 20px">
                        <el-breadcrumb-item v-for="page in index_page">{{ page }}</el-breadcrumb-item>
                    </el-breadcrumb>
                </div>
                <el-dropdown>
                    <div class="avatar">
                        <el-avatar :src="userdata['aviator']" :size="45" fit="fill"></el-avatar>
                        <div class="username">{{ userdata['realName'] }}</div>
                        <el-icon>
                            <arrow-down/>
                        </el-icon>
                    </div>
                    <template #dropdown>
                        <el-dropdown-menu>
                            <el-dropdown-item @click="this.$router.push('/home')">返回首页</el-dropdown-item>
                            <el-dropdown-item @click="toLogout">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </template>
                </el-dropdown>
            </div>
            <el-tag v-for="tag in index_table" :key="tag" closable :type="tps[Math.round(Math.random() * tps.length)]"
                    @close="handleClose(tag)" @click="tagChange(tag)">
                {{ tag }}
            </el-tag>
            <router-view/>
        </div>
    </div>
</template>

<script>
import {
    ArrowDown, ArrowRight, Close, DArrowLeft, Flag, Headset, Document,
    Message, Notebook, Notification, Setting, User
} from "@element-plus/icons"
import {markRaw} from "vue"
import {checkLogin, sign} from "@/api/Login";
import {ElMessage} from "element-plus";

export default {
    name: 'admin',
    data() {
        return {
            userdata: this.$store.state.userdata,
            isCollapse: false,
            ArrowRight,
            activeIndex: '1',
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
        Document: markRaw(Document),
    },

    // 加载函数
    mounted() {
        checkLogin(this)
    },

    // 监听函数
    watch: {
        'userdata.usertype'() {
            if (this.userdata.usertype !== 1) {
                this.$router.push('/home')
                ElMessage({
                    message: '你不是管理员，无法访问',
                    type: 'warning',
                })
            }
        }
    },

    methods: {
        before() {
        },

        handleSelect(key) {
            this.activeIndex = key
            const pathList = ['网站配置', '账号管理', '订单管理', '通知管理', '文章管理', '笔记管理']
            if (this.index_table.indexOf(pathList[key - 1]) === -1) {
                this.index_table.push(pathList[key - 1])
            }

        },

        // 动态编辑标签
        handleClose(tag) {
            this.index_table.splice(this.index_table.indexOf(tag), 1)
        },

        // 点击标签
        tagChange(tag) {
            console.log(tag)
            const pathList = ['网站配置', '账号管理', '订单管理', '通知管理', '文章管理', '笔记管理']
            this.activeIndex = (pathList.indexOf(tag)+1).toString()
        },

        // 退出登录函数
        toLogout() {
            sign({action: 'signout'}).then(res => {
                if (res) {
                    this.$router.push('/home')
                }
            })
        }
    }

}
</script>

<style lang="less" scoped>
.admin-view {
    display: flex;
    width: calc(85vw);
    margin: auto;

    .left {
        width: calc(10vw);

        .sf {
            height: 60px;
            text-align: center;
            font-size: 20px;
            font-weight: 400;
            line-height: 60px;
            padding: 5px;
            color: #eeeeee;
            background-color: #545c64;
            border-bottom: #eeeeee solid 2px;
        }
    }

    .right {
        width: calc(90vw);
        margin-left: 2px;

        .el-tag{
            position: relative;
            margin: 5px
        }
        .top {
            height: 60px;
            text-align: center;
            font-size: 20px;
            font-weight: 400;
            line-height: 60px;
            padding: 5px;
            color: #eeeeee;
            background-color: #545c64;
            border-bottom: #eeeeee solid 2px;
            display: flex;
            flex-flow: row nowrap;
            flex-direction: row;
            align-items: center;
            justify-content: space-between;

            .avatar {
                display: flex;
                flex-direction: row;
                align-items: center;
                color: #eeeeee;
                font-size: 20px;

                .username {
                    margin-left: 10px;
                    margin-right: 10px;
                }
            }
        }
    }
}
</style>
