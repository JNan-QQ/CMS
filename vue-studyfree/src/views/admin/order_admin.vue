<template>
    <div class="search-top">
        <el-input v-model="select_value" placeholder="请输入字段" clearable style="width: 50%;margin-right: 20px">
            <template #prepend>
                <el-select v-model="select_type" clearable placeholder="Select" style="width: 100px">
                    <el-option label="id" value="id"/>
                    <el-option label="订单号" value="orderNo"/>
                    <el-option label="用户名" value="user_id"/>
                    <el-option label="时间" value="create_time"/>
                </el-select>
            </template>
            <template #append>
                <el-button :icon="Search" @click="getOrderData"></el-button>
            </template>
        </el-input>
        <el-button type="primary" plain @click="" style="position: relative">添加</el-button>
    </div>
    <el-table :data="orderList" border class="table" v-loading="loading_table" element-loading-text="加载中...">
        <el-table-column prop="id" label="id" min-width="10%" sortable/>
        <el-table-column prop="orderNo" label="订单号" min-width="10%"/>
        <el-table-column prop="user__username" label="用户名" min-width="10%"/>
        <el-table-column prop="money" label="付款金额(元)" min-width="10%"/>
        <el-table-column prop="create_time" label="时间" min-width="10%"/>
        <el-table-column prop="status" label="订单状态" min-width="10%"/>
        <el-table-column label="操作" min-width="20%" #default="scope">
        </el-table-column>
    </el-table>
    <!--  分页  -->
    <pages :total="total" @get-data="getOrderData" :btn_background="false"></pages>
</template>

<script>
import {Edit, Loading, Search} from "@element-plus/icons";
import {markRaw} from "vue";
import {OrderApi} from "@/api/admin";
import Pages from "@/components/pages.vue"

export default {
    name: "order_admin",
    components: {Pages},
    data() {
        return {
            orderList: [],
            // 每页显示个数
            total: 0,
            // 选择字段
            select_type: '',
            // 字段值
            select_value: '',
            Search: markRaw(Search),
            Edit: markRaw(Edit),
            Loading: markRaw(Loading),
            loading_table: false
        }
    },
    mounted() {
        this.getOrderData()
    },
    methods: {
        getOrderData(current_page = 1, page_size = 10) {
            this.loading_table = true
            // 搜索过滤
            const search_items = {}
            if (this.select_type && this.select_value) {
                search_items[this.select_type] = this.select_value
            }
            // 发送列出账号请求
            OrderApi({
                search_items: search_items,
                action: 'list',
                pageSize: page_size,
                pageNum: current_page
            }).then(res => {
                if (res) {
                    this.orderList = res['retlist']
                    this.total = res['total']
                    this.loading_table = false
                }
            })
        },
    }
}
</script>

<style scoped>
.search-top {
    display: flex;
    align-items: center;
    margin-bottom: 3px
}

.table {
    min-height: 600px;
    padding: 10px;
    height: calc(72vh);
    overflow-y: scroll;
}
</style>
