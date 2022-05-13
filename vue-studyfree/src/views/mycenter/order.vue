<template>
    <div class="content">
        <el-empty :image-size="200" v-if="!orderList"></el-empty>
        <el-table :data="orderList" stripe v-else max-height="670" v-loading="loading_table"
                  element-loading-text="加载中..." class="table">
            <el-table-column type="index" width="50"/>
            <el-table-column prop="orderNo" label="订单编号" width="150"/>
            <el-table-column prop="create_time" label="创建时间" width="170"/>
            <el-table-column prop="money" label="订单金额 / 元" width="130"/>
            <el-table-column label="订单状态" width="120">
                <template #default="scope">
                    <span style="color: green" v-if="scope.row.status==='已付款'">已付款</span>
                    <span style="color: orange" v-else-if="scope.row.status==='未付款'" title="点击支付"
                          @click="repay(scope.row.orderNo)">未支付</span>
                    <span style="color: darkgray" v-else-if="scope.row.status==='已关闭'">已关闭</span>
                    <span style="color: #f68080" v-else-if="scope.row.status==='已退款'">已退款</span>
                </template>
            </el-table-column>
        </el-table>
        <!--    翻页      -->
        <pages :total="total" @get-data="getOrderData"></pages>
    </div>
</template>

<script>
import {orderApi} from "@/api/pay";
import Pages from '@/components/pages.vue'

export default {
    name: "order",
    data() {
        return {
            orderList: [],
            // 翻页
            total: 0,
            loading_table: false
        }
    },
    components: {Pages},
    mounted() {
        this.getOrderData()
    },
    methods: {
        // 订单列表
        getOrderData(current_page = 1, page_size = 10) {
            this.loading_table = true
            orderApi({action: 'list', pageSize: page_size, pageNum: current_page}).then(res => {
                if (res) {
                    this.orderList = res['retlist']
                    this.total = res['total']
                    this.loading_table = false
                }
            })
        },
        // 订单重新付款
        repay(orderNo) {
            orderApi({action: 'repay', orderNo: orderNo}).then(res => {
                if (res) {
                    window.open(res['url'])
                }
            })
        },
    }
}
</script>

<style scoped lang="less">
.content {
    height: 100%;
    width: 100%;
    text-align: center;

    .table {
        height: calc(72vh);
        overflow-y: scroll;
    }

    .table::-webkit-scrollbar {
        display: none; /* Chrome Safari */
    }
}
</style>