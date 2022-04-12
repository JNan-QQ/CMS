<template>
    <div class="navbar">
        <div class="container">
            <el-image :src="require('../../assets/studyfree1.png')" fit="fill"
                      style="width: 180px; height: 38px"></el-image>
            <div class="navbar-collapse">
                <ul class="navbar-nav">
                    <router-link to="/Article">
                        <li @click="is_active='文章'">
                            <a :class="{ active: is_active==='文章' }">文章</a><i class="bgd-left">热门</i>
                        </li>
                    </router-link>
                    <router-link to="/Note">
                        <li @click="is_active='笔记'"><a :class="{ active: is_active==='笔记' }">笔记</a></li>
                    </router-link>
                    <router-link to="/Skill">
                        <li @click="is_active='技巧'"><a :class="{ active: is_active==='技巧' }">技巧</a></li>
                    </router-link>
                    <router-link to="/Tool">
                        <li v-if="userdata.isLogin" @click="is_active='工具'"><a
                            :class="{ active: is_active==='工具' }">工具</a></li>
                    </router-link>
                </ul>
                <router-link to="/login" v-if="!userdata.isLogin">
                    <el-button type="primary" :icon="Avatar">登陆</el-button>
                </router-link>
                <div class="inLogin" v-else>
                    <div class="inHome" v-if="inHome">
                        <el-icon>
                            <home-filled/>
                        </el-icon>
                        <router-link to="/home"><span>进入首页</span></router-link>
                    </div>
                    <router-link to="/admin" v-if="userdata.usertype===1" style="margin-right: 10px">
                        <span>进入后台</span>
                    </router-link>
                    <el-dropdown trigger="click">
                        <div class="drop">
                            <el-avatar :size="38" :src="userdata.aviator"></el-avatar>
                            <span>{{ userdata.username }}</span>
                            <el-icon>
                                <caret-bottom/>
                            </el-icon>
                        </div>
                        <template #dropdown>
                            <el-dropdown-menu style="width: 280px">
                                <el-dropdown-item>
                                    <div class="login-items">
                                        <div class="header-items mt-3">
                                            <ul>
                                                <li class="num-items">
                                                    <a>
                                                        <span class="num ksd-num-count6">0</span>
                                                        <span class="ktext">文章</span>
                                                    </a>
                                                </li>
                                                <li class="num-items">
                                                    <a>
                                                        <span class="num ksd-num-count1">0</span>
                                                        <span class="ktext">笔记</span>
                                                    </a>
                                                </li>
                                                <li class="num-items">
                                                    <a>
                                                        <span class="num ksd-num-count2">0</span>
                                                        <span class="ktext">关注</span>
                                                    </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div style="text-align: center;">
                                            <el-button @click="qd">{{ userdata.qd }}</el-button>
                                        </div>
                                    </div>
                                </el-dropdown-item>
                                <el-dropdown-item>
                                    <div class="login-items">
                                        <ul>
                                            <li class="items" @click="this.$router.push('/myCenter')">
                                                <div>
                                                    <el-icon>
                                                        <home-filled/>
                                                    </el-icon>
                                                    个人中心
                                                </div>
                                                <span v-if="userdata.usertype===1005">付费用户</span>
                                                <span v-else-if="userdata.usertype===1">管理员</span>
                                                <span v-else>普通用户</span>
                                            </li>
                                            <li class="items" v-if="false">
                                                <div>
                                                    <el-icon>
                                                        <cloudy/>
                                                    </el-icon>
                                                    获取数字账号
                                                </div>
                                            </li>
                                            <li class="items">
                                                <div>
                                                    <el-icon>
                                                        <star/>
                                                    </el-icon>
                                                    等级
                                                </div>
                                                <span>Lv{{ userdata.lv }}</span>
                                            </li>
                                            <li class="items">
                                                <div>
                                                    <el-icon>
                                                        <coin/>
                                                    </el-icon>
                                                    F币
                                                </div>
                                                <span>{{ userdata.coins }} 币</span>
                                            </li>
                                            <li class="items" v-if="userdata.usertype===1 || userdata.usertype===1005"
                                                @click="this.$router.push('/pay')">
                                                <div>
                                                    <el-icon>
                                                        <trophy/>
                                                    </el-icon>
                                                    订购会员
                                                </div>
                                            </li>
                                            <li class="items" v-if="false">
                                                <div>
                                                    <el-icon>
                                                        <position/>
                                                    </el-icon>
                                                    分享推广
                                                </div>
                                            </li>
                                            <li class="items">
                                                <div>
                                                    <el-icon>
                                                        <setting/>
                                                    </el-icon>
                                                    个人设置
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </el-dropdown-item>
                                <el-dropdown-item @click="logout">
                                    <el-icon>
                                        <moon/>
                                    </el-icon>
                                    退出登陆
                                </el-dropdown-item>
                            </el-dropdown-menu>
                        </template>
                    </el-dropdown>
                </div>
            </div>
        </div>
    </div>
    <router-view></router-view>

</template>

