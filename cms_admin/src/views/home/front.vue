<template>
    <div class="content">
        <div class="img">
            <el-carousel :interval="4000">
                <el-carousel-item v-for="item in hotNewsData" :key="item">
                    <el-image :src="'/api'+item['img']" fit="cover" style="height: 300px" @click="toNewsView(item.news)"></el-image>
                </el-carousel-item>
            </el-carousel>
        </div>

        <div class="schoolNews">
            <div class="table-title">校园实事</div>
            <el-row v-for="schoolNews in schoolTable" class="lines" @click="toNewsView(schoolNews.id)">
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
            <div class="table-title">社会热点</div>
            <el-row v-for="socNews in socTable" class="lines" @click="toNewsView(socNews.id)">
                <el-col :span="16">{{ socNews['title'] }}</el-col>
                <el-col :span="4">{{ socNews['author__realName'] }}</el-col>
                <el-col :span="4">{{ socNews['create_time'] }}</el-col>
            </el-row>
        </div>

        <div class="socNews">
            <div class="table-title">疫情防控</div>
            <el-row v-for="socNews in socTable" class="lines">
                <el-col :span="16">{{ socNews['title'] }}</el-col>
                <el-col :span="4">{{ socNews['author__realName'] }}</el-col>
                <el-col :span="4">{{ socNews['create_time'] }}</el-col>
            </el-row>
        </div>

    </div>
</template>

<script>
import request from "../../utils/request";
import {listNews, listNewsHot, listNewsImg} from '../../api/News'

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
        },
        // 新闻详情页面
        toNewsView(news_id){
            this.$router.push('/contentView?type=news&id='+news_id)
        },
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

/*界面样式*/
.content {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}

/*新闻列表样式*/
.lines {
    border-bottom: inset;
    height: 30px
}

/*各个模块大小*/
.img,.schoolNews,.socNews{
    width: 46%;
    margin: 2%;
    height: 300px;
}

/*新闻内容长度...*/
.el-col {
    white-space: nowrap; /*设置不换行*/
    overflow: hidden; /*设置隐藏*/
    text-overflow: ellipsis; /*设置隐藏部分为省略号*/
}

/*各个模块标题样式*/
.table-title{
    text-align: center;
    font-size: 26px;
    color: #77b2ef;
    height: 30px;
    margin-bottom: 3px;
    border-bottom: 1px solid var(--el-border-color-base);
}


</style>
