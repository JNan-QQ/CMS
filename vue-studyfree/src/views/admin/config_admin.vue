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
                    <el-input v-model="pay.F"><template #append>/元</template></el-input>
                </el-form-item>
                <el-form-item label="折扣：">
                    <el-input v-model="pay.Z"><template #append>折</template></el-input>
                </el-form-item>
                <div style="text-align: center">
                    <el-button @click="saveConfig(2)" type="success">保存</el-button>
                </div>
            </el-form>
        </el-tab-pane>
        <el-tab-pane label="Task">Task</el-tab-pane>
    </el-tabs>
</template>

<script>
import {CommonApi} from "../../api/common";
import {ElMessage} from "element-plus";
import {CqApi} from "../../api/admin";

export default {
    name: "config_admin",
    data() {
        return {
            ailiPay: {},
            cq: [],
            pay: {},
        }
    },
    mounted() {
        this.getAliPayData('aliPay')
        this.getAliPayData('pay')
        this.getCqData()
    },
    methods: {
        getAliPayData(title) {
            CommonApi({action: 'admin_list_webConfig', title: title}).then(res => {
                if (res) {
                    if (title === 'aliPay') {
                        this.ailiPay = eval('(' + res['retlist'][0]['config'] + ')')
                    } else if (title === 'pay') {
                        this.pay = eval('(' + res['retlist'][0]['config'] + ')')
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
        saveConfig(id) {
            let config = {}
            let title = ''
            if (id===1){
                config = this.ailiPay
                title = 'aliPay'
            }else if(id===2){
                config = this.pay
                title = 'pay'
            }
            CommonApi({action: 'admin_modify_webConfig', webConfig_id: id, config: config}).then(res => {
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
    },
}
</script>

<style scoped>

</style>