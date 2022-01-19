<template>
    <div class="center_view">
        <div class="left">
            <div class="aviator">
                <el-avatar :src="userdata.aviator" :size="150"></el-avatar>
                <el-button>更换头像</el-button>
            </div>
            <el-menu default-active="1" @select="activeIndexes">
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
                </el-menu-item>
                <el-menu-item index="4">
                    <el-icon>
                        <setting/>
                    </el-icon>
                    <span>设置-杂项</span>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="right">
            <div class="top-btn">
                <el-button :icon="Delete" circle @click="this.$router.go(-1);"></el-button>
            </div>
            <div v-if="activeIndex==='1'" class="content one">
                <el-card class="box-card">
                    <template #header>
                        <div class="card-header">
                            <span>个人信息</span>
                            <el-button class="button" type="text">重置密码</el-button>
                        </div>
                    </template>
                    <div class="item">
                        <span>用户名：</span><span class="item-content username">{{ userdata.username }}</span>
                    </div>
                    <div class="item">
                        <span>姓　名：</span><span class="item-content realName" v-if="!editRealName">{{
                            userdata.realName
                        }}</span>
                        <div style="display: flex" v-if="editRealName">
                            <el-input v-model="newUserdata.realName"></el-input>
                            <el-button type="success" :icon="Check"></el-button>
                            <el-button type="danger" :icon="Close" @click="editRealName=false;"></el-button>
                        </div>
                        <el-icon style="margin-left: 10px;color: #105c94" v-else @click="editRealName=true;">
                            <edit/>
                        </el-icon>
                    </div>
                    <div class="item">
                        <span>Ｆ　币：</span><span class="item-content coins">{{ userdata.coins }}</span>
                    </div>
                    <div class="item">
                        <span>等　级：</span><span class="item-content lv">{{ userdata.lv }}</span>
                    </div>
                    <div class="item">
                        <span>时　间：</span><span class="item-content deadline">{{ userdata.deadline }}</span>
                    </div>
                </el-card>
            </div>
            <div v-else-if="activeIndex==='2'">2</div>
            <div v-else-if="activeIndex==='3'">3</div>
            <div v-else-if="activeIndex==='4'">
                <div>
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
        </div>
    </div>
</template>

<script>
import {Setting, InfoFilled, Tickets, MessageBox, Delete, Check, Close, Edit} from "@element-plus/icons";
import {markRaw, ref} from "vue";
import {checkLogin} from "@/api/Login";
import {getUserConfig} from "@/api/pay";
import {ElMessage, ElMessageBox} from "element-plus";
import {Account} from "../../api/common";

export default {
    name: "index",
    data() {
        return {
            userdata: this.$store.state.userdata,
            activeIndex: "1",
            Delete: markRaw(Delete), Check: markRaw(Check), Close: markRaw(Close),
            editRealName: false,
            heightSwitch: this.$store.state.userdata.usertype === 1005,
            newUserdata: {
                username: '',
                realName: '',
            }
        }
    },
    components: {Setting, InfoFilled, Tickets, MessageBox, Edit},
    mounted() {
        checkLogin(this)
        getUserConfig(this)
    },
    watch:{
        '$store.state.userdata.usertype'(){
            this.heightSwitch = this.$store.state.userdata.usertype === 1005
        }
    },
    methods: {
        activeIndexes(index) {
            this.activeIndex = index
        },
        changeEdit() {
            this.editRealName = !this.editRealName
        },
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
                Account({action: 'modify', usertype: 1005})
            }).catch(() => {
                this.heightSwitch = false
            })
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

        .content {
            height: 100%;
            width: 100%;
            text-align: center;
        }

        .one {
            .box-card {
                margin: 10px;

                .item {
                    margin: 20px 10px;
                    font-size: 16px;
                    text-align: left;
                    border-bottom: #e0dddd solid 1px;
                    display: flex;
                    flex-direction: row;
                    align-items: center;

                }
            }

            .card-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
        }
    }
}

</style>
