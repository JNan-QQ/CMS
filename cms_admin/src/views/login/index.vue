<template>
    <div class="login-container">
        <div class="logo-img"></div>
        <el-form class="login-from" ref="form" :model="form">
            <el-form-item>
                <el-input v-model="form.username" placeholder="Please input username"></el-input>
            </el-form-item>
            <el-form-item>
                <el-input v-model="form.password" placeholder="Please input password" show-password/>
            </el-form-item>
            <el-form-item>
                <el-checkbox v-model="checked" label="我已阅读并同意用户协议隐私条款"></el-checkbox>
            </el-form-item>
            <el-form-item>
                <el-button class="login-btn" type="primary" @click="onSubmit">登录</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<script>
export default {
    name: "LoginIndex",
    data() {
        return {
            form: {
                username: '',
                password: '',
            },
            checked: false,
            src: '',
        }
    },
    methods: {
        onSubmit() {
            console.log('submit!')
        },
    },
}
</script>

<style scoped lang="less">
.login-container {
    max-width: 500px;
    align-items: center;
    background-color: #acc6da;

    .logo-img{
        background-image: url("login-logo.png");
        height: 119px;
        width: 320px;
        margin: 20px auto auto;
    }

    .login-from {
        padding: 50px;
    }

    .login-btn {
        width: 100%;
    }
}

</style>
