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
        <el-button type="primary" plain style="position: relative" @click="changeDialogVisible('add')">添加</el-button>
    </div>

    <el-table :data="messageData" border class="table" v-loading="loading_table" element-loading-text="加载中...">
        <el-table-column prop="id" label="id" sortable width="80"/>
        <el-table-column label="标题" width="200">
            <template #default="scope">
                <span class="tzt" :title="scope.row.title">{{ scope.row.title }}</span>
            </template>
        </el-table-column>
        <el-table-column label="内容" width="100">
            <template #default="scope">
                <el-popover effect="light" trigger="hover" placement="top" width="auto">
                    <template #default>
                        <div style="text-align: center">{{ scope.row.title }}</div>
                        <div v-html="scope.row.content"></div>
                    </template>
                    <template #reference>
                        <el-tag>悬浮查看</el-tag>
                    </template>
                </el-popover>
            </template>
        </el-table-column>
        <el-table-column label="接收组" width="100">
            <template #default="scope">
                <span v-if="scope.row['group_type']===1005">VIP用户组</span>
                <span v-if="scope.row['group_type']===1000">免费用户组</span>
                <span v-if="scope.row['group_type']===1006">个人用户</span>
                <span v-if="scope.row['group_type']===1007">自选</span>
            </template>
        </el-table-column>
        <el-table-column label="接收者id" width="100">
            <template #default="scope">
                <div v-if="scope.row['user']!==''">
                    <span v-for="item in scope.row['user']?.split('|')">{{ item }}&nbsp;</span>
                </div>
            </template>
        </el-table-column>
        <el-table-column label="通知类型" width="100">
            <template #default="scope">
                <span v-if="scope.row['message_type']===1">邮件</span>
                <span v-if="scope.row['message_type']===2">时间</span>
                <span v-if="scope.row['message_type']===3">充值</span>
                <span v-if="scope.row['message_type']===4">优惠码</span>
            </template>
        </el-table-column>
        <el-table-column prop="status" label="通知状态" width="100"/>
        <el-table-column label="创建时间" width="180">
            <template #default="scope">
                <span>{{ scope.row['creat_time']?.split('T')[0] }}</span>
            </template>
        </el-table-column>
        <el-table-column label="操作" #default="scope">
            <el-button type="text" @click="changeDialogVisible('modify',scope.row)">修改</el-button>
            <el-button type="text" :loading="disabledLoading" @click="disable(scope.row)">
                <span v-if="scope.row.status===true">禁用</span><span v-else>启用</span>
            </el-button>
            <el-button type="text" @click="deleteMessage(scope.row.id)" :loading="deleteLoading">删除</el-button>
        </el-table-column>
    </el-table>
    <!--    翻页      -->
    <pages :total="total" @get-data="getMessageData" :btn_background="false"></pages>

    <el-dialog v-model="dialogVisible" :title="newMessage.action" width="30%" center destroy-on-close>
        <el-form :model="newMessage" label-width="120px">
            <el-form-item label="标题：">
                <el-input v-model="newMessage.title" placeholder="请输入通知标题"/>
            </el-form-item>
            <el-form-item label="通知内容：">
                <el-input v-model="newMessage.content" show-word-limit type="textarea" placeholder="请选输入通知内容，支持HTML文本"/>
            </el-form-item>
            <el-form-item label="通知类型：">
                <el-select v-model="newMessage['message_type']" placeholder="请选择通知类型">
                    <el-option label="邮件通知" :value="1"/>
                    <el-option label="时间通知" :value="2"/>
                    <el-option label="充值通知" :value="3"/>
                    <el-option label="优惠码" :value="4"/>
                </el-select>
            </el-form-item>
            <el-form-item label="接收用户组：">
                <el-select v-model="newMessage['group_type']" placeholder="请选择通知类型">
                    <el-option label="vip" :value="1005"/>
                    <el-option label="free" :value="1000"/>
                    <el-option label="个人" :value="1006"/>
                    <el-option label="无" :value="1007"/>
                </el-select>
            </el-form-item>
            <el-form-item label="输入用户id：" v-if="newMessage['group_type'] === 1006">
                <el-input v-model="newMessage['user']" placeholder="|2556|" clearable/>
            </el-form-item>
        </el-form>
        <div style="text-align: center">
            <el-button type="success" @click="operateMessage" :loading="saveLoading">提交</el-button>
        </div>

    </el-dialog>

</template>

<script>
import {Delete, Edit, Loading, Search} from "@element-plus/icons"
import {markRaw} from "vue"
import {MessageApi} from "@/api/common"
import {ElMessage, ElMessageBox} from "element-plus"
import Pages from "@/components/pages.vue"

export default {
    name: "message_admin",
    data() {
        return {
            // 用户数据列表
            messageData: [],
            // 翻页
            total: 0,

            // 添加修改用户信息字典
            newMessage: {},
            dialogVisible: false,

            // 引入ico图标
            Edit: markRaw(Edit), Loading: markRaw(Loading), Delete: markRaw(Delete), Search: markRaw(Search),
            // 编辑、添加按钮判定
            editBtn: false,
            // 选择字段
            select_type: '',
            // 字段值
            select_value: '',
            deleteLoading: false,
            disabledLoading: false,
            saveLoading: false,
            loading_table: false

        }
    },
    components: {Pages},
    mounted() {
        this.getMessageData()
    },
    methods: {
        // 获取消息列表
        getMessageData(current_page = 1, page_size = 10) {
            this.loading_table = true
            // 搜索过滤
            const search_items = {}
            if (this.select_type && this.select_value) {
                search_items[this.select_type] = this.select_value
            }
            // 发送列出通知请求
            MessageApi({
                search_items: search_items,
                action: 'list',
                pageSize: page_size,
                pageNum: current_page
            }).then(res => {
                if (res) {
                    this.messageData = res['retlist']
                    this.total = res['total']
                    this.loading_table = false
                }
            })
        },


        changeDialogVisible(mode, item = {}) {
            if (mode === 'modify') {
                this.newMessage = item
            } else {
                this.newMessage = {}
            }
            this.newMessage.action = mode
            this.dialogVisible = true
        },

        operateMessage() {
            this.saveLoading = true
            // 发送添加通知请求
            MessageApi(this.newMessage).then(res => {
                if (res) {
                    this.getMessageData()
                    ElMessage.success(`${this.newMessage.action}成功！`)
                }
                this.saveLoading = false
            })
        },

        // 删除
        deleteMessage(id) {
            this.deleteLoading = true
            ElMessageBox.confirm(
                '确认删除通知?',
                'Warning',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                }
            ).then(() => {
                MessageApi({action: 'delete', message_id: id}).then(res => {
                    if (res) {
                        this.getMessageData()
                    }
                    this.deleteLoading = false
                })
            }).catch(() => {
            })
        },

        // 禁用、启用
        disable(data) {
            this.disabledLoading = true
            MessageApi({action: 'modify', status: !data.status, id: data.id}).then(res => {
                if (res) {
                    this.getMessageData()
                }
                this.disabledLoading = false
            })
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
    height: calc(72vh);
    overflow-y: scroll;
}

</style>