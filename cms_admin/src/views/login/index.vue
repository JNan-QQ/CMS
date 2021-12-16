<template>
    <div class="login-container">
        <el-image class="logo" fit="none" src="./login-logo.png"></el-image>
        <el-form ref="form" :model="form" class="login-from">
            <el-form-item>
                <user-filled style="width: 30px;height: 30px;margin-right: 10px;margin-top: 4px" />
                <el-input v-model="form.username" placeholder="Please input username"></el-input>
            </el-form-item>
            <el-form-item>
                <promotion style="width: 30px;height: 30px;margin-right: 10px;margin-top: 4px" />
                <el-input v-model="form.password" placeholder="Please input password" show-password/>
            </el-form-item>
            <el-form-item>
                <el-checkbox v-model="checked" label="我已阅读并同意用户协议隐私条款"></el-checkbox>
            </el-form-item>
            <el-form-item>
                <el-button :loading="loading" class="login-btn" type="primary" @click="onSubmit">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
import {ElMessage} from "element-plus";
import request from "../../utils/request";
import { UserFilled,Promotion } from "@element-plus/icons"
import {markRaw} from "vue";
import {loginMain} from '../../api/Login'

export default {
    name: "LoginIndex",
    data() {
        return {
            form: {
                username: '',
                password: '',
            },
            checked: false,
            loading: false,
        }
    },
    components:{UserFilled:markRaw(UserFilled),Promotion:markRaw(Promotion)},
    methods: {
        onSubmit() {
            // 禁用登陆按钮
            this.loading = true

            // 判断是否同意条款
            if (this.checked === false) {
                ElMessage('请阅读同意条款后登陆。')
                return this.loading = false
            }

            // 发起登陆请求
            // signin(this.form,this)
            loginMain('signin',this,this.form)
            this.loading = false
        },
    },
}
</script>

<style lang="less">
.login-container {
    max-width: 400px;
    margin: 5% auto;
    box-shadow: 0 0 24px rgba(0, 0, 0, 0.15);
    background-color: rgb(245, 246, 252);
    border-radius: 24px;
    padding: 24px 24px;

    .logo {
        padding-left: 50px;
    }

    .login-from {
        padding: 25px;
    }

    .login-btn {
        width: 100%;
    }
    .el-form-item__content{
        display: flex;
    }
}

</style>
