<template>
    <el-tabs type="border-card" v-loading="loading_table" element-loading-text="加载中...">
        <el-tab-pane label="支付宝相关设置">
            <el-form :model="ailiPay" label-width="120px">
                <el-form-item label="支付宝APPID：">
                    <el-input v-model="ailiPay['appid']" placeholder="请输入用户id"></el-input>
                </el-form-item>

                <el-form-item label="支付成功访问的链接：">
                    <el-input v-model="ailiPay['app_notify_url']"></el-input>
                </el-form-item>
                <el-form-item label="支付结果链接：">
                    <el-input v-model="ailiPay['return_url']"></el-input>
                </el-form-item>
                <el-form-item label="支付宝公钥：">
                    <el-input v-model="ailiPay['ALIPAY_PUBLIC']" :rows="5" type="textarea"></el-input>
                </el-form-item>
                <el-form-item label="APP私钥：">
                    <el-input v-model="ailiPay['APP_PRIVATE']" :rows="5" type="textarea"></el-input>
                </el-form-item>
                <el-form-item label="开发模式：">
                    <el-switch v-model="ailiPay['debug']"></el-switch>
                </el-form-item>
                <div style="text-align: center">
                    <el-button @click="saveConfig(1)" type="success">保存</el-button>
                </div>
            </el-form>
        </el-tab-pane>
        <el-tab-pane label="名人名言">
            <el-table :data="cq" style="width: 100%">
                <el-table-column label="名人名言" prop="content"/>
                <el-table-column label="作者" prop="author"/>
                <el-table-column align="center">
                    <template #header>
                        <el-button @click="change_cq_flg('add')">添加名言</el-button>
                    </template>
                    <template #default="scope">
                        <el-button size="small" type="warning" @click="change_cq_flg('modify',scope.row)">
                            Modify
                        </el-button>
                        <el-button size="small" type="danger" @click="deleteCq(scope.row.id)">
                            Delete
                        </el-button>
                    </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="F币倍率">
            <el-form :model="pay" label-width="120px">
                <el-form-item label="F币：">
                    <el-input v-model="pay.F">
                        <template #append>/元</template>
                    </el-input>
                </el-form-item>
                <el-form-item label="折扣：">
                    <el-input v-model="pay.Z">
                        <template #append>折</template>
                    </el-input>
                </el-form-item>
                <div style="text-align: center">
                    <el-button @click="saveConfig(2)" type="success">保存</el-button>
                </div>
            </el-form>
        </el-tab-pane>
        <el-tab-pane label="文件管理">
            <div>
                <div style="border-bottom: #414444 solid 1px;display: flex;justify-content: space-between;">
                    <el-breadcrumb separator="/" style="margin-bottom: 10px;font-size: 20px;padding: 2px">
                        <el-breadcrumb-item v-for="item in breadcrumbItem" @click="change_bread_crumb_item(item)">
                            {{ item }}
                        </el-breadcrumb-item>
                    </el-breadcrumb>
                    <div style="display: flex;padding: 5px;align-items: center;">
                        <el-upload action="api/my_admin/files" name="file" :show-file-list="false"
                                   :data="{action: 'addfile',file_path: breadcrumbItem.join('\\')}"
                                   :on-success="uploadFileSuccess" :on-progress="Uploading">
                            <el-button type="primary" size="small" v-if="!uploadBtn">上传文件</el-button>
                            <el-progress :percentage="percentage"
                                         :color="customColorMethod"
                                         v-else :text-inside="true"
                                         :stroke-width="15"
                                         style="width: 200px"/>
                        </el-upload>
                        <el-input v-model="dir_path" placeholder="输入目录结构" size="small" style="margin-left: 3px">
                            <template #prepend>新建目录</template>
                            <template #append>
                                <el-button :icon="Check" @click="makedir" :disabled="dir_path"></el-button>
                            </template>
                        </el-input>
                    </div>
                </div>
                <el-table :data="fileList" style="width: 100%">
                    <el-table-column label="Name" width="400">
                        <template #default="scope">
                            <div style="display: flex; align-items: center">
                                <el-icon v-if="scope.row.type==='file'">
                                    <document/>
                                </el-icon>
                                <el-icon v-else>
                                    <folder-opened/>
                                </el-icon>
                                <span style="margin-left: 10px" @click="getFileList(scope.row.path,scope.row.name)">
                                    {{ scope.row.name }}
                                </span>
                                <span v-if="scope.row.type==='dir'">/</span>
                            </div>
                        </template>
                    </el-table-column>
                    <el-table-column label="Size" width="200">
                        <template #default="scope">
                            <span style="margin: auto" v-if="scope.row.type==='file'">{{ scope.row.size }}</span>
                            <span style="margin: auto" v-else>--</span>
                        </template>
                    </el-table-column>
                    <el-table-column label="Time" width="400">
                        <template #default="scope">
                            <span style="margin: auto" v-if="scope.row.type==='file'">{{ scope.row.time }}</span>
                            <span style="margin: auto" v-else>--</span>
                        </template>
                    </el-table-column>
                    <el-table-column fixed="right" label="操作">
                        <template #default="scope">
                            <el-button type="text" size="small" @click="modify(scope.row.name)">Edit</el-button>
                            <el-button type="text" size="small" @click="deleteFD(scope.row.name)">Delete</el-button>
                        </template>
                    </el-table-column>
                </el-table>
            </div>
        </el-tab-pane>
        <el-tab-pane label="工具合集" style="text-align: center">
            <el-input v-model="tools" :rows="20" type="textarea" placeholder="Please input"/>
            <el-button @click="saveConfig(3)" type="success" style="margin: 5px">保存</el-button>
        </el-tab-pane>
    </el-tabs>

    <el-dialog v-model="cq_flg" :title="new_cq['action']" center width="30%">
        <el-form :model="new_cq">
            <el-form-item label="名言：">
                <el-input v-model="new_cq.content"/>
            </el-form-item>
            <el-form-item label="作者：">
                <el-input v-model="new_cq.author"/>
            </el-form-item>
        </el-form>
        <div style="text-align: center;">
            <el-button type="success" @click="change_cq">提交</el-button>
        </div>
    </el-dialog>
