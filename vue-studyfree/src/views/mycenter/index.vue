<template>
    <div class="center_view">
        <div class="left">
            <div class="aviator">
                <el-avatar :src="userdata.aviator" :size="150"></el-avatar>
                <el-upload action="/api/common/other"
                           :data="{action:'uploadImg',file_type:'aviator',file_name:'img_aviator_'+userdata.id+'_timeR.png'}"
                           :on-success="uploadImgSuccess"
                           :show-file-list="false"
                           accept="image/png, image/jpeg, image/jpg"
                >
                    <el-button>更换头像</el-button>
                </el-upload>
            </div>
            <el-menu default-active="1" @select="activeIndexes">
                <el-menu-item index="1">
                    <el-icon>
                        <InfoFilled/>
                    </el-icon>
                    <span>账号信息</span>
                </el-menu-item>
                <el-menu-item index="2">
                    <el-icon>
                        <Tickets/>
                    </el-icon>
                    <span>我的订单</span>
                </el-menu-item>
                <el-menu-item index="3">
                    <el-icon>
                        <MessageBox/>
                    </el-icon>
                    <span>通知中心</span>
                </el-menu-item>
                <el-menu-item index="4">
                    <el-icon>
                        <setting/>
                    </el-icon>
                    <span>设置-杂项</span>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="right">
            <div class="top-btn">
                <el-button :icon="Delete" circle @click="this.$router.go(-1);"></el-button>
            </div>
            <div v-if="activeIndex==='1'" class="content one">
                <el-card class="box-card">
                    <template #header>
                        <div class="card-header">
                            <span>个人信息</span>
                            <el-button class="button" type="text" v-if="!editPassword" @click="editPassword=true">重置密码
                            </el-button>
                            <div v-else style="display: flex">
                                <el-input placeholder="请输入新密码" v-model="newUserdata.password"/>
                                <el-button :icon="Check" @click="changePassword"></el-button>
                                <el-button :icon="Close" @click="editPassword=false"></el-button>
                            </div>
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
                        <el-icon style="margin-left: 10px;color: #105c94" v-else @click="editRealName=true;">
                            <edit/>
                        </el-icon>
                    </div>
                    <div class="item">
                        <span>Ｆ　币：</span><span class="item-content coins">{{ userdata.coins }}</span>
                    </div>
                    <div class="item">
                        <span>等　级：</span><span class="item-content lv">{{ userdata.lv }}</span>
                    </div>
                    <div class="item">
                        <span>时　间：</span><span class="item-content deadline">{{ userdata.deadline }}</span>
                    </div>
                    <div class="item">
                        <span>邮　箱：</span><span class="item-content email">{{ userdata.email }}</span>
                    </div>
                </el-card>
            </div>
            <div v-else-if="activeIndex==='2'">2</div>
            <div v-else-if="activeIndex==='3'">3</div>
            <div v-else-if="activeIndex==='4'">
                <div style="border-bottom: #1E9FFF solid 1px;padding: 5px;
                            display:flex;justify-content: space-between;align-items: center;">
                    <div><span>开启高级模式：</span>
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
                    <div>
                        <el-button size="small" v-if="!editUserServerConfig" @click="editUserServerConfig=true">
                            编辑配置文件
                        </el-button>
                        <el-button size="small" v-else @click="saveUserServerConfig" :loading="saveLoading">
                            保存配置文件
                        </el-button>
                    </div>
                </div>
                <div style="margin-top: 10px;padding: 10px">
                    <el-empty description="无配置" v-if="userServerConfig === {} && !editUserServerConfig"></el-empty>
                    <div v-if="userServerConfig !== {} && !editUserServerConfig">123</div>
                    <div v-if="editUserServerConfig">
                        <vue3-json-editor
                            v-model="userServerConfig"
                            :expandedOnStart="true"
                            @json-change="onJsonChange"
                        />
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {Setting, InfoFilled, Tickets, MessageBox, Delete, Check, Close, Edit} from "@element-plus/icons";
import {markRaw, reactive} from "vue"
import {checkLogin} from "@/api/Login";
import {getUserConfig} from "@/api/pay";
import {ElMessage, ElMessageBox} from "element-plus";
import {AccountApi, CommonApi, sendEmailCode} from "@/api/common";
import {UserConfigApi} from "../../api/pay";
import {Vue3JsonEditor} from 'vue3-json-editor'

