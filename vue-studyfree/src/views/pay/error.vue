<template>
    <div class="top">
        <el-icon @click="close">
            <back/>
        </el-icon>
    </div>
    <el-card class="payView">
        <div class="payTop">
            <el-icon :size="36" color="#B10000">
                <circle-close/>
            </el-icon>
            <span>您的付款过程看起来出现了问题</span>
        </div>
        <div class="payInfo">
            <p>{{ username }},&nbsp;{{ getTime() }}</p><br>
            <p style="text-indent:2em;">
                <span>你的订单：<strong @click="copy" title="点击复制">{{ orderNo }}</strong>&nbsp;支付过程中出现了问题，后台显示</span>
                <span v-if="status===1">订单已经支付成功，请到
                    <a @click="this.$router.push({name:'myCenter',params:{index:'2'}})" style="color: #1E9FFF"
                       title="前往订单界面">订单</a>
                    界面查看、核实。
                </span>
                <span v-if="status===0">订单未支付，请稍后重试，如果你已支付成功，请联系管理员核实。</span>
            </p><br>
            <p>谢谢理解！</p><br><br>
            <p style="text-align: right">studyFree服务系统</p>
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

import {Back, CircleClose, CopyDocument, Download, Warning} from "@element-plus/icons";
import {orderApi} from "@/api/pay";
import {ElNotification} from "element-plus";

export default {
    name: "error",
    data() {
        return {
            orderNo: '',
            pay_time: '',
            username: '',
            status: 0
        }
    },
    components: {CircleClose, Warning, CopyDocument, Back, Download},
    mounted() {
        orderApi({action: 'payResult', flg: false}).then(res => {
            if (res['flg']) {
                const order = res['info']
                this.orderNo = order['orderNo']
                this.pay_time = order['time']
                this.username = order['username']
                this.status = order['status']
            } else {
                this.$router.push('/404')
            }
        })
    },
    methods: {
        getTime() {
            let date = new Date();
            let hoursTip = ''
            if (date.getHours() >= 0 && date.getHours() < 12) {
                hoursTip = "上午好!"
            } else if (date.getHours() >= 12 && date.getHours() < 18) {
                hoursTip = "下午好!"
            } else {
                hoursTip = "晚上好!"
            }
            return hoursTip
        },
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
        background-color: #fff5dc;
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