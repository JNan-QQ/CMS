<template>
    <div class="content" style="display: flex;flex-direction: row;flex-wrap: wrap;">
        <el-carousel :interval="4000" type="card" style="width: 100%">
            <el-carousel-item v-for="item in pageImg" :key="item" style="height: auto;">
                <el-image :src="'/api'+item['img']" fit="fill"></el-image>
            </el-carousel-item>
        </el-carousel>

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
                that.pageImg = response['retlist']
            })

            request.post('/api/notice/news', {
                action: 'pageNews'
            }).then(function (response) {
                that.schoolTable = response['retlist']
                that.socTable = response['retlist']
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
