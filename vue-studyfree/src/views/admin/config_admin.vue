<template>
    <el-tabs type="border-card">
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
                <el-table-column label="Operations">
                    <template #default="scope">
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
                                   :data="{action: 'addfile',file_path: breadcrumbItem.join('\\')}">
                            <el-button type="primary" size="small">上传文件</el-button>
                        </el-upload>
                        <el-input v-model="dir_path" placeholder="Please input" size="small" style="margin-left: 3px">
                            <template #prepend>新建目录</template>
                            <template #append>
                                <el-button :icon="Check" @click="makedir"></el-button>
                            </template>
                        </el-input>
                    </div>
                </div>
                <el-table :data="fileList" style="width: 100%">
                    <el-table-column label="Name" width="200">
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
                </el-table>
            </div>
        </el-tab-pane>
        <el-tab-pane label="工具合集" style="text-align: center">
            <el-input v-model="tools" :rows="20" type="textarea" placeholder="Please input"/>
            <el-button @click="saveConfig(3)" type="success" style="margin: 5px">保存</el-button>
        </el-tab-pane>
    </el-tabs>
</template>

<script>
import {ElMessage} from "element-plus";
import {CqApi, FilesApi, WebConfigApi} from "@/api/admin"
import {FolderOpened, Document, Check} from "@element-plus/icons";
import {markRaw} from "vue";

export default {
    name: "config_admin",
    data() {
        return {
            ailiPay: {},
            cq: [],
            pay: {},
            tools: {},
            fileList: [],
            breadcrumbItem: ['static'],
            FolderOpened: markRaw(FolderOpened), Document: markRaw(Document), Check: markRaw(Check),
            dir_path: ''
        }
    },
    components: {FolderOpened, Document},
    mounted() {
        this.getAliPayData('aliPay')
        this.getAliPayData('pay')
        this.getCqData()
        this.getFileList('static')
        this.getAliPayData('tools')
    },
    methods: {
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
                }
            })
        },
        getCqData() {
            CqApi({action: 'listAll'}).then(res => {
                if (res) {
                    this.cq = res['retlist']
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
        change_bread_crumb_item(item) {
            const index = this.breadcrumbItem.indexOf(item)
            this.breadcrumbItem = this.breadcrumbItem.slice(0, index + 1)
            this.getFileList(this.breadcrumbItem.join('/'))
        },

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
        }
    },

}
</script>

<style scoped>

</style>