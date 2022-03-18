<template>
    <div class="content">
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
</template>

<script>
import {UserConfigApi} from "@/api/pay";

export default {
    name: "services",
    data() {
        return {
            userdata: this.$store.state.userdata,
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
        }
    },
    components: {},
    mounted() {
        this.getUserConfigApi()
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
.content {
    height: 100%;
    width: 100%;
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
</style>