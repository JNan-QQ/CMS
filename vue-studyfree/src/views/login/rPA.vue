<template>
    <div class="forget-view">
        <el-steps :active="active" finish-status="success" process-status="process" simple class="steps">
            <el-step title="输入账号"></el-step>
            <el-step title="验证邮箱"></el-step>
            <el-step title="重置密码"></el-step>
        </el-steps>
        <div v-if="active===0" class="card">
            <el-card class="box-card">
                <div style="margin: 20px"><span style="margin-right: 10px">忘记账号：</span>
                    <el-switch v-model="forgetAccount"/>
                </div>
                <div style="margin: 20px">
                    <el-input v-model="username" placeholder="请输入用户名"
                              :disabled="forgetAccount"/>
                </div>
                <div style="margin: 20px 20px auto 20px;text-align: right">
                    <el-button type="success" @click="active=1">
                        下一步
                        <el-icon class="el-icon--right">
                            <ArrowRight/>
                        </el-icon>
                    </el-button>
                </div>
            </el-card>
        </div>
        <div v-else-if="active===1" class="card">
            <el-card class="box-card">
                <div style="margin: 20px;display: flex">
                    <el-input v-model="email" placeholder="请输入邮箱"></el-input>
                    <el-button :loading="btnCodeStatus" @click="getCode">获取验证码</el-button>
                </div>
                <div style="margin: 20px">
                    <el-input v-model="code" placeholder="请输入验证码"/>
                </div>
                <div style="margin: 20px 20px auto 20px;text-align: right">
                    <el-button type="success" @click="active=2">
                        下一步
                        <el-icon class="el-icon--right">
                            <ArrowRight/>
                        </el-icon>
                    </el-button>
                </div>
            </el-card>
        </div>
        <div v-else-if="active===2" class="card">
            <el-card class="box-card">
                <div style="margin: 20px;display: flex;justify-content: space-between;">
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
                    <el-button type="danger" size="small" round v-if="forgetAccount" :loading="btnCodeStatus" @click="getUserName">
                        获取邮箱账号信息
                    </el-button>
                </div>
                <div style="margin: 20px;">
                    <el-input v-model="password" placeholder="请输入新密码" style="margin-bottom: 10px"></el-input>
                    <el-input v-model="newpassword" placeholder="请确认密码"></el-input>
                    <div v-if="checkerr" style="color: red;text-align: right;font-size: small">两次输入密码不同!!!</div>
                </div>
                <div style="text-align: center;margin: 20px;">
                    <el-button type="success">提交</el-button>
                </div>
            </el-card>
        </div>
        <div v-else>4</div>
    </div>
</template>

<script>
import {ArrowRight, Refresh} from "@element-plus/icons";
import {CommonApi, registerEmailCode} from "@/api/common";

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
    components: {ArrowRight, Refresh},
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
            CommonApi({action: 'emailAccount', email: this.email, code: this.code}).then(res=>{
                if(res){
                    this.usernameList = res['usernameList']
                }
                this.btnCodeStatus = false
            })
        },
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
        }
    }
}

</style>