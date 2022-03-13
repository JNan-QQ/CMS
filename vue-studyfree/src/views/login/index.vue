<template>
    <div class="login-container" v-if="loginOrRegister">
        <div class="left-container">
            <div class="title"><span>登录</span></div>
            <div class="input-container">
                <el-form :model="loginForm">
                    <el-form-item style="margin-bottom: 0">
                        <el-input v-model="loginForm.username" placeholder="用户名" clearable/>
                    </el-form-item>
                    <el-form-item style="margin-bottom: 0">
                        <el-input v-model="loginForm.password" placeholder="密码" type="password" show-password
                                  @keydown.enter="onSubmit" clearable/>
                    </el-form-item>
                </el-form>
            </div>
            <div class="message-container">
                <span><router-link to="/forget">忘记密码</router-link></span>
            </div>
        </div>
        <div class="right-container">
            <div class="register-container">
                <span class="register" @click="loginOrRegister=false">注册</span>
            </div>
            <div class="action-container">
                <el-button plain @click="onSubmit" :loading="btnSubmitStatus">提交</el-button>
            </div>
        </div>
    </div>

    <div class="register-containers" v-else>
        <div class="right-container">
            <div class="login-containers" @click="loginOrRegister=true">
                <span class="login">登录</span>
            </div>
            <div class="action-container">
                <el-button type="warning" plain @click="onSubmit" :loading="btnSubmitStatus">提交</el-button>
            </div>
        </div>

        <div class="left-container">
            <div class="title"><span>注册</span></div>
            <div class="input-container">
                <el-form :model="registerForm">
                    <el-form-item style="margin-bottom: 0">
                        <el-input v-model="registerForm.username" placeholder="请输入用户名" clearable/>
                    </el-form-item>
                    <el-form-item style="margin-bottom: 0">
                        <el-input v-model="registerForm.password" placeholder="请输入密码" type="password" show-password
                                  clearable/>
                    </el-form-item>
                    <el-form-item style="margin-bottom: 0;">
                        <div style="display: flex;flex-wrap: nowrap;align-items: center;">
                            <el-input v-model="registerForm.email" placeholder="请输入邮箱" clearable type="email"/>
                            <el-button @click="getCode" :loading="btnCodeStatus">获取验证码</el-button>
                        </div>
                    </el-form-item>
                    <el-form-item style="margin-bottom: 0;">
                        <el-input v-model="registerForm.code" placeholder="验证码" clearable/>
                    </el-form-item>
                </el-form>
            </div>
        </div>

    </div>
</template>

<script>
import {Promotion, UserFilled} from "@element-plus/icons"
import {markRaw} from "vue"
import {sign} from "../../api/Login"
import {registerEmailCode} from "../../api/common"
import {ElMessage} from "element-plus"
import {email_conf} from "@/store/config";
import {encrypt} from "../../tools/mima";

export default {
    name: "LoginIndex",
    data() {
        return {
            loginOrRegister: true,
            btnSubmitStatus: false,
            btnCodeStatus: false,
            loginForm: {
                username: '',
                password: '',
                action: 'signin'
            },
            registerForm: {
                username: '',
                password: '',
                email: '',
                code: '',
                action: 'register'
            },
            isLogin: this.$store.state.userdata.isLogin
        }
    },
    components: {UserFilled: markRaw(UserFilled), Promotion: markRaw(Promotion)},
    mounted() {
    },
    methods: {
        onSubmit() {
            this.btnSubmitStatus = true
            if (this.loginOrRegister) {
                // 登录
                sign({
                    action: this.loginForm.action,
                    username: this.loginForm.username,
                    password: encrypt(this.loginForm.password)
                }, this).then(res => {
                    if (res) {
                        this.$store.commit('changeUserInfo', res)
                        this.$router.push('/')
                    }
                    this.btnSubmitStatus = false
                })
            } else {
                // 注册
                sign({
                    username: this.registerForm.username,
                    password: encrypt(this.registerForm.password),
                    email: this.registerForm.email,
                    code: this.registerForm.code,
                    action: this.registerForm.action
                }).then(res => {
                    if (res) {
                        ElMessage({
                            message: '恭喜你注册成功，请登陆',
                            type: 'success',
                        })
                        this.$router.push('/home')
                    }
                    this.btnSubmitStatus = false
                })
            }
        },
        // 获取邮箱验证码
        getCode() {
            registerEmailCode(this.registerForm.email, email_conf.email_register, this)
        }
    },
}
</script>

