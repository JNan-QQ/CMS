<template>
    <div class="center_view">
        <div class="left">
            <div class="aviator">
                <el-avatar :src="userdata.aviator" :size="150"></el-avatar>
                <el-upload action="/api/common/other"
                           :data="{action:'uploadImg',file_type:'aviator',file_name:'img_aviator_'+userdata.user_id+'_.png'}"
                           :on-success="uploadImgSuccess"
                           :show-file-list="false"
                           accept="image/png, image/jpeg, image/jpg">
                    <el-button>更换头像</el-button>
                </el-upload>
            </div>
            <el-menu :default-active="activeIndex" @select="activeIndexes">
                <el-menu-item index="1">
                    <el-icon>
                        <InfoFilled/>
                    </el-icon>
                    <span>账号信息</span>
                </el-menu-item>
                <el-menu-item index="2">
                    <el-icon>
                        <Tickets/>
                    </el-icon>
                    <span>我的订单</span>
                </el-menu-item>
                <el-menu-item index="3">
                    <el-icon>
                        <MessageBox/>
                    </el-icon>
                    <span>通知中心</span>
                    <el-badge :value="messageNum" :max="10" style="display: flex;height:85%" v-if="messageNum!==0"/>
                </el-menu-item>
                <el-menu-item index="4">
                    <el-icon>
                        <setting/>
                    </el-icon>
                    <span>设置杂项</span>
                </el-menu-item>
                <el-menu-item index="5" v-if="userdata.usertype===1005||userdata.usertype===1">
                    <el-icon>
                        <star/>
                    </el-icon>
                    <span>服务配置</span>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="right">
            <div class="top-btn">
                <el-button :icon="Delete" circle @click="this.$router.go(-1);"></el-button>
            </div>
            <MyInfo v-if="activeIndex==='1'"></MyInfo>
            <OrderMy v-else-if="activeIndex==='2'"></OrderMy>
            <MessageMy v-else-if="activeIndex==='3'"></MessageMy>
            <ToolMy v-else-if="activeIndex==='4'"></ToolMy>
            <Services v-else-if="activeIndex==='5'"></Services>
        </div>
    </div>
</template>

<script>
import {Setting, InfoFilled, Tickets, MessageBox, Delete, Edit, Star} from "@element-plus/icons"
import {markRaw} from "vue"
import {checkLogin} from "@/api/Login"
import {ElMessage} from "element-plus"
import MyInfo from "./myInfo"
import MessageMy from "./message"
import OrderMy from "./order"
import Services from "./services"
import ToolMy from "./tool"
import {MessageApi} from "@/api/common";

export default {
    name: "index",
    data() {
        return {
            userdata: this.$store.state.userdata,
            activeIndex: "1",
            Delete: markRaw(Delete),
            messageNum: 0
        }
    },
    components: {Setting, InfoFilled, Tickets, MessageBox, Edit, Star, MyInfo, ToolMy, MessageMy, OrderMy, Services},
    mounted() {
        checkLogin(this)
        this.getIndex()
        MessageApi({action: 'newMessageNum'}).then(res => {
            if (res) {
                this.messageNum = res['num']
            }
        })
    },
    methods: {
        getIndex() {
            const index = this.$route.params.index
            if (index !== undefined) {
                this.activeIndex = index
            }
        },
        // 激活索引
        activeIndexes(index) {
            this.activeIndex = index
        },

        // 上传头像图片成功后修改头像
        uploadImgSuccess(response, file, fileList) {
            if (response['ret'] === 0) {
                this.userdata.aviator = 'api_file/' + response['url']
                ElMessage({
                    message: '修改成功，请刷新！',
                    type: 'success',
                })
            }
        },
    },
}
</script>

<style scoped lang="less">
.center_view {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: calc(80vh);
    margin: 10vh auto;

    .left, .right {
        background-color: #FFFFFF;
        position: relative;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: stretch;
    }

    .left {
        width: 220px;
        border-radius: 8px 0 0 8px;

        .aviator {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 10px;
            border-bottom: #105c94 solid 2px;

            .el-button {
                margin-top: 10px;
            }
        }

    }

    .right {
        width: 620px;
        margin-left: 3px;
        border-radius: 0 8px 8px 0;

        .top-btn {
            display: flex;
            justify-content: right;
            border-bottom: #105c94 solid 1px;

            .el-button {
                margin: 5px;
            }
        }
    }
}

</style>
