<template>
    <div class="login-container">
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
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background-size: cover;
    .login-from {
        padding: 50px;
        background-color: #acc6da;
    }

    .login-btn {
        width: 100%;
    }
}

</style>