<script>
import {
    Avatar,
    CaretBottom,
    Cloudy,
    Coin,
    Document,
    Flag,
    HomeFilled,
    Moon,
    Notebook,
    Position,
    Setting,
    Star,
    Trophy
} from '@element-plus/icons';
import {markRaw} from "vue";
import {checkLogin, sign} from "@/api/Login";
import {getUserConfig} from "@/api/pay";
import {qianDao} from "@/api/common";

export default {
    name: "index",
    data() {
        return {
            Avatar: markRaw(Avatar), Notebook: markRaw(Notebook), Document: markRaw(Document), Flag: markRaw(Flag),
            userdata: this.$store.state.userdata,
            inHome: false,
            is_active: '文章'
        }
    },
    components: {Document, CaretBottom, HomeFilled, Cloudy, Star, Coin, Setting, Position, Trophy, Moon},
    mounted() {
        checkLogin(this)
        this.jumpUrl()
        getUserConfig(this)
    },
    watch: {
        $route() {
            const url = this.$route.fullPath
            this.$store.commit('upDataUrl', url)
            console.log(url)
            this.inHome = url !== '/home'
        },
    },
    methods: {
        logout() {
            sign({action: 'signout'}).then(res => {
                if (res) {
                    checkLogin(this)
                }
            })
        },
        jumpUrl() {
            if (this.$route.path === '/') {
                this.$router.push('/home')
            } else {
                this.inHome = this.$route.path !== '/home';
            }
        },
        qd() {
            qianDao(this)
        }
    }
}
</script>

<style lang="less">

a:link, a:visited {
    text-decoration: none; /*超链接无下划线*/
}

.navbar {
    position: sticky;
    text-align: center;
    height: 60px;
    color: #FFFFFF;
    top: 0;

    .container {
        width: 100%;
        padding-right: 15px;
        padding-left: 15px;
        margin-right: auto;
        margin-left: auto;
        display: flex;
        padding-top: 15px;

        .navbar-collapse {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;

            .inLogin {
                display: flex;
                align-items: center;
                flex-direction: row;

                .inHome {
                    margin-right: 60px;
                    display: flex;
                    align-items: center;

                    span {
                        color: #FFFFFF;
                        margin-left: 5px;
                        font-size: 14px;
                    }

                }

                .drop {
                    display: flex;
                    align-items: center;
                    color: #FFFFFF;

                    span {
                        margin-left: 3px;
                        margin-right: 5px;
                    }
                }
            }

        }

        .navbar-nav {
            display: -ms-flexbox;
            -ms-flex-direction: column;
            flex-direction: column;
            list-style: none;

            li {
                display: inline;
                margin-block-start: 1em;
                margin-block-end: 1em;
                margin-inline-start: 0;
                margin-inline-end: 0;
                padding-inline-start: 40px;
                margin-left: 5px;
                margin-right: 5px;
                -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
                line-height: 38px;
                color: #FFFFFF !important;

                a {
                    font-size: 14px;
                    font-weight: 400;
                    border-radius: 10px;
                    padding: 4px 22px;

                }

                a.active{
                    color: #1E9FFF;
                }

                a:hover {
                    background-color: #1e9fff;
                }

                .bgd-left {
                    position: relative;
                    right: 26px;
                    top: -10px;
                    transform: scale(0.82);
                    font-size: 12px !important;
                    border: 1px solid #eee;
                    border-radius: 10px;
                    background: red;
                    color: #fff;
                    padding: 0 6px;
                    text-align: center;
                    font-style: initial;
                }
            }
        }

    }
}


.login-items {
    border-bottom: 1px solid #eee;
    padding: 8px 6px;
    width: 100%;

    .header-items {
        margin: 6px;
        overflow: hidden;
        margin-top: 1rem !important;


        .num-items {
            float: left;
            width: 33.33333%;
            text-align: center;
            transition: 60ms linear;
            padding: 5px 0;
            font-weight: 400;
            list-style: none;

            :hover {
                color: #04121c;
            }

            span {
                display: block;
                font: 14px "微软雅黑";
            }

            .num {
                font-size: 18px;
                margin-bottom: 2px;
            }

        }
    }

    .items {
        cursor: pointer;
        overflow: hidden;
        list-style: none;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;

        :hover {
            color: #04121c;
        }

        a {
            font-size: 12px;
            padding: 8px;
            font-weight: 400;
            cursor: pointer;
            display: flex;
            transition: 60ms linear;
        }
    }

}

@media (min-width: 992px) {
    .navbar-expand-lg > .container, .navbar-expand-lg > .container-fluid, .navbar-expand-lg > .container-lg, .navbar-expand-lg > .container-md, .navbar-expand-lg > .container-sm, .navbar-expand-lg > .container-xl {
        -ms-flex-wrap: nowrap;
        flex-wrap: nowrap;
    }
}

@media (min-width: 1200px) {
    .container, .container-lg, .container-md, .container-sm, .container-xl, .courseListBox {
        max-width: 1140px;
    }
}


</style>
