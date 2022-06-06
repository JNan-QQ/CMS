<template>
    <div class="content">
        <div class="skill-top">
            <div class="carousel">
                <el-carousel :interval="4000" height="200px">
                    <el-carousel-item v-for="(item,index) in images" :key="index" style="text-align: center">
                        <el-image :src="item" fit="fill"></el-image>
                    </el-carousel-item>
                </el-carousel>
            </div>
            <div class="skill-menu">
                <el-menu
                    :default-active="activeIndex"
                    class="el-menu-demo"
                    mode="horizontal"
                    @select="handleSelect"
                >
                    <el-menu-item index="1">热门</el-menu-item>
                    <el-menu-item index="2">全部</el-menu-item>
                    <el-menu-item index="3" v-if="isLogin">我的收藏</el-menu-item>
                    <el-menu-item index="4" v-if="isLogin">发帖</el-menu-item>
                </el-menu>
                <el-input v-model="searchKey" placeholder="输入关键字......" size="small">
                    <template #append>
                        <el-button :icon="Search" size="small"/>
                    </template>
                </el-input>
            </div>
        </div>
        <div class="skill-view">
            <skill-list-view :mode="activeIndex" v-if="activeIndex!=='4'"></skill-list-view>
            <my-skill v-else></my-skill>
        </div>
    </div>

</template>

<script>
import {Search} from "@element-plus/icons";
import {markRaw} from "vue";
import SkillListView from "@/components/skillViewPage/skillListView";
import MySkill from "@/components/skillViewPage/mySkill";
import axios from "axios";

export default {
    name: "sillView",
    data() {
        return {
            activeIndex: '1',
            searchKey: '',
            Search: markRaw(Search),
            images: [
                'https://upload-bbs.mihoyo.com/upload/2020/07/21/21918678/7e624245423cbb6d3cce148c67d6db6f_5277841816657379233.jpg',
                'http://p5.qhimg.com/t015a7830c430ff61bb.jpg?size=1920x1080',
                'http://p4.qhimg.com/t01777f7c2055747c40.jpg?size=1162x727'
            ]

        }
    },
    components: {MySkill, SkillListView},
    computed: {
        isLogin: {
            get() {
                return this.$store.state.userdata.isLogin
            }
        }

    },
    methods: {
        handleSelect(index) {
            this.activeIndex = index
        },
    }
}
</script>

<style scoped lang="less">
.content {
    width: 100%;
    margin-top: 5px;
    border-top: #FFFFFF solid 1px;

    .skill-top {
        width: 1000px;
        margin: 20px auto auto;

        .skill-menu {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding-left: 5px;
            padding-right: 5px;
            background-color: #FFFFFF;
            height: 40px;
            border-bottom: #04121c solid 1px;

            .el-menu {
                height: 40px;
                width: 50%;
            }

            .el-input {
                width: 30%;
            }
        }
    }

    .skill-view {
        width: 1000px;
        margin: auto;
        background-color: #FFFFFF;
        min-height: calc(75vh - 100px);
    }

}


.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}
</style>