export default {
    name: "index",
    data() {
        return {
            userdata: this.$store.state.userdata,
            activeIndex: "1",
            Delete: markRaw(Delete), Check: markRaw(Check), Close: markRaw(Close),
            editRealName: false,
            editPassword: false,
            editUserServerConfig: false,
            saveLoading: false,
            heightSwitch: this.$store.state.userdata.usertype === 1005,
            newUserdata: {
                username: '',
                realName: '',
                password: '',
            },
            userServerConfig: {}
        }
    },
    components: {Setting, InfoFilled, Tickets, MessageBox, Edit, Vue3JsonEditor},
    mounted() {
        checkLogin(this)
        getUserConfig(this)
        UserConfigApi({action: 'listServerConfig'}).then(res => {
            if (res) {
                this.userServerConfig = res['userServerConfig']
            }
        })
    },
    watch: {
        // 监听用户类型
        '$store.state.userdata.usertype'() {
            this.heightSwitch = this.$store.state.userdata.usertype === 1005
        },
    },
    methods: {
        // 激活索引
        activeIndexes(index) {
            this.activeIndex = index
        },
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
                AccountApi({action: 'modify', usertype: 1005})
            }).catch(() => {
                this.heightSwitch = false
            })
        },
        changeRealName() {
            if (this.newUserdata.realName) {
                AccountApi({action: 'modify', 'realName': this.newUserdata.realName}).then(res => {
                    console.log(res)
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
        // 上传头像图片成功后修改头像
        uploadImgSuccess(response, file, fileList) {
            if (response['ret'] === 0) {
                this.userdata.aviator = response['url']
                AccountApi({action: 'modify', 'aviator': response['url']})
            }
        },
        changePassword() {
            if (this.newUserdata.password.length >= 6) {
                sendEmailCode()
                ElMessageBox.prompt('请输入邮箱接收到的验证码', 'Tip', {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                }).then(({value}) => {
                    CommonApi({action: 'checkEmailCode', code: value}).then(res => {
                        if (res) {
                            AccountApi({action: 'modify', 'password': this.newUserdata.password})
                        }
                    })
                }).catch(() => {

                })
            } else {
                ElMessage({
                    message: '请输入至少6位的密码！',
                    type: 'warning',
                })
            }


        },
        saveUserServerConfig() {
            this.saveLoading = true
            UserConfigApi({action: 'modify', 'userServerConfig': this.userServerConfig}).then(res => {
                if(res){
                    this.editUserServerConfig = false
                }
                this.saveLoading = false
            })

        },
        onJsonChange(value) {
            this.userServerConfig = value
        }
    },
}
</script>

<style scoped lang="less">
.center_view {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: calc(80vh);
    margin: 10vh auto;

    .left, .right {
        background-color: #FFFFFF;
        position: relative;
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: stretch;
    }

    .left {
        width: 220px;
        border-radius: 8px 0 0 8px;

        .aviator {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px 10px;
            border-bottom: #105c94 solid 2px;

            .el-button {
                margin-top: 10px;
            }
        }
    }

    .right {
        width: 620px;
        margin-left: 3px;
        border-radius: 0 8px 8px 0;

        .top-btn {
            display: flex;
            justify-content: right;
            border-bottom: #105c94 solid 1px;

            .el-button {
                margin: 5px;
            }
        }

        .content {
            height: 100%;
            width: 100%;
            text-align: center;
        }

        .one {
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
    }
}

</style>
