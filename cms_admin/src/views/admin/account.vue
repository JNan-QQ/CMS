<template>
    <el-table :data="accountData" border style="width: 100%;text-align: center">
        <el-table-column prop="id" label="id" min-width="10%"/>
        <el-table-column prop="username" label="username" min-width="10%"/>
        <el-table-column prop="realName" label="realName" min-width="10%"/>
        <el-table-column prop="No" label="No" min-width="10%" v-if="accountType!=='mgr'"/>
        <el-table-column prop="classNo" label="classNo" min-width="10%" v-if="accountType==='student'"/>
        <el-table-column prop="gradeNo" label="gradeNo" min-width="10%" v-if="accountType==='student'"/>
        <el-table-column prop="major" label="major" min-width="10%" v-if="accountType!=='mgr'"/>
        <el-table-column label="操作" min-width="20%">
            <el-button type="primary" :icon="Edit" circle></el-button>
            <el-button type="success" :icon="Loading" circle></el-button>
            <el-button type="danger" :icon="Delete" circle></el-button>
        </el-table-column>
    </el-table>
</template>

<script>
import request from "../../utils/request"
import { Edit, Loading, Delete } from '@element-plus/icons'
import {markRaw} from "vue";

export default {
    name: "account",
    data() {
        return {
            accountData: [],
            accountType: '',
            Edit:markRaw(Edit),Loading:markRaw(Loading), Delete:markRaw(Delete)
        }
    },
    components:{},
    watch: {
        '$route': 'before'
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
        }
    },
}
</script>

<style scoped>

</style>
