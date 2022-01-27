<template>
    <el-collapse v-model="activeName" accordion>
        <el-collapse-item :name="tags.id" v-for="tags in articleData">
            <template #title>
                <span style="margin-left: 5px">{{tags.tag_name}}</span>
                <el-button class="title-btn" @click="">添加章节</el-button>
                <el-button class="title-btn" @click="editBtn=true;editType='tag1'">编辑</el-button>
                <el-button class="title-btn">删除</el-button>
            </template>
            <div class="tag1">
                <el-card class="box-card" v-for="tag2 in tags['tag_child']">
                    <template #header>
                        <div class="card-header">
                            <span>{{ tag2.tag_name }}</span>
                            <div>
                                <el-button class="button" type="success" size="small">添加章节内容</el-button>
                                <el-button class="button" type="danger" size="small">删除</el-button>
                            </div>
                        </div>
                    </template>
                    <div style="display: flex">
                        <div v-for="content in tag2['tag_child']" class="content">
                            <el-image :src="'/api/static/' + content['contentList'].images"></el-image>
                            <span>{{ content.tag_name }}</span>
                        </div>
                    </div>

                </el-card>
            </div>
        </el-collapse-item>
    </el-collapse>

    <!-- 添加、编辑页面   -->
    <el-dialog v-model="editBtn" title="文章信息" width="30%" destroy-on-close center>
        <el-form ref="form" :model="newTags" label-position="left" label-width="80px">
            <el-form-item label="标签名：" v-if="editType==='tag1'">
                <el-input v-model="newTags.tag_name"></el-input>
            </el-form-item>
            <el-form-item label="链接标签：" v-if="editType!=='tag1'">
                <el-input v-model="newTags.tag_id"></el-input>
            </el-form-item>
            <el-form-item label="状态：">
                <el-input v-model="newTags.tag_name"></el-input>
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

export default {
    name: "article_admin",
    data() {
        return {
            articleData: [],
            activeName: '1',
            editBtn:false,
            newTags:{},
            editType:''
        }
    },
    mounted() {
        this.getArticleData()
    },
    methods: {
        getArticleData() {
            // 发送列出账号请求
            ArticleApi({action: 'list'}).then(res => {
                if (res) {
                    this.articleData = res['retlist']
                }
            })

        },
        modify_add_Article(){

        },
        // 取消操作
        editBtnCancel() {
            this.editBtn = false
            this.newTags = {}
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
        }
    }
}

.title-btn{
    margin: auto;
    position: relative;
}

</style>
