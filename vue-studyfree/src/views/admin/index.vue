<template>
    <div class="admin-top">
        <div class="admin-top1">
            <div class="sf">SF-ADMIN</div>
            <div class="top">
                <el-breadcrumb :separator-icon="ArrowRight" style="margin-left: 10px;font-size: 20px">
                    <el-breadcrumb-item v-for="page in index_page">{{ page }}</el-breadcrumb-item>
                </el-breadcrumb>
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
            <el-menu active-text-color="#ffd04b" background-color="#545c64" :collapse="isCollapse"
                     text-color="#fff" @select="handleSelect" :default-active="activeIndex">
                <el-menu-item index="1">
                    <el-icon>
                        <setting/>
                    </el-icon>
                    <span>网站配置</span>
                </el-menu-item>
                <el-menu-item index="2">
                    <el-icon>
                        <user/>
                    </el-icon>
                    <span>账号管理</span>
                </el-menu-item>
                <el-menu-item index="3">
                    <el-icon>
                        <notification/>
                    </el-icon>
                    <span>订单管理</span>
                </el-menu-item>
                <el-menu-item index="4">
                    <el-icon>
                        <message/>
                    </el-icon>
                    <span>通知管理</span>
                </el-menu-item>
                <el-menu-item index="5">
                    <el-icon>
                        <document/>
                    </el-icon>
                    <span>文章管理</span>
                </el-menu-item>
                <el-menu-item index="6">
                    <el-icon>
                        <notebook/>
                    </el-icon>
                    <span>笔记管理</span>
                </el-menu-item>
                <el-menu-item index="7">
                    <el-icon>
                        <key/>
                    </el-icon>
                    <span>CDK</span>
                </el-menu-item>
                <el-menu-item index="100" v-if="activeIndex==='100'">
                    <el-icon>
                        <grape/>
                    </el-icon>
                    <span>欢迎页面</span>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="right">
            <el-tag v-for="tag in index_table" :key="tag" closable :type="tps[Math.round(Math.random() * tps.length)]"
                    @close="handleClose(tag)" @click="tagChange(tag)">
                {{ tag }}
            </el-tag>
            <Config_admin ref="config_admin" v-if="activeIndex==='1'"></Config_admin>
            <Account_admin ref="account_admin" v-else-if="activeIndex==='2'"></Account_admin>
            <Order_admin ref="order_admin" v-else-if="activeIndex==='3'"></Order_admin>
            <Message_admin ref="message_admin" v-else-if="activeIndex==='4'"></Message_admin>
            <Article_admin ref="article_admin" v-else-if="activeIndex==='5'"></Article_admin>
            <Notebook_admin ref="notebook_admin" v-else-if="activeIndex==='6'"></Notebook_admin>
            <Cdk_admin ref="cdk_admin" v-else-if="activeIndex==='7'"></Cdk_admin>
            <div v-else-if="activeIndex==='100'" class="welcome"><span>欢迎登录后台系统</span></div>
        </div>
    </div>
</template>

<script>
import {
    ArrowDown, ArrowRight, Close, DArrowLeft, Flag, Headset, Document,
    Message, Notebook, Notification, Setting, User, Grape, Key
} from "@element-plus/icons"
import {markRaw} from "vue"
import {checkLogin, sign} from "@/api/Login";
import Account_admin from "./account_admin";
import Config_admin from "./config_admin";
import Order_admin from "./order_admin";
import Message_admin from "./message_admin";
import Article_admin from "./article_admin";
import Notebook_admin from "./notebook_admin";
import Cdk_admin from "./cdk_admin";

export default {
    name: 'admin',
    data() {
        return {
            userdata: this.$store.state.userdata,
            isCollapse: false,
            ArrowRight,
            activeIndex: '100',
            tps: ['success', '', 'danger', 'warning', 'info'],
            // 面包学导航
            index_page: [],
            // 标签页
            index_table: [],
            activeName: '',
            pathList: ['网站配置', "账号管理", '订单管理', '通知管理', '文章管理', '笔记管理','CDK'],

        }
    },
    components: {
        Key,
        Grape,
        Notebook_admin,
        Article_admin,
        Message_admin,
        Order_admin,
        Config_admin,
        Account_admin,
        Cdk_admin,
        User,
        Setting,
        Notebook,
        Headset: markRaw(Headset),
        Flag: markRaw(Flag),
        Message,
        Notification,
        DArrowLeft: markRaw(DArrowLeft), ArrowRight: markRaw(ArrowRight),
        ArrowDown: markRaw(ArrowDown),
        Close: markRaw(Close),
        Document,
    },

    // 加载函数
    mounted() {
        checkLogin(this)
    },

    methods: {
        handleSelect(key) {
            this.activeIndex = key
            if (this.index_table.indexOf(this.pathList[key - 1]) === -1) {
                this.index_table.push(this.pathList[key - 1])
            }

        },

        // 动态编辑标签
        handleClose(tag) {
            this.index_table.splice(this.index_table.indexOf(tag), 1)
        },

        // 点击标签
        tagChange(tag) {
            this.activeIndex = (this.pathList.indexOf(tag) + 1).toString()
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

        .welcome {
            width: 100%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;

            span {
                font-size: 40px;
                color: #e8ee67;
            }
        }

    }
}
</style>
