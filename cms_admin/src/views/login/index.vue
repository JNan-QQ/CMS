<template>
  <div class="login-container">
    <el-image class="logo" src="./login-logo.png" fit="none"></el-image>
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

<style lang="less">
.login-container {
  max-width: 400px;
  margin: 5% auto;
  box-shadow: 0 0 24px rgba(0, 0, 0, 0.15);
  background-color: rgb(245, 246, 252);
  border-radius: 24px;
  padding: 24px 14px;

  .logo{
    padding-left: 50px;
  }

  .login-from {
    padding: 25px;
  }

  .login-btn {
    width: 100%;
  }
}

</style>
