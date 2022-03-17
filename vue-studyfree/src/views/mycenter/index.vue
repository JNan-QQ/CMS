<template>
    <div class="center_view">
        <div class="left">
            <div class="aviator">
                <el-avatar :src="userdata.aviator" :size="150"></el-avatar>
                <el-upload action="/api/common/other"
                           :data="{action:'uploadImg',file_type:'aviator',file_name:'img_aviator_'+userdata.user_id+'_.png'}"
                           :on-success="uploadImgSuccess"
                           :show-file-list="false"
                           accept="image/png, image/jpeg, image/jpg">
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
                    <span>设置杂项</span>
                </el-menu-item>
                <el-menu-item index="5" v-if="userdata.usertype===1005||userdata.usertype===1">
                    <el-icon>
                        <star/>
                    </el-icon>
                    <span>服务配置</span>
                </el-menu-item>
            </el-menu>
        </div>
        <div class="right">
            <div class="top-btn">
                <el-button :icon="Delete" circle @click="this.$router.go(-1);"></el-button>
            </div>
            <MyInfo v-if="activeIndex==='1'"></MyInfo>
            <div v-else-if="activeIndex==='2'" class="content two">
                <el-empty :image-size="200" v-if="orderList === []"></el-empty>
                <el-table :data="orderList" stripe style="width: 100%" v-else max-height="500">
                    <el-table-column type="index" width="50" index="1"/>
                    <el-table-column prop="orderNo" label="订单编号" width="150"/>
                    <el-table-column prop="create_time" label="创建时间" width="170"/>
                    <el-table-column prop="money" label="订单金额（元）" width="130"/>
                    <el-table-column prop="status" label="订单状态" width="120"/>
                </el-table>
            </div>
            <div v-else-if="activeIndex==='3'" class="content three">
                <div v-for="(item,index) in messageList">
                    <span>{{ index + 1 }}</span>
                    <span>{{ item.title }}</span>
                </div>
            </div>
            <ToolMy v-else-if="activeIndex==='4'"></ToolMy>
            <div v-else-if="activeIndex==='5'" class="content five">
                <div class="five-top">
                    <el-button size="small" v-if="!editUserConfig"
                               @click="editUserConfigs('simple')">
                        修改
                    </el-button>
                    <el-button size="small" v-if="!editUserConfig"
                               @click="editUserConfigs">
                        编辑配置源码
                    </el-button>
                    <el-button size="small" v-if="editUserServerConfigSimple" @click="saveUserServerConfigSimple"
                               :loading="saveLoading">
                        保存
                    </el-button>
                    <el-button size="small" v-if="editUserServerConfig" @click="saveUserServerConfig"
                               :loading="saveLoading">
                        保存配置源码
                    </el-button>
                </div>
                <div class="five-content">
                    <el-empty description="无配置"
                              v-if="userServerConfig === '{}' && !editUserServerConfig && !editUserConfig"></el-empty>
                    <span v-if="userServerConfig === '{}' && editUserServerConfigSimple">如果没有内容请先编辑源码</span>
                    <div v-if="userServerConfig !== '{}' && !editUserServerConfig" class="server-config">
                        <el-form :model="userServerConfigView" label-width="auto">
                            <el-form-item :label="value1['desc_name']" v-for="(value1,key1) in userServerConfigView">
                                <div v-for="(value2,key2) in value1" class="server-config-items"
                                     v-show="key2!=='desc_name'">
                                    <div class="item-name">{{ key2 }}：</div>
                                    <el-input v-model="userServerConfigView[key1][key2]"
                                              :disabled="!editUserServerConfigSimple"
                                              v-if="typeof(value2)==='string' || typeof(value2)==='number'">
                                    </el-input>
                                    <div v-else class="server-config-list">
                                        <el-input v-model="userServerConfigView[key1][key2][index3]"
                                                  :disabled="!editUserServerConfigSimple"
                                                  v-for="(value3,index3) in value2">
                                        </el-input>
                                    </div>
                                </div>
                            </el-form-item>
                        </el-form>
                    </div>
                    <div v-if="editUserServerConfig">
                        <el-input v-model="userServerConfig" :rows="20" type="textarea" placeholder="Please input"/>
                    </div>
                </div>
                <span style="font-size: 10px;float: right;margin-right: 10px;color: red;"
                      v-if="userServerConfig !== '{}'">可以滚动查看</span>
            </div>
        </div>
    </div>
</template>

