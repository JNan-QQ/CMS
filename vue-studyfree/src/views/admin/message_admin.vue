<template>
    <div class="search-top">
        <el-input v-model="select_value" placeholder="请输入字段" clearable style="width: 50%;margin-right: 20px">
            <template #prepend>
                <el-select v-model="select_type" clearable placeholder="Select" style="width: 100px">
                    <el-option label="id" value="id"/>
                    <el-option label="标题" value="title"/>
                    <el-option label="内容" value="content"/>
                    <el-option label="接收者类型" value="group_type"/>
                </el-select>
            </template>
            <template #append>
                <el-button :icon="Search" @click="getMessageData"></el-button>
            </template>
        </el-input>
        <el-button type="primary" plain style="position: relative">添加</el-button>
    </div>

    <el-table :data="messageData.slice((currentPage-1)*pageSize,currentPage*pageSize)" border class="table">
        <el-table-column prop="id" label="id" sortable width="80"/>
        <el-table-column label="标题" width="200">
            <template #default="scope">
                <span class="tzt" :title="scope.row.title">{{ scope.row.title }}</span>
            </template>
        </el-table-column>
        <el-table-column label="内容" width="300">
            <template #default="scope">
                <span class="tzt" :title="scope.row.content">{{ scope.row.content }}</span>
            </template>
        </el-table-column>
        <el-table-column prop="group_type" label="接收组" width="100">
            <template #default="scope">
                <span v-if="scope.row['group_type']===1005">VIP用户组</span>
                <span v-if="scope.row['group_type']===1000">免费用户组</span>
                <span v-if="scope.row['group_type']===1006">个人用户</span>
                <span v-if="scope.row['group_type']===1007">自选</span>
            </template>
        </el-table-column>
        <el-table-column prop="message_type" label="通知类型" width="100"/>
        <el-table-column label="创建时间" width="180">
            <template #default="scope">
                <span>{{ scope.row['creat_time'].replace('T', ' ') }}</span>
            </template>
        </el-table-column>
        <el-table-column label="操作" #default="props">

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
            :total="messageData.length">
        </el-pagination>
    </div>
</template>

<script>
import {Delete, Edit, Loading, Search} from "@element-plus/icons";
import {markRaw} from "vue";
import {MessageApi} from "@/api/common";

export default {
    name: "message_admin",
    data() {
        return {
            // 用户数据列表
            messageData: [],
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
    mounted() {
        this.getMessageData()
    },
    methods: {
        // 获取消息列表
        getMessageData() {
            // 搜索过滤
            const search_items = {}
            if (this.select_type && this.select_value) {
                search_items[this.select_type] = this.select_value
            }
            // 发送列出账号请求
            MessageApi({search_items: search_items, action: 'list'}).then(res => {
                if (res) {
                    this.messageData = res['retlist']
                }
            })
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
    }
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

.tzt {
    overflow: hidden;
    width: 100%;
    white-space: nowrap;
    text-overflow: ellipsis;
}

/*分页模块*/
.page {
    text-align: center;
    margin: 10px auto auto;
    position: relative;
}
</style>