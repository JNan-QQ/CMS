<template>
    <div class="content">
        <div v-if="userdata.usertype===1000">
            <span>开启高级模式：</span>
            <el-switch @change="changeUserType"
                       v-model="heightSwitch"
                       :disabled="heightSwitch"
                       inline-prompt
                       active-color="#13ce66"
                       inactive-color="#ff4949"
                       active-text="Y"
                       inactive-text="N">
            </el-switch>
        </div>
        <div v-else class="cdk tools">
            <span>CDK兑换：</span>
            <el-input v-model="cdk" placeholder="请输入CDK兑换码" :suffix-icon="Key"/>
            <el-button type="warning" @click="useCdk" :loading="cdkBtn">兑换</el-button>
        </div>
        <div class="web-view tools">
            <span class="tools-item">界面调整：</span>
            <el-form label-width="85px">
                <el-form-item label="粒子效果：">
                    <el-switch @change="changeParticles"
                        v-model="particles"
                        inline-prompt
                        active-color="#13ce66"
                        inactive-color="#ff4949"
                        active-text="Y"
                        inactive-text="N"
                    />
                </el-form-item>
                <el-form-item label="背景渐变：">
                    <el-color-picker v-model="rgb1" show-alpha :predefine="predefineColors"/>
                    &nbsp;&nbsp;-->&nbsp;&nbsp;
                    <el-color-picker v-model="rgb2" show-alpha :predefine="predefineColors"/>
                    <span class="res-background-color" @click="resBackGroundColor">背景色重置</span>
                </el-form-item>
                <el-form-item label="笔记实验：">
                    <el-switch @change="changeNoteBookRoute"
                        v-model="notebookRoute"
                        inline-prompt
                        active-color="#13ce66"
                        inactive-color="#ff4949"
                        active-text="Y"
                        inactive-text="N"
                    />
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
import {ElMessage, ElMessageBox} from "element-plus";
import {CommonApi} from "@/api/common";
import {Key} from "@element-plus/icons";
import {markRaw, ref} from "vue";
import {cdkApi} from "@/api/pay";
import {setTheme} from "@/styles/style";


export default {
    name: "tool",
    data() {
        return {
            userdata: this.$store.state.userdata,
            heightSwitch: this.$store.state.userdata.usertype === 1005,
            Key: markRaw(Key),
            cdk: '',
            cdkBtn: false,
            particles: true,
            rgb1: '',
            rgb2: '',
            notebookRoute: localStorage.getItem('notebookRoute')==='true',
            predefineColors: ref([
                '#ff4500',
                '#ff8c00',
                '#ffd700',
                '#90ee90',
                '#00ced1',
                '#1e90ff',
                '#c71585',
                'rgba(255, 69, 0, 0.68)',
                'rgb(255, 120, 0)',
                'hsv(51, 100, 98)',
                'hsva(120, 40, 94, 0.5)',
                'hsl(181, 100%, 37%)',
                'hsla(209, 100%, 56%, 0.73)',
                '#c7158577',
            ]),
        }
    },
    watch: {
        // 监听用户类型
        '$store.state.userdata.usertype'() {
            this.heightSwitch = this.$store.state.userdata.usertype === 1005
        },
        'rgb1'() {
            localStorage.setItem('rgb1', this.rgb1)
            setTheme(this.rgb1, this.rgb2)
        },
        'rgb2'() {
            localStorage.setItem('rgb2', this.rgb2)
            setTheme(this.rgb1, this.rgb2)
        },
    },
    components: {Key},
    mounted() {
        this.particles = localStorage.getItem('particles') !== 'false'

        if (localStorage.getItem('rgb1') === null) {
            this.rgb1 = 'rgb(180, 189, 241)'
        } else {
            this.rgb1 = localStorage.getItem('rgb1')
        }
        if (localStorage.getItem('rgb2') === null) {
            this.rgb2 = 'rgb(193, 160, 238)'
        } else {
            this.rgb2 = localStorage.getItem('rgb2')
        }
    },
    methods: {
        // 改变用户类型
        changeUserType(val) {
            ElMessageBox.confirm(
                '确认开启高级功能? 开启后无法关闭',
                '提示',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                }
            ).then(() => {
                CommonApi({action: 'changeUserInfo', usertype: 1005}).then(res => {
                    if (res) {
                        ElMessage.success('用户权限升级成功！！！')
                    }
                })
            }).catch(() => {
                this.heightSwitch = false
            })
        },

        // 改变背景粒子效果
        changeParticles(val){
            localStorage.setItem('particles', val)
            this.$store.commit("pChange", val)
        },

        // 改变笔记路由
        changeNoteBookRoute(val){
             localStorage.setItem('notebookRoute', val)
        },

        // 使用cdk
        useCdk() {
            this.cdkBtn = true
            cdkApi({action: 'useCdk', cdk: this.cdk}).then(res => {
                if (res) {
                    this.cdk = ''
                    ElMessage.success('CDK兑换成功！！！')
                }
                this.cdkBtn = false
            })
        },

        // 重置背景色
        resBackGroundColor() {
            this.rgb1 = 'rgb(180, 189, 241)'
            this.rgb2 = 'rgb(193, 160, 238)'
        },
    }
}
</script>

<style scoped lang="less">
.content {
    height: 100%;
    width: 100%;
    text-align: left;

    div {
        padding: 5px;
    }

    .tools {
        display: flex;
        align-items: center;

        span.res-background-color {
            margin-left: 20px;
            color: #FFFFFF;
        }

        span.res-background-color:hover {
            color: #1E9FFF;
        }

        span.res-background-color:active {
            color: #fc4c00;
        }
    }

    .cdk {
        .el-input {
            width: 40%;
            margin-right: 8px;
            border-left: #d1e0ed solid 1px;
        }
    }

    .web-view {
        .el-form {
            border-left: #d1e0ed solid 1px;
        }
    }
}
</style>