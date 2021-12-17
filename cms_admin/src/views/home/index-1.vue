<template>
    <div class="home_main">
        <div class="navbar-top">
            <div class="row">
                <ul>
                    <li>
                        <service class="icon"/>
                        <span>+86 5507 6896 3326</span></li>
                    <li>
                        <message class="icon"/>
                        <span>cms@website.com</span>
                    </li>
                </ul>
                <ul>
                    <li><i class="el-ali-facebook-fill lis"></i></li>
                    <li><i class="el-ali-QQ-circle-fill lis"></i></li>
                    <li><i class="el-ali-email-fill lis"></i></li>
                    <li><i class="el-ali-bilibili-line lis"></i></li>
                </ul>
            </div>
        </div>

        <div class="menus">
            <el-image src="./login-logo.png" class="logo"></el-image>
            <div class="space"></div>
            <el-menu class="menu" mode="horizontal" active-text-color="#ffd04b" :ellipsis="false">
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
                <el-menu-item index="5">个人中心</el-menu-item>
            </el-menu>
        </div>

        <div class="banner-area">
            <img src="http://v.bootstrapmb.com/2021/6/qrmyy10242/assets/img/banner/5.png"/>
        </div>
    </div>
</template>

<script>
import {Service, Message,} from "@element-plus/icons"
import {markRaw} from "vue";

export default {
    name: "index-1",
    components: {Service: markRaw(Service), Message: markRaw(Message)}
}
</script>

<style lang="less">
.home_main {
    position: absolute;
    width: 100%;
    z-index: 99;
    background: #fff;

}

* {
    box-sizing: border-box;
    outline: none;
    -moz-osx-font-smoothing: grayscale;
    -webkit-font-smoothing: antialiased;
}

.navbar-top {
    padding: 10px 0 10px 0;
    background-image: linear-gradient(to right, #2878EB, #F129C9);

    .row {
        display: flex;
        flex-wrap: wrap;
        flex-direction: row;
        justify-content: space-around;
    }

    ul {
        margin: 10px;

        li {
            display: inline-block;
            list-style: none;
            margin-right: 25px;
            color: #fff;
            height: 30px;

            .icon {
                height: 18px;
                margin-right: 5px;
                margin-top: auto;
                margin-bottom: auto;
            }

            span {
                line-height: 30px;
                font-size: 16px;
            }

            .lis:hover {
                color: #77b2ef;
            }
        }
    }
}

.menus {
    display: flex;
    justify-content: space-evenly;
    padding: 8px;
    height: 74px;
    width: auto;

    .space {
        width: 20px;
    }

    .menu {
        width: auto;
    }

}

.banner-area {
    background: url("http://v.bootstrapmb.com/2021/6/qrmyy10242/assets/img/banner/2.png");
    padding: 245px 0 120px 0;

    img {
        position: absolute;
        left: -30px;
        top: 30%;
        transform: translateY(-50%);
        animation: img 3s infinite ease-in-out;
        vertical-align: middle;
        border-style: none;
        max-width: 100%;


    }

}

</style>
