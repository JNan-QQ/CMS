<template>
    <div class="noteView">
        <div class="slide-item-table">
            <div class="text-center"><h2 class="slider_title">StudyFree，学习笔记好帮手！</h2>
                <p class="product-desctext">开开心心学习，快快乐乐生活</p>
            </div>
        </div>
        <div class="noteBox">
            <div class="notebook">
                <div style="display: flex;justify-content: right;margin-bottom: 5px">
                    <el-button @click="addNoteBook">新增</el-button>
                </div>
                <div class="bJ">
                    <el-collapse v-model="activeName" accordion v-for="(item,index) in bjList">
                        <el-collapse-item :name="index + 1">
                            <template #title>
                                {{ item['title'] }}
                                <el-icon class="header-icon" style="margin-left: 2px" @click="modifyTitle(item.id)">
                                    <edit/>
                                </el-icon>
                            </template>
                            <div
                                style="margin: 2px;display: flex;justify-content: right;border-bottom: #eeeeee solid 2px">
                                <el-button @click="isEdit=true" v-if="!isEdit">编辑</el-button>
                                <el-button v-if="isEdit" @click="isEdit=false">返回</el-button>
                                <el-button v-if="isEdit" @click="saveNoteBook(item.id,item.content)"
                                           :loading="saveLoading">保存
                                </el-button>
                                <el-button @click="deleteNoteBook(item.id)">删除</el-button>
                            </div>
                            <div style="margin: 2px;">
                                <md-editor v-if="isEdit" v-model="item.content"
                                           @onSave="saveNoteBook(item.id,item.content)"
                                           @onUploadImg="onUploadImg"
                                />
                                <md-editor v-else v-model="item.content" previewOnly/>
                            </div>
                        </el-collapse-item>
                    </el-collapse>
                </div>
            </div>
        </div>
    </div>
    <div class="blog-footer">
        <p>
            <a>关于我们</a>
            <span>|</span>
            <a>加入我们</a>
            <span>|</span>
            <a>联系我们</a>
        </p>
        <p class="down">
            <span>EveryOne © 个人学习备忘网站 </span><a>待备案 - 20220122 </a>
        </p>
    </div>
</template>

<script>
import MdEditor from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';
import {noteContent} from "@/api/common";
import {Edit} from "@element-plus/icons";
import {ElMessage, ElMessageBox} from "element-plus";
import request from "../../api/request";

export default {
    name: "noteView",
    data() {
        return {
            isEdit: false,
            activeName: 1,
            bjList: [],
            saveLoading: false
        }
    },
    components: {MdEditor, Edit},
    mounted() {
        this.before()
    },
    methods: {
        before() {
            noteContent({action: 'listNoteBook'}).then(res => {
                if (res) {
                    this.bjList = res['retlist']
                }
            })
        },
        addNoteBook() {
            noteContent({action: 'addNoteBook'}).then(res => {
                this.before()
            })
        },
        deleteNoteBook(id) {
            noteContent({action: 'deleteNoteBook', 'note_id': id}).then(res => {
                this.before()
            })
        },
        saveNoteBook(id, text) {
            this.saveLoading = true
            noteContent({action: 'modifyNoteBook', 'note_id': id, 'content': text}).then(res => {
                this.before();
                this.saveLoading = false
                ElMessage({
                    message: '保存成功',
                    type: 'success',
                })
            })
        },
        modifyTitle(id) {
            ElMessageBox.prompt('Please input your title', 'Tip', {
                confirmButtonText: 'OK',
                cancelButtonText: 'Cancel',
            }).then(({value}) => {
                noteContent({action: 'modifyNoteBook', 'note_id': id, 'title': value}).then(res => {
                    this.before()
                    ElMessage({
                        message: '修改成功',
                        type: 'success',
                    })
                })
            })
        },
        async onUploadImg(files, callback) {
            const file_name = `img_notebook_${this.bjList[this.activeName-1].id}_timeR.png`
            const res = await Promise.all(
                Array.from(files).map((file) => {
                    return new Promise((rev, rej) => {
                        const form = new FormData();
                        form.append('file', file);
                        form.append('action','uploadImg')
                        form.append('file_name',file_name)
                        request.post('/common/other', form).then((res) => rev(res)).catch((error) => rej(error));
                    });
                })
            );
            console.log(res)
            callback(res.map((item) => '/api/' + item.url));
        }
    },
}
</script>

<style scoped lang="less">
.noteView {
    position: relative;
    height: calc(100vh - 140px);
    overflow-y: auto;
    background-color: #414444;

    .slide-item-table {
        height: 200px;
        background-image: url("../../assets/coursebg.jpg");
        border-top: #FFFFFF solid 1px;
        border-bottom: #FFFFFF solid 1px;
        color: #FFFFFF;

        .text-center {
            text-align: center;
            margin-top: 60px;
            margin-bottom: 10px;

            .slider_title {
                font: 36px 'Arial Rounded MT Bold';
            }

            .product-desctext {
                font-size: 14px;
                margin-top: 10px;
            }
        }
    }

    .noteBox {
        border-left: 1px solid #eaeaea;
        max-width: 1000px;
        margin: auto;

        .notebook {
            position: relative;
            margin-bottom: 10px;
            margin-left: 12px;
            padding-top: 4px;

            .bJ {
                background-color: #FFFFFF;
                border-radius: 20px;

                .el-collapse {
                    padding: 10px 20px;
                    border-bottom: #04121c;
                    border-top: #04121c;
                }
            }
        }
    }
}

.blog-footer {
    padding: 20px 16px;
    font-size: 12px;
    color: #FFFFFF;
    text-align: center;
    height: auto;
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    border-top: #FFFFFF solid 1px;

    p {
        span {
            margin-left: 10px;
            margin-right: 10px;
        }
    }

    p.down {
        margin-top: 10px;
    }

}

@media (max-width: 767px) {
    .noteView {
        padding: 15px;
    }
}
</style>
