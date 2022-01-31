<template>
    <div class="search-top">
        <el-input v-model="select_value" placeholder="请输入字段" clearable style="width: 50%;margin-right: 20px">
            <template #prepend>
                <el-select v-model="select_type" clearable placeholder="Select" style="width: 100px">
                    <el-option label="id" value="id"/>
                    <el-option label="username" value="username"/>
                    <el-option label="realName" value="realName"/>
                    <el-option label="email" value="email"/>
                </el-select>
            </template>
            <template #append>
                <el-button :icon="Search" @click="getAccountData"></el-button>
            </template>
        </el-input>
        <el-button type="primary" plain @click="addBtnFunction" style="position: relative">添加</el-button>
        <!--        <el-button type="success" plain size="small" @click="addMost">批量添加</el-button>-->
    </div>

    <el-table :data="accountData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border class="table">
        <el-table-column prop="id" label="id" min-width="10%" sortable/>
        <el-table-column prop="username" label="用户名" min-width="10%"/>
        <el-table-column prop="realName" label="姓名" min-width="10%"/>
        <el-table-column prop="email" label="邮箱" min-width="10%"/>
        <el-table-column label="操作" min-width="20%" #default="props">
            <el-button type="primary" :icon="Edit" circle @click="editBtnFunction(props.row)"></el-button>
            <el-button type="success" :icon="Loading" circle @click="resetPassword(props.row.id)"></el-button>
            <el-button type="danger" :icon="Delete" circle @click="deleteAccount(props.row)"></el-button>
        </el-table-column>
    </el-table>
    <div class="page">
        <el-pagination
            background
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[5,10,20]"
            :page-size="pageSize"
            layout="sizes, prev, pager, next, jumper, total"
            :total="accountData.length">
        </el-pagination>
    </div>

    <!-- 添加、编辑页面   -->
    <el-dialog v-model="editBtn" title="账号信息" width="30%" destroy-on-close center>
        <el-form ref="form" :model="newAccount" label-position="left" label-width="80px">
            <el-form-item label="用户名：">
                <el-input v-model="newAccount.username"></el-input>
            </el-form-item>
            <el-form-item label="姓名：">
                <el-input v-model="newAccount.realName"></el-input>
            </el-form-item>
            <el-form-item label="邮箱：">
                <el-input v-model="newAccount.email"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="success" @click="modify_add_Account">确认</el-button>
                <el-button type="warning" @click="editBtnCancel">取消</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import {Delete, Edit, Loading, Search} from '@element-plus/icons'
import {markRaw} from "vue";
import {ElMessage, ElMessageBox} from "element-plus";
import {AccountApi} from "../../api/admin";

export default {
    name: "account_admin",
    data() {
        return {
            // 用户数据列表
            accountData: [],
            // 每页显示个数
            pageSize: 5,
            // 选择的页数
            currentPage: 1,

            // 添加修改用户信息字典
            newAccount: {},

            // 引入ico图标
            Edit: markRaw(Edit), Loading: markRaw(Loading), Delete: markRaw(Delete), Search: markRaw(Search),
            // 编辑、添加按钮判定
            editBtn: false,
            // 选择字段
            select_type: '',
            // 字段值
            select_value: '',

        }
    },
    components: {},
    watch: {},
    mounted() {
        this.getAccountData()
    },
    methods: {
        getAccountData() {
            // 搜索过滤
            const search_items = {}
            if (this.select_type && this.select_value) {
                search_items[this.select_type] = this.select_value
            }
            // 发送列出账号请求
            AccountApi({search_items: search_items, action: 'list'}).then(res => {
                if (res) {
                    this.accountData = res['retlist']
                }
            })

        },
        // 编辑修改账号
        editBtnFunction(data) {
            this.newAccount = {
                user_id: data['id'],
                username: data['username'],
                realName: data['realName'],
                email: data['email'],
                action: 'modify'
            }
            this.editBtn = true
        },
        // 添加账号
        addBtnFunction() {
            this.newAccount = {
                username: '',
                realName: '',
                email: '',
                action: 'add'
            }
            this.editBtn = true
        },
        // 取消操作
        editBtnCancel() {
            this.editBtn = false
            this.newAccount = {}
        },
        //提交修改、添加账号
        modify_add_Account() {
            // 修改\添加请求
            AccountApi(this.newAccount).then(res => {
                if (res) {
                    ElMessage({
                        message: '操作成功',
                        type: 'success',
                    })
                    this.editBtn = false
                    this.getAccountData()
                }
            })
            this.newAccount = {}
        },

        // 重置密码
        resetPassword(user_id) {
            ElMessageBox.confirm(
                '确认重置该账号密码吗?',
                '提示',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'info',
                }
            ).then(() => {
                AccountApi({action: 'modify', password: '123456', user_id: user_id}).then(res => {
                    if (res) {
                        ElMessage({
                            message: '密码重置为123456',
                            type: 'success',
                        })
                    }
                })
            }).catch(() => {
            })
        },

        // 删除账号
        deleteAccount(data) {
            ElMessageBox.confirm(
                '确认删除姓名为：' + data['realName'] + ' 的账号吗?',
                '提示',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'info',
                }
            ).then(() => {
                AccountApi({action: 'delete', user_id: data['id']}).then(res => {
                    if (res) {
                        ElMessage({
                            message: '姓名为：' + data['realName'] + ' 的账号删除成功',
                            type: 'success',
                        })
                    }
                })
            }).catch()
        },

        // 专业过滤
        filterMajor(value, row) {
            return row.major === value
        },

        //每页条数改变时触发 选择一页显示多少行
        handleSizeChange(val) {
            this.currentPage = 1;
            this.pageSize = val;
        },
        //当前页改变时触发 跳转其他页
        handleCurrentChange(val) {
            this.currentPage = val;
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

/*分页模块*/
.page {
    text-align: center;
    margin: 10px auto auto;
}
</style>
