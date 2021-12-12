<template>
    <!--   标签页    -->
    <el-tabs type="border-card">
        <el-tab-pane label="状态管理">
            <!--新闻表格-->
            <el-table :data="tableData" stripe style="width: 100%" border max-height="600">
                <!--表格id字段-->
                <el-table-column prop="id" label="Id" sortable min-width="10%"/>
                <!--表格title字段-->
                <el-table-column prop="title" label="Title" min-width="50%">
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
                <el-table-column prop="news_type__types" label="Type" sortable min-width="15%"/>
                <!--表格author字段-->
                <el-table-column prop="author__realName" label="Author" sortable min-width="15%"/>
                <!--表格状态字段-->
                <el-table-column min-width="20%" prop="status" label="状态" :filters="[
                        { text: '禁用', value: 0 },
                        { text: '正常', value: 1 },
                        { text: '热点', value: 2 },]"
                                 :filter-method="filterHandler">
                    <template #default="scope">
                        <el-slider v-model="scope.row.status" :max="2" show-stops
                                   @change="changeStatus(scope.row.status, scope.row.id)"></el-slider>
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
                        <Editor @onEditor="editorContent" base-txt=""/>
                    </el-form-item>
                    <el-form-item label="类型、状态：">
                        <el-select v-model="addForm.news_type" placeholder="选择新闻类型">
                            <el-option v-for="item in newsType" :label=item.types :value=item.id></el-option>
                        </el-select>
                        <el-radio v-model="addForm.status" label=0>cold</el-radio>
                        <el-radio v-model="addForm.status" label=1>warm</el-radio>
                        <el-radio v-model="addForm.status" label=2>hot</el-radio>
                    </el-form-item>
                    <el-form-item>
                        <el-button @click="onSubmitOne"
                                   style="display:block;margin:0 auto;background-color: #99a9bf;width: 40%">提交
                        </el-button>
                    </el-form-item>
                </el-form>
            </div>
        </el-tab-pane>
        <el-tab-pane label="修改">
            <el-table :data="tableData" @expand-change="modify_data">
                <el-table-column type="expand">
                    <template #default="props">
                        <el-form label-width="120px">
                            <el-form-item label="标题：">
                                <el-input v-model="newFrom.title" label="Title" clearable/>
                            </el-form-item>
                            <el-form-item label="内容：">
                                <Editor @onEditor="editorContent" :base-txt="props.row.content"/>
                            </el-form-item>
                            <el-button @click="modify_btn"
                                       style="display:block;margin:10px auto;background-color: #99a9bf;width: 40%">确认
                            </el-button>
                        </el-form>
                    </template>
                </el-table-column>
                <el-table-column label="ID" prop="id"/>
                <el-table-column label="Title" prop="title"/>
                <el-table-column label="Author" prop="author__realName"/>
                <el-table-column label="Delete" #default="props">
                    <el-button type="danger" :icon="Delete" round @click="delete_btn(props.row.id)"></el-button>
                </el-table-column>
            </el-table>
        </el-tab-pane>
    </el-tabs>
</template>

<script>
import Editor from '../../utils/editor'
import {Delete} from "@element-plus/icons"
import {markRaw} from "vue"
import {addNews, deleteNews, listNews, listNewsType, modifyNews} from "../../api/News";

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
            },
            newFrom: {
                title: '',
                content: '',
                news_id: 0
            },
            Delete: markRaw(Delete),
            newsType:[]
        }
    },
    components: {Editor, Delete},
    mounted() {
        this.before()
        listNewsType(this)
    },
    watch: {},

    methods: {
        before() {
            listNews({news_type: 'ALL'}, this)
        },

        // 列表筛选
        filterHandler(value, row, column) {
            const property = column['property']
            return row[property] === value
        },

        // 改变新闻状态
        changeStatus(newStatus, id) {
            modifyNews({status: newStatus, news_id: id}, this)
        },

        // 添加一个新闻
        onSubmitOne() {
            addNews(this.addForm,this)
        },

        // 接受子组件富文本内容
        editorContent(val) {
            this.addForm.content = val
            this.newFrom.content = val
        },

        // 修改新闻内容
        modify_data(row, expandedRows) {
            const data = expandedRows[0]
            if (data) {
                this.newFrom.title = data['title']
                this.newFrom.news_id = data['id']
            }
        },
        modify_btn() {
            modifyNews(this.newFrom,this)
        },

        // 删除新闻
        delete_btn(news_id) {
            deleteNews({news_id: news_id},this)
        },

    }

}
</script>

<style scoped>
/*.el-radio {*/
/*    margin-left: 15px;*/
/*}*/

/*.el-form-item {*/
/*    margin: 5px 20px 5px 10px;*/
/*}*/

</style>
