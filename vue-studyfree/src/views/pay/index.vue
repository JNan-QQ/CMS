<template>
    <div class="top">
        <el-icon @click="this.$router.go(-1);">
            <back/>
        </el-icon>
        <div>
            <span style="margin-right: 30px">服务期限：{{ userdata.deadline }}</span>
            <span>F：{{ userdata.coins }} 币</span>
        </div>
    </div>
    <div class="products">
        <el-card class="box-card">
            <template #header>
                <div class="card-header">
                    <span>充值F币</span>
                    <el-button class="button" @click="payF" :disabled="disablePay">确定</el-button>
                </div>
            </template>
            <div>
                <p>充值金额：
                    <el-input-number v-model="money"
                                     :min="1" :max="9999" size="small"
                                     :precision="2" :step="1"/>
                    　元
                </p>
                <p>Ｆ　　币：{{ Math.round(money * F * (1 + Z)) }}　币</p>
                <p>说　　明：{{ Z }}折扣</p>
            </div>
        </el-card>
        <el-card class="box-card" v-for="product in productsList">
            <template #header>
                <div class="card-header">
                    <span>{{ product['title'] }}</span>
                    <el-button class="button" @click="addTime(product['id'])">订购</el-button>
                </div>
            </template>
            <div>
                <p>时　　长：{{ product['timeDays'] }}　天</p>
                <p>价　　格：{{ product['price'] }}　币</p>
                <p>说　　明：{{ product['desc'] }}</p>
            </div>
        </el-card>
    </div>
</template>

<script>
import {getUserConfig} from "@/api/pay";
import {orderApi, productApi} from "@/api/pay";
import {ElMessage} from "element-plus";
import {CommonApi} from "@/api/common";
import {Back} from "@element-plus/icons";
import {checkLogin} from "@/api/Login";

export default {
    name: "index",
    data() {
        return {
            userdata:this.$store.state.userdata,
            productsList: [],
            money: 0,
            F: 500,
            Z: 1,
            disablePay:false,
        }
    },
    components: {Back},
    mounted() {
        checkLogin(this)
        getUserConfig(this)
        productApi({action: 'list'}).then(res => {
                if (res) {
                    this.productsList = res['retlist']
                }
            }
        )
        CommonApi({action: 'list_webConfig', title: 'pay'}).then(res => {
            if (res) {
                let ss = eval('(' + res['retlist'][0]['config'] + ')')
                this.F = parseInt(ss.F)
                this.Z = parseFloat(ss.Z)
                this.disablePay = ss.disablePay
            }
        })
    },
    methods: {
        payF() {
            orderApi({action: 'createOrder', money: this.money}).then(res => {
                    if (res) {
                        window.open(res['url'])
                    }
                }
            )
        },
        addTime(id) {
            productApi({action: 'addTime', 'product_id': id}).then(res => {
                    if (res) {
                        ElMessage({
                            message: '恭喜你购买成功',
                            type: 'success',
                        })
                    }
                }
            )
        }
    }
}
</script>

<style scoped lang="less">
.top {
    height: 60px;
    max-width: calc(80vw);
    margin: auto;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    position: relative;
    border-bottom: #e0dddd solid 2px;
    color: #eeeeee;
}

.products {
    display: flex;
    flex-flow: row wrap;
    flex-wrap: wrap;
    justify-content: flex-start;
    align-items: center;
    flex-direction: row;
    max-width: calc(75vw);
    margin: auto;

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .box-card {
        width: 30%;
        margin: 1%;

        p {
            margin-bottom: 5px;
        }

        .button {
            position: relative;
        }
    }
}

</style>
