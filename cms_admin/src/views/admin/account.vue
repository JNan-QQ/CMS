<template>
    <el-table :data="accountData" border style="width: 100%;text-align: center">
        <el-table-column prop="id" label="id" min-width="10%"/>
        <el-table-column prop="username" label="用户名" min-width="10%"/>
        <el-table-column prop="realName" label="姓名" min-width="10%"/>
        <el-table-column prop="No" label="编号" min-width="10%" v-if="accountType!=='mgr'"/>
        <el-table-column prop="classNo" label="班级" min-width="10%" v-if="accountType==='student'"/>
        <el-table-column prop="gradeNo" label="年级" min-width="10%" v-if="accountType==='student'"/>
        <el-table-column prop="major" label="专业" min-width="10%" v-if="accountType!=='mgr'"/>
        <el-table-column label="操作" min-width="20%" #default="props">
            <el-button type="primary" :icon="Edit" circle @click="editBtnFunction(props.row)"></el-button>
            <el-button type="success" :icon="Loading" circle @click="resetPassword(props.row.id)"></el-button>
            <el-button type="danger" :icon="Delete" circle></el-button>
        </el-table-column>
    </el-table>

    <!-- 添加、编辑页面   -->
    <el-dialog v-model="editBtn" title="修改账号信息" width="30%" destroy-on-close center>
        <el-form ref="form" :model="newAccount" label-position="left" label-width="80px">
            <el-form-item label="用户名：">
                <el-input v-model="newAccount.username"></el-input>
            </el-form-item>
            <el-form-item label="姓名：">
                <el-input v-model="newAccount.realName"></el-input>
            </el-form-item>
            <el-form-item label="编号：" v-if="accountType!=='mgr'">
                <el-input v-model="newAccount['No']"></el-input>
            </el-form-item>
            <el-form-item label="班级：" v-if="accountType==='student'">
                <el-input v-model="newAccount['classNo']"></el-input>
            </el-form-item>
            <el-form-item label="年级：" v-if="accountType==='student'">
                <el-input v-model="newAccount['gradeNo']"></el-input>
            </el-form-item>
            <el-form-item label="专业：" v-if="accountType!=='mgr'">
                <el-input v-model="newAccount['major']"></el-input>
            </el-form-item>
            <el-form-item>
                <el-button type="success" @click="modify_add_Account">确认</el-button>
                <el-button type="warning" @click="editBtnCancel">取消</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>
import request from "../../utils/request"
import {Edit, Loading, Delete} from '@element-plus/icons'
import {markRaw} from "vue";
import {ElMessage} from "element-plus";

export default {
    name: "account",
    data() {
        return {
            accountData: [],
            accountType: '',
            newAccount: {},
            Edit: markRaw(Edit), Loading: markRaw(Loading), Delete: markRaw(Delete),
            editBtn: false,
            deleteBtn: false,
            resetBtn: false,

        }
    },
    components: {},
    watch: {
        '$route': 'before',
        editBtn() {
            console.log(this.editBtn)
        }
    },
    mounted() {
        this.before()
    },
    methods: {
        before() {
            // 从路由中获取账号类型
            this.accountType = this.$route.query.type

            // 账号类型转换
            const usertype = {
                student: 1000,
                teacher: 100,
                mgr: 1
            }
            const that = this

            // 发送请求
            request.post('/api/account/', {
                action: 'list',
                search_items: {usertype: usertype[this.accountType]},
            }).then(res => {
                const data = res.data
                if (data['ret'] === 0) {
                    that.accountData = data['retlist']
                }

            })
        },
        // 编辑修改账号
        editBtnFunction(data) {
            this.newAccount = {
                action: 'modify',
                user_id: data['id'],
                username: data['username'],
                realName: data['realName'],
                No: data['No'],
                classNo: data['classNo'],
                gradeNo: data['gradeNo'],
                major: data['major'],
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
            const that = this
            if ('user_id' in this.newAccount) {
                // 修改请求
                request.post('/api/account/', this.newAccount).then(res => {
                    const data = res.data
                    if (data['ret'] === 0) {
                        ElMessage({message: '修改用户信息成功', type: 'success',})
                        that.before()
                    } else {
                        ElMessage({message: data['msg'],type: 'warning',})
                    }
                })
            } else {
                // 添加账号请求
                request.post('/api/account/', this.newAccount).then(res => {
                    const data = res.data
                    if (data['ret'] === 0) {
                        ElMessage({message: '添加用户信息成功,id:'+data['id'], type: 'success',})
                        that.before()
                    } else {
                        ElMessage({message: data['msg'],type: 'warning',})
                    }
                })

            }
        },

        // 重置密码
        resetPassword(user_id){

        }

    },
}
</script>

<style scoped>

</style>
