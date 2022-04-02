<template>
    <div class="content">
        <el-card class="box-card">
            <template #header>
                <div class="card-header">
                    <span>个人信息</span>
                    <el-button class="button" type="text" @click="editPassword=true">
                        重置密码
                    </el-button>
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
    <el-dialog v-model="editPassword" title="修改密码" width="30%" destroy-on-close center>
        <el-form :model="passwords" label-width="120px">
            <el-form-item label="原密码：">
                <el-input v-model="passwords.old_password"/>
            </el-form-item>
            <el-form-item label="新密码：">
                <el-input v-model="passwords.new_password1"/>
            </el-form-item>
            <el-form-item label="再次输入：">
                <el-input v-model="passwords.new_password2"/>
                <div style="width: 100%" v-if="checkNewPassWord">
                    <span style="float: right;font-size: 10px;color: red">两次输入的新密码不相同，请确认！！！</span>
                </div>
            </el-form-item>
        </el-form>
        <div style="display: flex;justify-content: space-evenly;">
            <el-button type="success" @click="changePassword" :loading="submitLoading">提交</el-button>
            <el-button type="warning" @click="editPassword=false">取消</el-button>
        </div>
    </el-dialog>
</template>

<script>
import {markRaw} from "vue";
import {Check, Close, Edit, Plus} from "@element-plus/icons";
import {ElMessage, ElMessageBox} from "element-plus";
import {CommonApi, sendEmailCode} from "@/api/common";
import {email_conf} from "@/store/config";
import {getUserConfig} from "@/api/pay";
import {encrypt} from "@/tools/mima";

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
            },
            passwords: {
                old_password: '',
                new_password1: '',
                new_password2: ''
            },
            checkNewPassWord: false,
            submitLoading: false,
            Check: markRaw(Check), Close: markRaw(Close),
        }
    },
    components: {Edit, Plus,},
    mounted() {
        getUserConfig(this)
    },
    watch: {
        "passwords.new_password2"() {
            this.checkNewPassWord = this.passwords.new_password1 !== this.passwords.new_password2
        }
    },
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

            if (this.passwords.new_password1 === this.passwords.new_password2) {
                if (this.passwords.old_password && this.passwords.new_password1) {
                    this.submitLoading = true
                    CommonApi({
                        action: 'changePassword',
                        old_password: encrypt(this.passwords.old_password),
                        new_password: encrypt(this.passwords.new_password2)
                    }).then(res => {
                        if (res) {
                            this.editPassword = false
                            ElMessage.success('密码修改成功！！！')
                        }
                        this.submitLoading = false
                    })
                } else {
                    ElMessage.warning('密码不能为空！！！')
                }
            } else {
                ElMessage.warning('请检查两次输入的密码是否相同！！！')
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