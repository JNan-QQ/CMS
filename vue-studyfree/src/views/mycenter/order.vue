<template>
    <div class="content">
        <el-empty :image-size="200" v-if="!orderList"></el-empty>
        <el-table :data="orderList" stripe v-else max-height="670">
            <el-table-column type="index" width="50" index="1"/>
            <el-table-column prop="orderNo" label="订单编号" width="150"/>
            <el-table-column prop="create_time" label="创建时间" width="170"/>
            <el-table-column prop="money" label="订单金额 / 元" width="130"/>
            <el-table-column prop="status" label="订单状态" width="120"/>
        </el-table>
    </div>
</template>

<script>
import {orderApi} from "@/api/pay";

export default {
    name: "order",
    data() {
        return {
            orderList: []
        }
    },
    mounted() {
        this.getOrderApi()
    },
    methods: {
        // 订单列表
        getOrderApi() {
            orderApi({action: 'list'}).then(res => {
                if (res) {
                    this.orderList = res['retlist']
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
}
</style>