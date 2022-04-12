<template>
    <el-button style="float: right;position: relative" type="success" size="small"
               @click="addBtn('tag1')">添加Tag标签
    </el-button>
    <el-collapse v-model="activeName" accordion v-loading="loading_table" element-loading-text="加载中...">
        <el-collapse-item :name="tags.id" v-for="tags in articleData">
            <template #title>
                <span style="margin-left: 5px">{{ tags.tag_name }}</span>
                <el-button class="title-btn" @click="addBtn('tag2',tags.id)">添加子章节</el-button>
                <el-button class="title-btn" @click="editTag(tags.id,'tag1')">编辑Tag标签</el-button>
                <el-button class="title-btn" @click="deleteTag(tags.id)">删除Tag标签</el-button>
                <span v-if="tags.status===2" style="color: red">已禁用显示</span>
            </template>
            <div class="tag1">
                <el-card class="box-card" v-for="tag2 in tags['tag_child']">
                    <template #header>
                        <div class="card-header">
                            <span>{{ tag2.tag_name }}</span>
                            <div style="position: relative">
                                <el-button class="button" type="success" size="small" @click="addBtn('tag3',tag2.id)">
                                    添加章节内容
                                </el-button>
                                <el-button class="button" size="small" @click="editTag(tag2.id,'tag2')">编辑章节标签
                                </el-button>
                                <el-button class="button" type="danger" size="small" @click="deleteTag(tag2.id)">删除
                                </el-button>
                            </div>
                        </div>
                    </template>
                    <div style="display: flex">
                        <div v-for="content in tag2['tag_child']" class="content">
                            <div>
                                <el-image :src="'api_file/static/' + content['contentList'].images"></el-image>
                                <span>{{ content.tag_name }}</span>
                            </div>
                            <div class="btn-group">
                                <el-button type="primary" :icon="Edit" circle size="small"
                                           @click="editArticleContent(content['contentList'].id)"></el-button>
                                <el-button type="danger" :icon="Delete" circle size="small"
                                           @click="deleteTag(content.id)"></el-button>
                            </div>
                        </div>
                    </div>

                </el-card>
            </div>
        </el-collapse-item>
    </el-collapse>

    <!--  文章内容编辑  -->
    <el-dialog v-model="articleContentVisible" title="修改显示图片与链接文档">
        <el-form ref="formRef" :model="newContent" label-width="120px">
            <el-form-item label="图片路径">
                <el-select v-model="newContent.images">
                    <el-option
                        v-for="item in options_images"
                        :label="item['img_name']"
                        :value="item['img_path']"
                    >
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="文档路径">
                <el-select v-model="newContent['filePath']">
                    <el-option
                        v-for="item in options_md"
                        :label="item['md_name']"
                        :value="item['md_path']"
                    >
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="success" @click="modifyArticleContent">确认</el-button>
                <el-button type="warning" @click="editBtnCancel">取消</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>

    <!-- 添加、编辑页面   -->
    <el-dialog v-model="editBtn" title="文章信息" width="30%" destroy-on-close center>
        <el-form ref="form" :model="newTags" label-position="left" label-width="80px">
            <el-form-item label="标签名：">
                <el-input v-model="newTags.tag_name"></el-input>
            </el-form-item>
            <el-form-item label="状态：">
                <el-select v-model="newTags.status" placeholder="Select">
                    <el-option label="显示" value="1"></el-option>
                    <el-option label="禁用" value="2"></el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <el-button type="success" @click="modify_add_Article">确认</el-button>
                <el-button type="warning" @click="editBtnCancel">取消</el-button>
            </el-form-item>
        </el-form>
    </el-dialog>
</template>

<script>

import {ArticleApi} from "@/api/admin";
import {ElMessage, ElMessageBox} from "element-plus";
import {Edit, Delete} from "@element-plus/icons";
import {markRaw} from "vue";

export default {
    name: "article_admin",
    data() {
        return {
            articleData: [],
            activeName: '1',
            editBtn: false,
            newTags: {},
            editType: '',
            typeTagDict: {tag1: 1, tag2: 2, tag3: 3},
            articleContentVisible: false,
            newContent: {},
            Edit: markRaw(Edit), Delete: markRaw(Delete),
            options_images: [],
            options_md: [],
            loading_table: false
        }
    },
    mounted() {
        this.getArticleData()
    },
    methods: {
        getArticleData() {
            this.loading_table = true
            // 发送列出通知请求
            ArticleApi({action: 'list'}).then(res => {
                if (res) {
                    this.articleData = res['retlist']
                    this.loading_table = false
                }
            })

        },
        editTag(id, type) {
            this.editBtn = true
            this.editType = type
            this.newTags['action'] = 'modify'
            this.newTags['id'] = id
        },
        addBtn(type, tag_id) {
            this.editBtn = true
            this.editType = type
            this.newTags['action'] = 'add'
            this.newTags['tag_type'] = this.typeTagDict[type]
            if (tag_id) {
                this.newTags['tag_id'] = tag_id
            }
        },
        editArticleContent(id) {
            this.newContent['id'] = id
            this.newContent['action'] = 'modify_content'
            ArticleApi({action: 'img_md'}).then(res => {
                this.options_images = res['images']
                this.options_md = res['md']
                this.articleContentVisible = true
            })
        },
        // 添加编辑标签
        modify_add_Article() {
            ArticleApi(this.newTags).then(res => {
                if (res) {
                    this.editBtn = false
                    ElMessage({
                        message: '操作成功',
                        type: 'success',
                    })
                    this.getArticleData()
                }
            })
            this.newTags = {}
        },
        modifyArticleContent() {
            ArticleApi(this.newContent).then(res => {
                if (res) {
                    this.articleContentVisible = false
                    ElMessage({
                        message: '操作成功',
                        type: 'success',
                    })
                    this.getArticleData()
                }
            })
            this.newContent = {}
        },
        // 取消操作
        editBtnCancel() {
            this.editBtn = false
            this.articleContentVisible = false
            this.newTags = {}
            this.newContent = {}
        },
        // 删除标签
        deleteTag(id) {
            ElMessageBox.confirm(
                '删除该标签后子标签将会同时删除',
                '提示',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'info',
                }
            ).then(() => {
                ArticleApi({action: 'delete', 'id': id}).then(res => {
                    if (res) {
                        ElMessage({
                            message: '删除标签成功',
                            type: 'success',
                        })
                        this.getArticleData()
                    }
                })
            }).catch(() => {
            })
        },

    }
}
</script>

<style scoped lang="less">
.tag1 {
    display: flex;

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .text {
        font-size: 14px;
    }

    .box-card {
        width: 48%;
        margin: 1%;

        .content {
            width: 32%;
            margin: 1%;
            padding: 2px;
            text-align: center;
            display: flex;

            .btn-group {
                display: flex;
                flex-direction: column;

                .el-button + .el-button {
                    margin-left: 0;
                }
            }
        }
    }
}

.title-btn {
    margin: auto;
    position: relative;
}

</style>
