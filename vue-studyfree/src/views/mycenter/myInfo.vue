<template>
    <div class="content">
        <el-card class="box-card">
            <template #header>
                <div class="card-header">
                    <span>个人信息</span>
                    <el-button class="button" type="text" v-if="!editPassword" @click="editPassword=true">重置密码
                    </el-button>
                    <div v-else style="display: flex">
                        <el-input placeholder="请输入新密码" v-model="newUserdata.password"/>
                        <el-button :icon="Check" @click="changePassword"></el-button>
                        <el-button :icon="Close" @click="editPassword=false"></el-button>
                    </div>
                </div>
            </template>
            <div class="item">
                <span>用户名：</span><span class="item-content username">{{ userdata.username }}</span>
            </div>
            <div class="item">
                <span>姓　名：</span>
                <span class="item-content realName" v-if="!editRealName">{{ userdata.realName }}</span>
                <div style="display: flex" v-if="editRealName">
                    <el-input v-model="newUserdata.realName"></el-input>
                    <el-button type="success" :icon="Check" @click="changeRealName"></el-button>
                    <el-button type="danger" :icon="Close" @click="editRealName=false;"></el-button>
                </div>
                <el-icon style="margin-left: 10px;" v-else @click="editRealName=true;">
                    <edit/>
                </el-icon>
            </div>
            <div class="item">
                <span>Ｆ　币：</span><span class="item-content coins">{{ userdata.coins }}</span>
                <el-icon style="margin-left: 10px" :size="14" @click="this.$router.push('/pay')">
                    <plus/>
                </el-icon>
            </div>
            <div class="item">
                <span>等　级：</span><span class="item-content lv">{{ userdata.lv }}</span>
            </div>
            <div class="item">
                <span>时　间：</span><span class="item-content deadline">{{ userdata.deadline }}</span>
                <el-icon style="margin-left: 10px" :size="14" @click="this.$router.push('/pay')">
                    <plus/>
                </el-icon>
            </div>
            <div class="item">
                <span>邮　箱：</span><span class="item-content email">{{ userdata.email }}</span>
            </div>
        </el-card>
    </div>
</template>

<script>
import {markRaw} from "vue";
import {Check, Close, Edit, Plus} from "@element-plus/icons";
import {ElMessage, ElMessageBox} from "element-plus";
import {CommonApi, sendEmailCode} from "@/api/common";
import {email_conf} from "@/store/config";

export default {
    name: "myInfo",
    data() {
        return {
            userdata: this.$store.state.userdata,
            editRealName: false,
            editPassword: false,
            newUserdata: {
                username: '',
                realName: '',
                password: '',
            },
            Check: markRaw(Check), Close: markRaw(Close),
        }
    },
    components: {Edit, Plus,},
    methods: {
        // 更改真实姓名
        changeRealName() {
            if (this.newUserdata.realName) {
                CommonApi({action: 'changeUserInfo', 'realName': this.newUserdata.realName}).then(res => {
                    if (res) {
                        this.editRealName = false
                        this.userdata.realName = this.newUserdata.realName
                    }
                })
            } else {
                ElMessage({
                    message: '请输入姓名！',
                    type: 'warning',
                })
            }
        },

        // 修改密码
        changePassword() {
            if (this.newUserdata.password.length >= 6) {
                sendEmailCode(email_conf.email_modify_password)
                ElMessageBox.prompt('请输入邮箱接收到的验证码', '提示', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    beforeClose: (action, instance, done) => {
                        if (action === 'confirm') {
                            instance.confirmButtonLoading = true
                            instance.confirmButtonText = 'Loading...'
                            CommonApi({
                                action: 'changePassword',
                                code: instance.inputValue,
                                password: this.newUserdata.password
                            }).then(res => {
                                if (res) {
                                    ElMessage({
                                        message: '密码修改成功！',
                                        type: 'success',
                                    })
                                    done()
                                    this.editPassword = false
                                }
                                instance.confirmButtonLoading = false
                                instance.confirmButtonText = '确认'
                            })
                        } else {
                            done()
                            this.editPassword = false
                        }
                    }
                })
            } else {
                ElMessage({
                    message: '请输入至少6位的密码！',
                    type: 'warning',
                })
            }
        }
    }
}
</script>

<style scoped lang="less">
.content {
    height: 100%;
    width: 100%;
    text-align: center;

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

            .el-icon:hover {
                color: #1E9FFF;
            }

            .item-content {
                font-weight: bold;
            }
        }
    }

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}
</style>