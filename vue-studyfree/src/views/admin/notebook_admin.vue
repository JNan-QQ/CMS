<template>
    <el-table :data="notebookData" style="width: 100%" v-loading="loading_table" element-loading-text="加载中...">
        <el-table-column type="expand">
            <template #default="props">
                <md-editor v-model="props.row.content" previewOnly/>
            </template>
        </el-table-column>
        <el-table-column label="id" prop="id"/>
        <el-table-column label="title" prop="title"/>
        <el-table-column label="username" prop="user_id__username"/>
        <el-table-column label="time" prop="time"/>
        <el-table-column label="status">
            <template #default="props">
                <el-slider v-model="props.row.status" :step="1" show-stops :min="1" :max="2" size="small"
                           @change="modify(props.row.status,props.row.id)"></el-slider>
            </template>
        </el-table-column>
    </el-table>
</template>

<script>
import MdEditor from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import {NoteBookApi} from "@/api/admin";
import {ElMessage} from "element-plus";

export default {
    name: "notebook_admin",
    components: {MdEditor},
    data() {
        return {
            notebookData: [],
            loading_table: false
        }
    },
    mounted() {
        this.getNoteBookData()
    },
    methods: {
        getNoteBookData() {
            this.loading_table = true
            NoteBookApi({action: 'list'}).then(res => {
                if (res) {
                    this.notebookData = res['retlist']
                    this.loading_table = false
                }
            })
        },
        modify(val, id) {
            NoteBookApi({action: 'modify', 'note_id': id, status: val}).then(res => {
                if (res) {
                    ElMessage({
                        message: '操作成功',
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