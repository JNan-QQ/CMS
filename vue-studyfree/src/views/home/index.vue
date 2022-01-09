<template>
    <div class="navbar">
        <div class="container">
            <el-image :src="require('../../assets/studyfree1.png')" fit="fill"
                      style="width: 180px; height: 38px"></el-image>
            <div class="navbar-collapse">
                <ul class="navbar-nav">
                    <li class="nav-item position-relative"><a>文章</a><i class="iconfont  ksd-bgd-left">热门</i></li>
                    <li class="nav-item position-relative"><a>笔记</a></li>
                    <li><a>技巧</a></li>
                    <li v-if="false"><a>工具</a></li>
                </ul>
                <router-link to="/login" v-if="!userdata.isLogin">
                    <el-button type="primary" :icon="Avatar">登陆</el-button>
                </router-link>
                <div class="inLogin" v-else>
                    <div class="inHome">
                        <el-icon>
                            <home-filled/>
                        </el-icon>
                        <span>进入首页</span></div>
                    <el-dropdown trigger="click">
                        <div class="drop">
                            <el-avatar :size="38"
                                       src="https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"
                            ></el-avatar>
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
                                                        <span class="ktext">关注</span>
                                                    </a>
                                                </li>
                                                <li class="num-items">
                                                    <a>
                                                        <span class="num ksd-num-count2">0</span>
                                                        <span class="ktext">粉丝</span>
                                                    </a>
                                                </li>
                                            </ul>
                                        </div>
                                        <div style="text-align: center;">
                                            <el-button>签到</el-button>
                                        </div>
                                    </div>
                                </el-dropdown-item>
                                <el-dropdown-item>
                                    <div class="login-items">
                                        <ul>
                                            <li class="items">
                                                <div>
                                                    <el-icon>
                                                        <home-filled/>
                                                    </el-icon>
                                                    个人中心
                                                </div>
                                                <span>普通用户</span>
                                            </li>
                                            <li class="items">
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
                                                <span>Lv0</span>
                                            </li>
                                            <li class="items">
                                                <div>
                                                    <el-icon>
                                                        <coin/>
                                                    </el-icon>
                                                    F币
                                                </div>
                                                <span>50 币</span>
                                            </li>
                                            <li class="items">
                                                <div>
                                                    <el-icon>
                                                        <trophy/>
                                                    </el-icon>
                                                    订购会员
                                                </div>
                                            </li>
                                            <li class="items">
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
                                <el-dropdown-item><el-icon><moon /></el-icon>退出登陆</el-dropdown-item>
                            </el-dropdown-menu>
                        </template>
                    </el-dropdown>
                </div>
            </div>
        </div>
    </div>
    <div class="main-view">
        <div class="product_name">
            <el-image :src="require('../../assets/studyfree_home.png')" fit="fill"
                      style="width: 360px;"></el-image>
        </div>
        <p class="product-desc">为每个想学习知识的人提供一个少走弯路的平台</p>
        <p class="product-desc product-desc1">生活明朗，万物可爱，人间值得，未来可期</p>
        <div class="button-area">
            <el-button :icon="Notebook" size="large" color="#28c58d">文章</el-button>
            <el-button :icon="Document" size="large" color="#4d2c8b">笔记</el-button>
            <el-button :icon="Flag" size="large" color="#b1149e">技巧</el-button>
        </div>
    </div>
    <footer class="blog-footer">
        <p>
            <a>关于我们</a>
            <span>|</span>
            <a>加入我们</a>
            <span>|</span>
            <a>联系我们</a>
        </p>
        <p>
            <span>EveryOne © 个人学习备忘网站 </span><a>待备案 - 20220122 </a>
        </p>
    </footer>
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
    Notebook,
    Position,
    Setting,
    Star,
    Trophy,
    Moon
} from '@element-plus/icons';
import {markRaw} from "vue";
import {checkLogin} from "../../api/Login";

export default {
    name: "index",
    data() {
        return {
            Avatar: markRaw(Avatar), Notebook: markRaw(Notebook), Document: markRaw(Document), Flag: markRaw(Flag),
            userdata: this.$store.state.userdata,
        }
    },
    components: {CaretBottom, HomeFilled, Cloudy, Star, Coin, Setting, Position, Trophy,Moon},
    mounted() {
        checkLogin(this)
    },
    methods: {}
}
</script>

<style lang="less">

.navbar {
    position: relative;
    text-align: center;
    height: 60px;

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
                color: #FFFFFF;

                .inHome {
                    margin-right: 60px;
                }

                .drop {
                    display: flex;
                    align-items: center;

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

                a:hover {
                    background-color: #1e9fff;
                }

                .ksd-bgd-left {
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

.main-view {
    position: absolute;
    left: 0;
    top: 44%;
    transform: translateY(-50%);
    box-sizing: border-box;
    max-width: 960px;
    text-align: center;
    padding: 40px;
    margin: 0 auto;
    right: 0;

    .product_name {
        display: inline-block;
    }

    .product-desc {
        height: 36px;
        font-size: 28px;
        font-family: Avenir-Medinum, serif;
        margin: 20px 10px 0;
        color: #FFFFFF;
    }

    .product-desc1 {
        font-size: 16px;
    }

    .button-area {
        font: 14px "Microsoft YaHei UI Light";
        margin: 55px 0 0;

        .el-button {
            margin-right: 10px;
            margin-left: 10px;
            padding: 0 40px;
            color: #FFFFFF;
        }
    }
}

.blog-footer {
    position: absolute;
    bottom: 5%;
    right: 0;
    left: 0;
    padding: 40px 16px;
    font-size: 12px;
    color: #FFFFFF;
    text-align: center;

    p {
        margin-top: 10px;

        span {
            margin-left: 10px;
            margin-right: 10px;
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
    .container, .container-lg, .container-md, .container-sm, .container-xl {
        max-width: 1140px;
    }
}


</style>
