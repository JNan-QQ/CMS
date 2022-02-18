<template>
    <div class="forget-view">
        <el-steps :active="active" finish-status="success" process-status="process" simple class="steps">
            <el-step title="输入账号"></el-step>
            <el-step title="验证邮箱"></el-step>
            <el-step title="重置密码"></el-step>
        </el-steps>
        <div class="card">
            <el-card class="box-card">
                <el-icon class="return" v-if="active!==0" @click="active=active-1">
                    <arrow-left-bold/>
                </el-icon>
                <div v-if="active===0" class="input_box">
                    <span style="margin-right: 10px">忘记账号：</span>
                    <el-switch v-model="forgetAccount"/>
                    <el-input v-model="username" placeholder="请输入用户名" :disabled="forgetAccount" class="input-line"/>
                </div>
                <div v-else-if="active===1" class="input_box">
                    <div style="display: flex">
                        <el-input v-model="email" placeholder="请输入邮箱"></el-input>
                        <el-button :loading="btnCodeStatus" @click="getCode">获取验证码</el-button>
                    </div>
                    <el-input v-model="code" placeholder="请输入验证码" class="input-line"/>
                </div>
                <div v-else-if="active===2" class="input_box">
                    <div style="display: flex;justify-content: space-between;">
                        <span v-if="!forgetAccount">用户名：{{ username }}</span>
                        <el-select v-model="username" placeholder="选择账号" size="small" v-else>
                            <el-option
                                v-for="item in usernameList"
                                :key="item"
                                :label="item"
                                :value="item"
                            >
                            </el-option>
                        </el-select>
                        <el-button type="danger" size="small" round v-if="forgetAccount" :loading="btnCodeStatus"
                                   @click="getUserName">
                            获取邮箱账号信息
                        </el-button>
                    </div>
                    <el-input v-model="password" placeholder="请输入新密码" class="input-line"></el-input>
                    <el-input v-model="newpassword" placeholder="请确认密码" class="input-line"></el-input>
                    <div v-if="checkerr" style="color: red;text-align: right;font-size: small">两次输入密码不同!!!</div>
                </div>
                <div :class="{'button-center':active===2,'button-right':active!==2}">
                    <el-button type="success" @click="active=active+1" v-if="active!==2" size="small">
                        下一步
                        <el-icon class="el-icon--right">
                            <ArrowRight/>
                        </el-icon>
                    </el-button>
                    <el-button type="success" v-else size="small" @click="changePassword" :loading="btnCodeStatus">
                        提交
                    </el-button>
                </div>
            </el-card>
        </div>
    </div>
</template>

<script>
import {ArrowRight, Refresh, ArrowLeftBold} from "@element-plus/icons";
import {AccountApi, CommonApi, registerEmailCode} from "@/api/common";
import {ElMessage} from "element-plus";

export default {
    name: "rPA",
    data() {
        return {
            active: 0,
            forgetAccount: false,
            username: '',
            usernameList: [],
            email: '',
            code: '',
            Refresh,
            btnCodeStatus: false,
            password: '',
            newpassword: '',
            checkerr: false
        }
    },
    components: {ArrowRight, Refresh, ArrowLeftBold},
    watch: {
        'newpassword'() {
            this.checkerr = this.password !== this.newpassword;
        }
    },
    methods: {
        getCode() {
            registerEmailCode(this.email, this)
        },
        getUserName() {
            this.btnCodeStatus = true
            CommonApi({action: 'emailAccount', email: this.email, code: this.code}).then(res => {
                if (res) {
                    this.usernameList = res['usernameList']
                }
                this.btnCodeStatus = false
            })
        },
        changePassword() {
            if (!this.checkerr && this.username && this.password) {
                this.btnCodeStatus = true
                CommonApi({
                    action: 'resetPassword',
                    code: this.code,
                    email: this.email,
                    username: this.username,
                    password: this.password
                }).then(res => {
                    if (res) {
                        ElMessage({
                            message: '找回找回、密码成功.',
                            type: 'success',
                        })
                        this.$router.push('/login')
                    }
                    this.btnCodeStatus = false
                })
            } else {
                ElMessage.error('检查输入信息.')
            }

        }
    }
}
</script>

<style scoped lang="less">
.forget-view {
    max-width: calc(70vw);
    text-align: center;
    padding: 40px;
    margin: auto;

    .steps {
        margin-top: 10px;
        position: relative;
    }

    .card {
        height: calc(80vh);

        .box-card {
            width: 50%;
            margin: auto;
            position: relative;
            top: calc(15vh);
            text-align: left;

            .return:hover {
                color: #1E9FFF;
            }

            .input_box {
                padding: 15px 30px;

                .input-line {
                    margin-top: 20px;
                }

            }

            .button-center, .button-right {
                padding: 0 30px;
            }

            .button-center {
                text-align: center;
            }

            .button-right {
                text-align: right;
            }

        }

    }
}

</style>