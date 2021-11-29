<template>
    <div class="content">
        <el-carousel :interval="4000" type="card" height="200px">
            <el-carousel-item v-for="item in pageImg" :key="item">
                <el-image :src="item['img']" fit="fit"></el-image>
            </el-carousel-item>
        </el-carousel>
        <div class="table">
            <el-table :data="schoolTable" stripe>
                <el-table-column prop="title"/>
                <el-table-column prop="author__realName"/>
                <el-table-column prop="create_time"/>
            </el-table>

            <el-table :data="socTable" stripe>
                <el-table-column prop="title"/>
                <el-table-column prop="author__realName"/>
                <el-table-column prop="create_time"/>
            </el-table>
        </div>

    </div>
</template>

<script>
import request from "../../utils/request";

export default {
    name: "front",
    data() {
        return {
            schoolTable: [],
            socTable: [],
            pageImg: []
        }
    },
    mounted() {
        this.getHomeInfo()
    },
    methods: {
        getHomeInfo() {
            const that = this
            request.post('/api/notice/news', {
                action: 'pageImg'
            }).then(function (response) {
                that.pageImg = response.data['retlist']
            })

            request.post('/api/notice/news', {
                action: 'pageNews'
            }).then(function (response) {
                that.schoolTable = response.data['retlist']
                that.socTable = response.data['retlist']
            })
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


</style>