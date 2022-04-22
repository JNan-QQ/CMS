<template>
    <div class="content">
        <div v-if="userdata.usertype===1000">
            <span>开启高级模式：</span>
            <el-switch @change="changeUserType"
                       v-model="heightSwitch"
                       :disabled="heightSwitch"
                       inline-prompt
                       active-color="#13ce66"
                       inactive-color="#ff4949"
                       active-text="Y"
                       inactive-text="N">
            </el-switch>
        </div>
        <div v-else class="cdk">
            <span>CDK兑换：</span>
            <el-input v-model="cdk" placeholder="请输入CDK兑换码" :suffix-icon="Key"/>
            <el-button type="warning" @click="useCdk" :loading="cdkBtn">兑换</el-button>
        </div>
    </div>
</template>

<script>
import {ElMessage, ElMessageBox} from "element-plus";
import {CommonApi} from "@/api/common";
import {Key} from "@element-plus/icons";
import {markRaw} from "vue";
import {cdkApi} from "@/api/pay";


export default {
    name: "tool",
    data() {
        return {
            userdata: this.$store.state.userdata,
            heightSwitch: this.$store.state.userdata.usertype === 1005,
            Key: markRaw(Key),
            cdk: '',
            cdkBtn:false
        }
    },
    watch: {
        // 监听用户类型
        '$store.state.userdata.usertype'() {
            this.heightSwitch = this.$store.state.userdata.usertype === 1005
        },
    },
    components: {Key},
    methods: {
        // 改变用户类型
        changeUserType(val) {
            ElMessageBox.confirm(
                '确认开启高级功能? 开启后无法关闭',
                '提示',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                }
            ).then(() => {
                CommonApi({action: 'changeUserInfo', usertype: 1005}).then(res=>{
                    if (res){
                        ElMessage.success('用户权限升级成功！！！')
                    }
                })
            }).catch(() => {
                this.heightSwitch = false
            })
        },

        // 使用cdk
        useCdk() {
            this.cdkBtn = true
            cdkApi({action: 'useCdk', cdk: this.cdk}).then(res=>{
                if (res){
                    this.cdk = ''
                    ElMessage.success('CDK兑换成功！！！')
                }
                this.cdkBtn = false
            })
        },
    }
}
</script>

<style scoped lang="less">
.content {
    height: 100%;
    width: 100%;
    text-align: left;

    div {
        padding: 5px;
    }

    .cdk {
        display: flex;
        align-items: center;

        span {
            margin-left: 10px;
            margin-right: 5px;
        }

        .el-input {
            width: 40%;
            margin-right: 8px;
        }
    }
}
</style>