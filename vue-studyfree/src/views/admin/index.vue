<template>
    <div class="admin-top">
        <div class="admin-top1">
            <div class="sf">SF-ADMIN</div>
            <div class="top">
                <div style="display:flex">
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
        </div>
    </div>
    <div class="admin-view">
        <div class="left">
            <el-menu active-text-color="#ffd04b" background-color="#545c64" :collapse="isCollapse" :router="true"
                     text-color="#fff" @select="handleSelect" :default-active="activeIndex">
                <el-menu-item index="/">
                    <el-icon>
                        <setting/>
                    </el-icon>
                    <template #title>网站配置</template>
                </el-menu-item>
                <el-menu-item index="/admin/account">
                    <el-icon>
                        <user/>
                    </el-icon>
                    <template #title>账号管理</template>
                </el-menu-item>
                <el-menu-item index="/">
                    <el-icon>
                        <notification/>
                    </el-icon>
                    <template #title>订单管理</template>
                </el-menu-item>
                <el-menu-item index="/">
                    <el-icon>
                        <message/>
                    </el-icon>
                    <template #title>通知管理</template>
                </el-menu-item>
                <el-menu-item index="/">
                    <el-icon>
                        <document/>
                    </el-icon>
                    <template #title>文章管理</template>
                </el-menu-item>
                <el-menu-item index="/">
                    <el-icon>
                        <notebook/>
                    </el-icon>
                    <template #title>笔记管理</template>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="right">
            <!--            <el-icon @click="this.isCollapse=!this.isCollapse">-->
            <!--                <d-arrow-left style="width: 20px;height: 20px"/>-->
            <!--            </el-icon>-->
            <el-tag v-for="tag in index_table" :key="tag.path" closable :type="tps[Math.round(Math.random() * tps.length)]"
                    @close="handleClose(tag)" @click="tagChange(tag)">
                <router-link :to="tag.path">{{ tag.name }}</router-link>
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
            activeIndex: '/admin',
            tps: ['success', '', 'danger', 'warning', 'info'],
            // 面包学导航
            index_page: [],
            // 标签页
            index_table: [],
            activeName: '',
            pathList : {
                '/1': '网站配置',
                "/admin/account": "账号管理",
                '/3': '订单管理',
                '/4': '通知管理',
                '/5': '文章管理',
                '/6': '笔记管理',
            }
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
        },

    },

    methods: {
        before() {
        },

        handleSelect(key) {
            this.activeIndex = key
            const dict = {
                path:key,
                name:this.pathList[key]
            }
            if (this.index_table.indexOf(dict) === -1) {
                this.index_table.push(dict)
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
            this.activeIndex = (pathList.indexOf(tag) + 1).toString()
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

.admin-top {
    height: 60px;
    background-color: #545c64;
    border-bottom: #eeeeee solid 2px;

    .admin-top1 {
        display: flex;
        width: calc(80vw);
        justify-content: space-between;
        align-items: center;
        margin: auto;
        height: 60px;

        .sf {
            text-align: center;
            font-size: 20px;
            font-weight: 400;
            line-height: 60px;
            padding: 5px;
            color: #eeeeee;
            width: calc(10vw);

        }

        .top {
            text-align: center;
            font-size: 20px;
            font-weight: 400;
            line-height: 60px;
            padding: 5px;
            color: #eeeeee;

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

.admin-view {
    display: flex;
    width: calc(80vw);
    margin: auto;

    .left {
        width: calc(10vw);
        height: 100%;

    }

    .right {
        width: 100%;
        margin-left: 2px;

        .el-tag {
            position: relative;
            margin: 5px
        }

    }
}

</style>
