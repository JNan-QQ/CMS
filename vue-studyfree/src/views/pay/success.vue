<template>
    <div class="top">
        <el-icon @click="close">
            <back/>
        </el-icon>
        <el-button type="primary">Download&nbsp;<el-icon>
            <Download/>
        </el-icon>
        </el-button>
    </div>
    <el-card class="payView">
        <div class="payTop">
            <el-icon :size="36" color="#228800">
                <circle-check/>
            </el-icon>
            <span>您已成功付款</span>
        </div>
        <div class="payInfo">
            <el-form label-width="120px">
                <el-form-item label="商品订单：">
                    <span>{{ orderNo }}</span>
                    <el-tooltip content="复制订单号" effect="light">
                        <el-icon class="icon" @click="copy">
                            <copy-document/>
                        </el-icon>
                    </el-tooltip>
                </el-form-item>
                <el-form-item label="支付金额：">
                    <span class="payedInfoPrice">￥{{ money }}</span>
                </el-form-item>
                <el-form-item label="商品名称：">
                    <span>{{ coins }}&nbsp;F币付费</span>
                </el-form-item>
                <el-form-item label="用户名：">
                    <span>{{ username }}</span>
                </el-form-item>
                <el-form-item label="支付时间：">
                    <span>{{ new Date(pay_time) }}</span>
                </el-form-item>
            </el-form>
        </div>
        <div class="warning">
            <el-icon :size="16" color="#ebd2a6">
                <warning/>
            </el-icon>
            <span>若有疑问请与客服联系，我们将尽快为你提供服务！</span>
        </div>
    </el-card>
</template>

<script>
import {CircleCheck, Warning, CopyDocument, Back, Download} from "@element-plus/icons";
import {checkLogin} from "@/api/Login";
import {orderApi} from "@/api/pay";
import {ElNotification} from "element-plus";

export default {
    name: "success",
    data() {
        return {
            orderNo: '',
            money: 0,
            pay_time: '',
            username: '',
            coins: 0
        }
    },
    components: {CircleCheck, Warning, CopyDocument, Back, Download},
    mounted() {
        checkLogin(this)
        orderApi({action: 'payResult', flg: true}).then(res => {
            if (res['flg']) {
                const order = res['info']
                this.orderNo = order['orderNo']
                this.money = order['money']
                this.pay_time = order['time']
                this.username = order['username']
                this.coins = order['coins']

            } else {
                this.$router.push('/404')
            }
        })
    },
    methods: {
        copy() {
            navigator.clipboard.writeText(this.orderNo)
            ElNotification({
                title: '剪切板',
                message: '订单号已复制到了剪贴板中！！！',
                type: 'success',
                duration: 2000
            })
        },
        close() {
            if (navigator.userAgent.indexOf("Firefox") !== -1 || navigator.userAgent.indexOf("Chrome") !== -1) {
                window.location.href = "about:blank";
                window.close();
            } else {
                window.opener = null;
                window.open("", "_self");
                window.close();
            }
        }
    }
}
</script>

<style scoped lang="less">
.top {
    height: 60px;
    max-width: 1100px;
    margin: auto;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    position: relative;
    border-bottom: #e0dddd solid 2px;
    color: #eeeeee;
}

.payView {
    border: 1px solid #D4D4D4;
    max-width: 1013px;
    margin: 30px auto 20px auto;
    position: relative;

    .payTop {
        background-color: #ECFFDC;
        padding: 17px 25px 17px 25px;
        display: flex;
        align-items: center;

        span {
            font-weight: bold;
            font-size: 14px;
            margin-left: 10px;
        }

    }

    .payInfo {
        padding: 26px 35px;

        .el-form-item {
            margin-bottom: 10px;

            .payedInfoPrice {
                color: #B10000;
                font-weight: bold;
                font-size: 14px;
                font-family: arial, serif;
            }

            .icon {
                margin-left: 5px;
                color: #FFFFFF;

                :hover {
                    color: #0bee8c;
                }
            }
        }
    }

    .warning {
        display: flex;
        align-items: center;
        border-top: #0bee8c solid 1px;
        padding-top: 3px;

        span {
            font-size: 10px;
            margin-left: 5px;
            color: #bfbcbc;
        }
    }
}

</style>