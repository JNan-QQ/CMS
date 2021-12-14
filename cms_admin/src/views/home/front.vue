<template>
    <div class="content">

        <el-carousel :interval="4000" type="card" style="width: 100%">
            <el-carousel-item v-for="item in hotNewsData" :key="item" style="height: auto;">
                <el-image :src="'/api'+item['img']" fit="fill"></el-image>
            </el-carousel-item>
        </el-carousel>

        <div class="news">
            <div class="schoolNews">

                <el-row v-for="schoolNews in schoolTable" class="lines">
                    <el-col :span="16">
                        <span>{{ schoolNews['title'] }}</span>
                    </el-col>
                    <el-col :span="4">
                        <span>{{ schoolNews['author__realName'] }}</span>
                    </el-col>
                    <el-col :span="4">
                        <span>{{ schoolNews['create_time'] }}</span>
                    </el-col>
                </el-row>
            </div>
            <div class="socNews">
                <el-row v-for="socNews in socTable" class="lines">
                    <el-col :span="16">{{ socNews['title'] }}</el-col>
                    <el-col :span="4">{{ socNews['author__realName'] }}</el-col>
                    <el-col :span="4">{{ socNews['create_time'] }}</el-col>
                </el-row>
            </div>
        </div>
    </div>
</template>

<script>
import request from "../../utils/request";
import {listNewsHot, listNewsImg} from '../../api/News'

export default {
    name: "front",
    data() {
        return {
            schoolTable: [],
            socTable: [],
            hotNewsData: []
        }
    },
    mounted() {
        this.before()
    },
    methods: {
        before() {
            listNewsHot(this)
            listNewsImg(this)
        }
    }
}
</script>

<style scoped>
.el-carousel__item img {
    margin: auto;
    width: auto;
    height: auto;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}

.el-carousel__item:nth-child(2n + 1) {
    background-color: #d3dce6;
}

.table {
    display: flex;
    width: 100%;
}

.el-table {
    margin-left: 10px;
    margin-right: 10px;
}

.el-table-column {
    margin: auto;
}

.news {
    margin-top: 20px;
    border-top: 2px solid var(--el-border-color-base);
    display: flex;
}

.lines {
    border-style: inset;
    height: 30px
}

.schoolNews {
    margin-right: 3px;
    width: 50%;
    text-align: left;
}

.socNews {
    margin-left: 3px;
    width: 50%;
    text-align: left;
}

.el-col {
    white-space: nowrap; /*设置不换行*/
    overflow: hidden; /*设置隐藏*/
    text-overflow: ellipsis; /*设置隐藏部分为省略号*/
}


</style>
