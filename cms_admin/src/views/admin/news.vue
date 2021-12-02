<template>
    <el-table :data="tableData" stripe style="width: 100%" border max-height="600">
        <el-table-column prop="id" label="Id" sortable/>

        <el-table-column prop="title" label="Title">
            <template #default="scope">
                <el-popover effect="light" trigger="hover" placement="top">
                    <template #default>
                        <p>{{ scope.row.title }}</p>
                        <p></p>
                        <p>{{ scope.row.content }}</p>
                    </template>
                    <template #reference>
                        <div class="name-wrapper">
                            <el-tag size="medium">{{ scope.row.title }}</el-tag>
                        </div>
                    </template>
                </el-popover>
            </template>
        </el-table-column>

        <el-table-column prop="status" label="状态" :filters="[
                        { text: '禁用', value: 0 },
                        { text: '正常', value: 1 },
                        { text: '热点', value: 2 },]"
                         :filter-method="filterHandler">
            <template #default="scope">
                <el-slider v-model="scope.row.status" :max="2" show-input show-stops></el-slider>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
import request from "../../utils/request";
import {ElMessage} from "element-plus";

export default {
    name: "news",
    data() {
        return {
            tableData: [],
        }
    },
    mounted() {
        this.before()
    },

    methods: {
        before() {
            const that = this
            request.post('/api/notice/news', {
                action: 'list', news_type: 'ALL'
            }).then(res => {
                const data = res.data
                if (data['ret']===0){
                    that.tableData = data['retlist']
                }else {
                    ElMessage.error('服务器错误')
                }
            })
        },
        // 列表筛选
        filterHandler(value, row, column) {
            const property = column['property']
            return row[property] === value
        },
    }

}
</script>

<style scoped>

</style>
