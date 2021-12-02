<template>
    <!--   标签页    -->
    <el-tabs type="border-card">
        <el-tab-pane label="状态管理">
            <!--新闻表格-->
            <el-table :data="tableData" stripe style="width: 100%" border max-height="600">
                <!--表格id字段-->
                <el-table-column prop="id" label="Id" sortable min-width="5%"/>
                <!--表格title字段-->
                <el-table-column prop="title" label="Title" min-width="55%">
                    <template #default="scope">
                        <el-popover effect="light" trigger="hover" placement="top">
                            <template #default>
                                <p>{{ scope.row.title }}</p>
                                <p></p>
                                <p>{{ scope.row.content }}</p>
                            </template>
                            <template #reference>
                                <div class="name-wrapper">
                                    <el-tag size="medium">{{ scope.row.title }}</el-tag>
                                </div>
                            </template>
                        </el-popover>
                    </template>
                </el-table-column>
                <!--表格news_type字段-->
                <el-table-column prop="news_type" label="Type" sortable min-width="10%"/>
                <!--表格author字段-->
                <el-table-column prop="author__realName" label="Author" sortable min-width="10%"/>
                <!--表格状态字段-->
                <el-table-column min-width="30%" prop="status" label="状态" :filters="[
                        { text: '禁用', value: 0 },
                        { text: '正常', value: 1 },
                        { text: '热点', value: 2 },]"
                                 :filter-method="filterHandler">
                    <template #default="scope">
                        <el-slider v-model="scope.row.status" :max="2" show-input show-stops></el-slider>
                    </template>
                </el-table-column>
            </el-table>
        </el-tab-pane>
        <el-tab-pane label="添加">
            <span>开启批量添加模式：</span>
            <el-switch v-model="isAdds" inline-prompt active-text="是" inactive-text="否"></el-switch>
            <div v-if="isAdds">1</div>
            <div v-else>
                <el-form :model="addForm" label-width="120px">
                    <el-form-item label="新闻标题：">
                        <el-input v-model="addForm.title"></el-input>
                    </el-form-item>
                    <el-form-item label="新闻内容：">
                        <el-input type="textarea" v-model="addForm.content"></el-input>
                    </el-form-item>
                    <div style="display: flex;margin-left: 5px">
                        <el-select v-model="addForm.news_type" placeholder="选择新闻类型">
                            <el-option label="校园" value="校园"></el-option>
                            <el-option label="社会" value="社会"></el-option>
                        </el-select>
                        <el-radio v-model="addForm.status" label=0>cold</el-radio>
                        <el-radio v-model="addForm.status" label=1>warm</el-radio>2
                        <el-radio v-model="addForm.status" label=2>hot</el-radio>
                    </div>
                </el-form>
            </div>
        </el-tab-pane>
        <el-tab-pane label="Role">Role</el-tab-pane>
        <el-tab-pane label="Task">Task</el-tab-pane>
    </el-tabs>
</template>

<script>
import request from "../../utils/request";
import {ElMessage} from "element-plus";

export default {
    name: "news",
    data() {
        return {
            tableData: [],
            isAdds: false,
            addForm: {
                title: '',
                content: '',
                news_type: '',
                status: 1
            }
        }
    },
    mounted() {
        this.before()
    },

    methods: {
        before() {
            const that = this
            request.post('/api/notice/news', {
                action: 'list', news_type: 'ALL'
            }).then(res => {
                const data = res.data
                console.log(data)
                if (data['ret'] === 0) {
                    that.tableData = data['retlist']
                } else {
                    ElMessage.error('服务器错误')
                }
            })
        },
        // 列表筛选
        filterHandler(value, row, column) {
            const property = column['property']
            return row[property] === value
        },
    }

}
</script>

<style scoped>

</style>
