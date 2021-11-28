<template>
  <div class="login-container">
    <el-image class="logo" fit="none" src="./login-logo.png"></el-image>
    <el-form ref="form" :model="form" class="login-from">
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
        <el-button :loading="loading" class="login-btn" type="primary" @click="onSubmit">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import {ElMessage} from "element-plus";
import request from "../../utils/request";

export default {
  name: "LoginIndex",
  data() {
    return {
      form: {
        action: 'signin',
        username: '',
        password: '',
      },
      checked: false,
      loading: false,
    }
  },
  methods: {
    onSubmit() {
      // 禁用登陆按钮
      this.loading = true

      // 判断是否同意条款
      if (this.checked===false){
        ElMessage('请阅读同意条款后登陆。')
        return this.loading = false
      }

      // 发起登陆请求
      request.post('/api/sign/', this.form).then(
          function (response) {
            const data = response.data
            if (data['ret'] === 0) {
              ElMessage({
                message: '登陆成功！欢迎您：' + data['realName'],
                type: 'success',
              })
            } else {
              ElMessage({
                message: '登陆失败！msg：' + data['msg'],
                type: 'warning',
              })
            }
          }
      ).catch(reason => ElMessage.error('服务器错误'))
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
}

</style>