<script>
import {Setting, InfoFilled, Tickets, MessageBox, Delete, Check, Close, Edit, Plus, Star} from "@element-plus/icons"
import {markRaw} from "vue"
import {checkLogin} from "@/api/Login"
import {getUserConfig} from "@/api/pay"
import {ElMessage, ElMessageBox} from "element-plus"
import {AccountApi, MessageApi} from "@/api/common"
import {UserConfigApi} from "@/api/pay"
import {orderApi} from "@/api/pay"
import MyInfo from "./myInfo"
import MessageMy from "./message"
import OrderMy from "./order"
import Services from "./services"
import ToolMy from "./tool"

export default {
    name: "index",
    data() {
        return {
            userdata: this.$store.state.userdata,
            activeIndex: "1",
            Delete: markRaw(Delete),
            // 编辑源码
            editUserServerConfig: false,
            // 简单编辑
            editUserServerConfigSimple: false,
            // 进入编辑页面
            editUserConfig: false,
            // 保存标志
            saveLoading: false,
            userServerConfig: {},
            userServerConfigView: {},
            orderList: [],
            messageList: []
        }
    },
    components: {Setting, InfoFilled, Tickets, MessageBox, Edit, Star, MyInfo, ToolMy, MessageMy, OrderMy, Services},
    mounted() {
        checkLogin(this)
        getUserConfig(this)
        this.getUserConfigApi()
        this.getOrderApi()
        this.getMessageApi()
    },
    watch: {
        // 监听用户类型
        '$store.state.userdata.usertype'() {
            this.heightSwitch = this.$store.state.userdata.usertype === 1005
        },
    },
    methods: {
        // 用户信息配置
        getUserConfigApi() {
            UserConfigApi({action: 'listServerConfig'}).then((res) => {
                if (res) {
                    this.userServerConfigView = res['userServerConfig']
                    this.userServerConfig = JSON.stringify(res['userServerConfig'], null, "     ")
                }
            })
        },

        // 订单列表
        getOrderApi() {
            orderApi({action: 'list'}).then(res => {
                if (res) {
                    this.orderList = res['retlist']
                }
            })
        },

        // 通知列表
        getMessageApi() {
            MessageApi({action: 'list'}).then(res => {
                if (res) {
                    this.messageList = res['retlist']
                }
            })
        },

        // 激活索引
        activeIndexes(index) {
            this.activeIndex = index
        },

        // 上传头像图片成功后修改头像
        uploadImgSuccess(response, file, fileList) {
            if (response['ret'] === 0) {
                this.userdata.aviator = 'api_file/' + response['url']
                ElMessage({
                    message: '修改成功，请刷新！',
                    type: 'success',
                })
            }
        },

        saveUserServerConfig() {
            this.saveLoading = true
            const userServerConfig = eval("(" + this.userServerConfig + ")")
            UserConfigApi({action: 'modify_config', 'userServerConfig': userServerConfig}).then(res => {
                if (res) {
                    this.editUserServerConfig = false
                    this.editUserConfig = false
                    this.getUserConfigApi()
                }
                this.saveLoading = false
            })
        },

        saveUserServerConfigSimple() {
            this.saveLoading = true
            UserConfigApi({action: 'modify_config', 'userServerConfig': this.userServerConfigView}).then(res => {
                if (res) {
                    this.editUserServerConfigSimple = false
                    this.editUserConfig = false
                    this.getUserConfigApi()
                }
                this.saveLoading = false
            })
        },

        editUserConfigs(type) {
            this.editUserConfig = true
            if (type === 'simple') {
                this.editUserServerConfigSimple = true
            } else {
                this.editUserServerConfig = true
            }
        },
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

        .four {
            text-align: left;

            .four-top {
                border-bottom: #1E9FFF solid 1px;
                padding: 5px;
                display: flex;
                align-items: center;
            }
        }

        .five {
            text-align: left;

            .five-top {
                border-bottom: #1E9FFF solid 1px;
                padding: 5px;
                display: flex;
                justify-content: flex-end;
                align-items: center;
            }

            .five-content {
                margin-top: 10px;
                padding: 10px;

                .el-input {
                    margin-left: 5px;
                }

                .server-config::-webkit-scrollbar {
                    display: none; /* Chrome Safari */
                }

                .server-config {
                    height: calc(65vh);
                    overflow-y: scroll;
                    border: #dee3e3 solid 2px;

                    .el-form-item {
                        border-bottom: #105c94 solid 2px;
                        margin-bottom: 10px;
                    }

                    .server-config-items {
                        border-left: #105c94 solid 1px;
                        display: flex;
                        padding: 5px;
                        width: 100%;

                        .item-name {
                            min-width: 115px;
                            text-align: right;
                        }

                        .server-config-list {
                            display: flex;
                        }
                    }

                }
            }
        }
    }
}

</style>
