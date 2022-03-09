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
        <!--        <el-button type="success" plain size="small" @click="addMost">批量添加</el-button>-->
    </div>
    <el-table :data="orderList.slice((currentPage-1)*pageSize,currentPage*pageSize)" border class="table">
        <el-table-column prop="id" label="id" min-width="10%" sortable/>
        <el-table-column prop="orderNo" label="订单号" min-width="10%"/>
        <el-table-column prop="user__username" label="用户名" min-width="10%"/>
        <el-table-column prop="money" label="付款金额(元)" min-width="10%"/>
        <el-table-column prop="create_time" label="时间" min-width="10%"/>
        <el-table-column prop="status" label="订单状态" min-width="10%"/>
        <el-table-column label="操作" min-width="20%" #default="props">
            <!--            <el-button type="primary" :icon="Edit" circle @click="editBtnFunction(props.row)"></el-button>-->
            <!--            <el-button type="success" :icon="Loading" circle @click="resetPassword(props.row.id)"></el-button>-->
            <!--            <el-button type="danger" :icon="Delete" circle @click="deleteAccount(props.row)"></el-button>-->
        </el-table-column>
    </el-table>
    <div class="page">
        <el-pagination
            background
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[5,10,20]"
            :page-size="pageSize"
            layout="sizes, prev, pager, next, jumper, total"
            :total="orderList.length">
        </el-pagination>
    </div>
</template>

<script>
import {Edit, Loading, Search} from "@element-plus/icons";
import {markRaw} from "vue";
import {OrderApi} from "@/api/admin";

export default {
    name: "order_admin",
    components: {},
    data() {
        return {
            orderList: [],
            // 每页显示个数
            pageSize: 5,
            // 选择的页数
            currentPage: 1,
            // 选择字段
            select_type: '',
            // 字段值
            select_value: '',
            Search: markRaw(Search),
            Edit: markRaw(Edit),
            Loading: markRaw(Loading),
        }
    },
    mounted() {
        this.getOrderData()
    },
    methods: {
        getOrderData() {
            // 搜索过滤
            const search_items = {}
            if (this.select_type && this.select_value) {
                search_items[this.select_type] = this.select_value
            }
            // 发送列出账号请求
            OrderApi({search_items: search_items, action: 'list'}).then(res => {
                if (res) {
                    this.orderList = res['retlist']
                }
            })
        },
        //每页条数改变时触发 选择一页显示多少行
        handleSizeChange(val) {
            this.currentPage = 1;
            this.pageSize = val;
        },
        //当前页改变时触发 跳转其他页
        handleCurrentChange(val) {
            this.currentPage = val;
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
}

/*分页模块*/
.page {
    text-align: center;
    margin: 10px auto auto;
    position: relative;
}
</style>