</template>

<script>
import {ElMessage, ElMessageBox} from "element-plus";
import {CqApi, FilesApi, WebConfigApi} from "@/api/admin"
import {FolderOpened, Document, Check} from "@element-plus/icons";
import {markRaw} from "vue";
import {checkLogin} from "@/api/Login";

export default {
    name: "config_admin",
    data() {
        return {
            ailiPay: {},
            cq: [],
            cq_flg: false,
            new_cq: {},
            pay: {},
            tools: {},
            fileList: [],
            breadcrumbItem: ['static'],
            FolderOpened: markRaw(FolderOpened), Document: markRaw(Document), Check: markRaw(Check),
            dir_path: '',
            loading_table: false,
            uploadBtn: false,
            percentage: 0, //进度条0-100
        }
    },
    components: {FolderOpened, Document},
    mounted() {
        this.loading_table = true
        this.getAliPayData('aliPay')
        this.getAliPayData('pay')
        this.getCqData()
        this.getFileList('static')
        this.getAliPayData('tools')
    },
    methods: {
        // 获取后台数据
        getAliPayData(title) {
            WebConfigApi({action: 'admin_list_webConfig', title: title}).then(res => {
                if (res) {
                    if (title === 'aliPay') {
                        this.ailiPay = eval('(' + res['retlist'][0]['config'] + ')')
                    } else if (title === 'pay') {
                        this.pay = eval('(' + res['retlist'][0]['config'] + ')')
                    } else if (title === 'tools') {
                        this.tools = eval('(' + res['retlist'][0]['config'] + ')')
                        this.tools = JSON.stringify(this.tools, null, "     ")
                    }
                    this.loading_table = false
                }
            })
        },

        // 获取名人名言数据
        getCqData() {
            CqApi({action: 'listAll'}).then(res => {
                if (res) {
                    this.cq = res['retlist']
                }
            })
        },
        // 改变名人名言标志
        change_cq_flg(mode, item = '') {
            if (mode === 'add') {
                this.new_cq = {content: '', author: '', action: 'add'}

            } else {
                this.new_cq = item
                this.new_cq.action = 'modify'
            }
            this.cq_flg = true
        },
        change_cq() {
            CqApi(this.new_cq).then(res => {
                if (res) {
                    this.cq_flg = false
                    this.getCqData()
                }
            })
        },

        getFileList(file_path, name) {
            if (file_path) {
                if (name) {
                    if (name !== this.breadcrumbItem[this.breadcrumbItem.length - 1]) {
                        this.breadcrumbItem.push(name)
                    }
                }
                FilesApi({action: 'list', file_path: file_path}).then(res => {
                    if (res) {
                        this.fileList = res['retlist']
                    }
                })
            }
        },

        // 保存配置
        saveConfig(id) {
            let config = {}
            let title = ''
            if (id === 1) {
                config = this.ailiPay
                title = 'aliPay'
            } else if (id === 2) {
                config = this.pay
                title = 'pay'
            } else if (id === 3) {
                config = JSON.parse(this.tools, null)
                title = 'tools'
            }
            WebConfigApi({action: 'admin_modify_webConfig', webConfig_id: id, config: config}).then(res => {
                if (res) {
                    this.getAliPayData(title)
                    ElMessage({
                        message: '保存成功',
                        type: 'success',
                    })
                }
            })
        },

        // 删除名人名言
        deleteCq(id) {
            CqApi({action: 'delete', cq_id: id}).then(res => {
                if (res) {
                    this.getCqData()
                    ElMessage({
                        message: '删除成功',
                        type: 'success',
                    })
                }
            })
        },

        // 文件导航头
        change_bread_crumb_item(item) {
            const index = this.breadcrumbItem.indexOf(item)
            this.breadcrumbItem = this.breadcrumbItem.slice(0, index + 1)
            this.getFileList(this.breadcrumbItem.join('/'))
        },

        // 新建文件夹
        makedir() {
            FilesApi({
                action: 'addDir',
                dir_path: this.dir_path,
                base_path: this.breadcrumbItem.join('\\')
            }).then(res => {
                if (res) {
                    this.getFileList(this.breadcrumbItem.join('\\'))
                }
            })
        },

        // 删除文件文件或文件夹
        deleteFD(path) {
            ElMessageBox.confirm(
                '确认删除文件/文件夹：' + path + ' 吗?',
                'Warning',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                }
            ).then(() => {
                FilesApi({
                    action: 'delete',
                    path: this.breadcrumbItem.join('\\') + '\\' + path
                }).then(res => {
                    if (res) {
                        ElMessage({
                            type: 'success',
                            message: '文件/文件夹： ' + path + ' 已删除！',
                        })
                        this.getFileList(this.breadcrumbItem.join('\\'))
                    }
                })
            }).catch(() => {
            })
        },

        // 修改文件名
        modify(path) {
            ElMessageBox.prompt('请输入新的文件/文件夹名', '输入', {
                confirmButtonText: 'OK',
                cancelButtonText: 'Cancel',
            }).then(({value}) => {
                FilesApi({
                    action: 'modify',
                    path: this.breadcrumbItem.join('\\') + '\\' + path,
                    new_path: this.breadcrumbItem.join('\\') + '\\' + value
                }).then(res => {
                    if (res) {
                        ElMessage({
                            type: 'success',
                            message: '文件名修改成功！',
                        })
                        this.getFileList(this.breadcrumbItem.join('\\'))
                    }
                })
            }).catch(() => {
            })
        },

        // 文件上传成功
        uploadFileSuccess(response, uploadFile, uploadFiles) {
            ElMessage({
                type: 'success',
                message: '文件上传成功！',
            })
            this.getFileList(this.breadcrumbItem.join('\\'))
            this.uploadBtn = false
        },

        // 文件上传过程中
        Uploading(evt, uploadFile, uploadFiles) {
            this.uploadBtn = true
            this.percentage = parseInt(evt.percent)
        },
        // 进度条颜色
        customColorMethod(percentage) {
            if (percentage < 30) {
                return '#97b4f1'
            } else if (percentage < 80) {
                return '#e6a23c'
            } else {
                return '#67c23a'
            }
        }
    },

}

</script>

<style scoped>

</style>