<style lang="less">
* {
    padding: 0;
    margin: 0;
}

html {
    height: 100%;
}

body {
    background-image: linear-gradient(to bottom right, rgb(180, 189, 241), rgb(193, 160, 238));
}

.login-container {
    width: 530px;
    height: 315px;
    margin: 10% auto 0;
    border-radius: 15px;
    box-shadow: 0 10px 50px 0 rbg(59, 45, 159);
    background-color: rgb(95, 76, 194);
    position: relative;

    .left-container {
        display: inline-block;
        width: 260px;
        border-top-left-radius: 15px;
        border-bottom-left-radius: 15px;
        padding: 54px;
        background-image: linear-gradient(to bottom right, rgb(118, 76, 163), rgb(92, 103, 211));

        .title {
            color: #fff;
            font-size: 18px;
            font-weight: 200;

            span {
                border-bottom: 3px solid rgb(237, 221, 22);
            }
        }

        .input-container {
            padding: 10px 0;

            input {
                border: 0;
                background: none;
                outline: none;
                color: #fff;
                margin: 20px 0;
                display: block;
                width: 100%;
                padding: 5px 0;
                transition: .2s;
                border-bottom: 1px solid rgb(199, 191, 219);

                :hover {
                    border-bottom-color: #fff;
                }

                ::-webkit-input-placeholder {
                    color: rgb(199, 191, 219);
                }
            }
        }

        .message-container {
            font-size: 14px;
            transition: .2s;
            color: rgb(199, 191, 219);
            cursor: pointer;

            :hover {
                color: #fff;
            }
        }
    }

    .right-container {
        width: 145px;
        display: inline-block;
        height: calc(100% - 120px);
        vertical-align: top;
        padding: 60px 0;

        .register-container {
            text-align: center;
            color: #fff;
            font-size: 18px;
            font-weight: 200;
            height: auto;

            span {
                border-bottom: 3px solid rgb(237, 221, 22);
            }
        }

        .action-container {
            text-align: center;
            margin-top: 150px;
        }
    }

}


.register-containers {
    width: 530px;
    height: 440px;
    margin: 10% auto 0;
    border-radius: 15px;
    box-shadow: 0 10px 50px 0 rbg(59, 45, 159);
    background-color: rgb(95, 76, 194);
    position: relative;

    .left-container {
        display: inline-block;
        width: 292px;
        border-top-right-radius: 15px;
        border-bottom-right-radius: 15px;
        padding: 54px;
        background-image: linear-gradient(to bottom right, rgb(118, 76, 163), rgb(92, 103, 211));

        .title {
            color: #fff;
            font-size: 18px;
            font-weight: 200;

            span {
                border-bottom: 3px solid rgb(237, 221, 22);
            }
        }

        .input-container {
            padding: 10px 0;

            input {
                border: 0;
                background: none;
                outline: none;
                color: #fff;
                margin: 20px 0;
                display: block;
                width: 100%;
                padding: 5px 0;
                transition: .2s;
                border-bottom: 1px solid rgb(199, 191, 219);

                :hover {
                    border-bottom-color: #fff;
                }

                ::-webkit-input-placeholder {
                    color: rgb(199, 191, 219);
                }
            }
        }

        .message-container {
            font-size: 14px;
            transition: .2s;
            color: rgb(199, 191, 219);
            cursor: pointer;

            :hover {
                color: #fff;
            }
        }
    }

    .right-container {
        width: 130px;
        display: inline-block;
        height: calc(100% - 120px);
        vertical-align: top;
        padding: 60px 0;

        .login-containers {
            text-align: center;
            color: #fff;
            font-size: 18px;
            font-weight: 200;
            height: auto;

            span {
                border-bottom: 3px solid rgb(237, 221, 22);
            }
        }

        .action-container {
            text-align: center;
            margin-top: 260px;
        }


    }

}


</style>
