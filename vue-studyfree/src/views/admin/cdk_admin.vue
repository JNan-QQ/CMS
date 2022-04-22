<template>
    <div class="search-top">
        <el-input v-model="select_value" placeholder="请输入字段" clearable style="width: 50%;margin-right: 20px">
            <template #prepend>
                <el-select v-model="select_type" clearable placeholder="Select" style="width: 100px">
                    <el-option label="id" value="cdk_id"/>
                    <el-option label="cdk" value="cdk"/>
                    <el-option label="status" value="status"/>
                </el-select>
            </template>
            <template #append>
                <el-button :icon="Search" @click="getCdkData"></el-button>
            </template>
        </el-input>
        <el-button type="primary" plain @click="editBtn=true" style="position: relative">添加</el-button>
    </div>

    <el-table :data="cdkData" border class="table" v-loading="loading_table" element-loading-text="加载中...">
        <el-table-column prop="id" label="id" sortable width="80"/>
        <el-table-column prop="cdk" label="CDK" width="150"/>
        <el-table-column label="status" width="100">
            <template #default="scope">
                <el-switch v-model="scope.row.status" style="margin-left: 24px" inline-prompt
                           :active-icon="Check" :inactive-icon="Close"
                           @change="modify_cdk(scope.row.id,'status',scope.row.status)"/>
            </template>
        </el-table-column>
        <el-table-column label="剩余数量" width="150">
            <template #default="scope">
                <el-input-number v-model="scope.row.num" size="small" :controls="false"
                                 @change="modify_cdk(scope.row.id,'num',scope.row.num)"/>
            </template>
        </el-table-column>
        <el-table-column label="+coins" width="150">
            <template #default="scope">
                <el-input-number v-model="scope.row.coins" size="small" :controls="false"
                                 @change="modify_cdk(scope.row.id,'coins',scope.row.coins)"/>
            </template>
        </el-table-column>
        <el-table-column label="+days" width="150">
            <template #default="scope">
                <el-input-number v-model="scope.row.days" size="small" :controls="false"
                                 @change="modify_cdk(scope.row.id,'days',scope.row.days)"/>
            </template>
        </el-table-column>
        <el-table-column label="endTime" width="250">
            <template #default="scope">
                <el-date-picker v-model="scope.row.endTime" type="datetime" placeholder="选择到期时间"
                                @change="modify_cdk(scope.row.id,'endTime',scope.row.endTime)"
                                format="YYYY-MM-DD HH:mm:ss" value-format="YYYY-MM-DD HH:mm:ss"/>
            </template>
        </el-table-column>
        <el-table-column label="操作" #default="props">
            <el-button type="danger" :icon="Delete" circle @click="delete_one_cdk(props.row.id)"></el-button>
        </el-table-column>
    </el-table>

    <!--    翻页      -->
    <div style="text-align: center;position: relative">
        <el-pagination layout="prev, pager, next" :current-page.sync="current_page" :page-size="page_size"
                       :total="total" @current-change="handleCurrentChange"/>
    </div>

    <!-- 添加页面   -->
    <el-dialog v-model="editBtn" title="cdk信息" width="30%" destroy-on-close center>
        <el-form ref="form" :model="newCdk" label-position="right" label-width="120px">
            <el-form-item label="CDK到期时间：">
                <el-date-picker v-model="newCdk.endTime" placeholder="选择到期时间" type="datetime"
                                format="YYYY-MM-DD HH:mm:ss" value-format="YYYY-MM-DD HH:mm:ss"/>
            </el-form-item>
            <el-form-item label="CDK数量：">
                <el-input-number v-model="newCdk.num" size="small" :controls="false"/>
            </el-form-item>
            <el-form-item label="+coins：">
                <el-input-number v-model="newCdk.coins" size="small" :controls="false"/>
            </el-form-item>
            <el-form-item label="+days：">
                <el-input-number v-model="newCdk.days" size="small" :controls="false"/>
            </el-form-item>
        </el-form>
        <div style="text-align: center">
            <el-button type="success" @click="addCdk" :loading="addBtn">确认</el-button>
            <el-button type="warning" style="margin-left: 20%" @click="editBtn=false">取消</el-button>
        </div>
    </el-dialog>
</template>

<script>
import {Delete, Edit, Loading, Search, Check, Close} from "@element-plus/icons";
import {markRaw} from "vue";
import {CdkApi} from "@/api/admin";
import {ElMessage, ElMessageBox} from "element-plus";

export default {
    name: "cdk_admin", data() {
        return {
            // 用户数据列表
            cdkData: [],
            // 翻页
            total: 0,
            page_size: 10,
            current_page: 1,
            // 添加修改用户信息字典
            newCdk: {},
            // 引入ico图标
            Edit: markRaw(Edit),
            Loading: markRaw(Loading),
            Delete: markRaw(Delete),
            Search: markRaw(Search),
            Check: markRaw(Check),
            Close: markRaw(Close),
            // 编辑、添加按钮判定
            editBtn: false,
            // 选择字段
            select_type: '',
            // 字段值
            select_value: '',
            loading_table: false,
            addBtn: false
        }
    },
    watch: {
        'current_page'() {
            this.getCdkData()
        }
    },
    mounted() {
        this.getCdkData()
    },
    components: {},
    methods: {
        getCdkData() {
            this.loading_table = true
            // 搜索过滤
            const search_items = {}
            if (this.select_type && this.select_value) {
                search_items[this.select_type] = this.select_value
            }
            // 发送列出账号请求
            CdkApi({
                search_items: search_items,
                action: 'list',
                page_num: this.current_page,
                page_size: this.page_size
            }).then(res => {
                if (res) {
                    this.cdkData = res['retlist']
                    this.total = res['total']
                    this.loading_table = false
                }
            })
        },
        // 翻页
        handleCurrentChange: function (currentPage) {
            this.current_page = currentPage
        },
        // 添加一个CDK
        addCdk() {
            this.addBtn = true
            this.newCdk.action = 'add'
            CdkApi(this.newCdk).then(res => {
                if (res) {
                    this.addBtn = false
                    this.editBtn = false
                    this.getCdkData()
                    ElMessage.success('CDK添加成功！！！')
                }
            })
        },
        modify_cdk(id, key, value) {
            const data = {action: 'modify', cdk_id: id}
            data[key] = value
            CdkApi(data).then(res => {
                if (res) {
                    this.getCdkData()
                }
            })
        },
        delete_one_cdk(id) {
            ElMessageBox.confirm(
                '确认删除这个CDK吗?',
                '提示',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'info',
                }
            ).then(() => {
                CdkApi({action: 'delete', cdk_id: id}).then(res => {
                    if (res) {
                        this.getCdkData()
                    }
                })
            }).catch()
        },
    },
}
</script>

<style scoped lang="less">
.search-top {
    display: flex;
    align-items: center;
    margin-bottom: 3px
}

.table {
    min-height: 600px;
    padding: 10px;
}
</style>