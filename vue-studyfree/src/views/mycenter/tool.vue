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
    </div>
</template>

<script>
import {ElMessageBox} from "element-plus";
import {CommonApi} from "@/api/common";

export default {
    name: "tool",
    data() {
        return {
            userdata: this.$store.state.userdata,
            heightSwitch: this.$store.state.userdata.usertype === 1005,
        }
    },
    watch: {
        // 监听用户类型
        '$store.state.userdata.usertype'() {
            this.heightSwitch = this.$store.state.userdata.usertype === 1005
        },
    },
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
                CommonApi({action: 'changeUserInfo', usertype: 1005})
            }).catch(() => {
                this.heightSwitch = false
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

    .four-top {
        border-bottom: #1E9FFF solid 1px;
        padding: 5px;
        display: flex;
        align-items: center;
    }
}
</style>