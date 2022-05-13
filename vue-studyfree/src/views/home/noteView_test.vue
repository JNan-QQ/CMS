<template>
    <div class="noteView" id="noteView" v-loading="loading" element-loading-background="#414444"
         element-loading-text="加载中...">
        <div class="noteBox">
            <div class="notebook">
                <div class="bJ">
                    <el-collapse v-model="activeName" accordion v-for="(item,index) in bjList">
                        <el-collapse-item :name="index + 1" :id="'bj'+index">
                            <template #title>
                                {{ item['title'] }}
                                <el-icon class="header-icon" style="margin-left: 2px" @click="modifyTitle(item.id)">
                                    <edit/>
                                </el-icon>
                            </template>
                            <div class="noteBtn" v-if="index + 1===activeName">
                                <el-button @click="isEdit=true" v-if="!isEdit">编辑</el-button>
                                <el-button v-if="isEdit" @click="isEdit=false">返回</el-button>
                                <el-button v-if="isEdit" @click="saveNoteBook(item.id,item.content)"
                                           :loading="saveLoading">保存
                                </el-button>
                                <el-button @click="deleteNoteBook(item.id)" :loading="deleteBtn">删除</el-button>
                            </div>
                            <div style="margin: 2px;" v-if="index + 1===activeName">
                                <md-editor v-if="isEdit" v-model="item.content"
                                           @onSave="saveNoteBook(item.id,item.content)"
                                           @onUploadImg="onUploadImg"
                                />
                                <md-editor v-else v-model="item.content" previewOnly/>
                            </div>
                        </el-collapse-item>
                    </el-collapse>
                </div>
                <div class="no-login" v-if="!isLogin">你还未登录┗|｀O′|┛ 嗷~~</div>
            </div>
            <div class="right" v-if="isLogin">
                <el-affix :offset="80">
                    <el-tooltip content="添加新笔记" placement="right-start" effect="light">
                        <el-button :icon="DocumentAdd" size="default" type="warning" circle
                                   @click="addNoteBook"></el-button>
                    </el-tooltip>
                    <el-tooltip content="全部折叠" placement="right-start" effect="light">
                        <el-button :icon="Remove" size="default" type="primary" circle
                                   style="margin-left: 0;margin-top: 8px;"
                                   @click="activeName=0"></el-button>
                    </el-tooltip>
                    <el-tooltip content="回到顶部" placement="right-start" effect="light">
                        <el-button :icon="CaretTop" size="default" type="success" circle
                                   style="margin-left: 0;margin-top: 8px;" @click="backTop">
                        </el-button>

                    </el-tooltip>
                </el-affix>
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
import MdEditor from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'
import {noteContent} from "@/api/common"
import {DocumentAdd, Edit, Remove, CaretTop} from "@element-plus/icons"
import {ElMessage, ElMessageBox} from "element-plus"
import request from "../../api/request"
import {markRaw} from "vue"

export default {
    name: "noteView",
    data() {
        return {
            isEdit: false,
            activeName: 1,
            bjList: [],
            saveLoading: false, deleteBtn: false,
            DocumentAdd: markRaw(DocumentAdd), Remove: markRaw(Remove), CaretTop: markRaw(CaretTop),
            loading: false,
        }
    },
    components: {MdEditor, Edit},
    mounted() {
        this.before()
    },
    computed:{
        isLogin(){
            return this.$store.state.userdata.isLogin
        }
    },
    methods: {
        before() {
            this.loading = true
            noteContent({action: 'listNoteBook'}).then(res => {
                if (res) {
                    this.bjList = res['retlist']
                }
                this.loading = false
            })
        },
        addNoteBook() {
            noteContent({action: 'addNoteBook'}).then(res => {
                this.before()
            })
        },
        deleteNoteBook(id) {
            ElMessageBox.confirm(
                '确认删除改笔记？',
                '提示',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                }
            ).then(() => {
                this.deleteBtn = true
                noteContent({action: 'deleteNoteBook', 'note_id': id}).then(res => {
                    this.before()
                    this.deleteBtn = false
                    ElMessage({
                        type: 'success',
                        message: '删除笔记成功',
                    })
                })
            }).catch(() => {
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
            const file_name = `img_notebook_${this.bjList[this.activeName - 1].id}_timeR.png`
            const res = await Promise.all(
                Array.from(files).map((file) => {
                    return new Promise((rev, rej) => {
                        const form = new FormData();
                        form.append('file', file);
                        form.append('action', 'uploadImg');
                        form.append('file_name', file_name);
                        form.append('file_type', 'notebook');
                        request.post('/common/other', form).then((res) => rev(res)).catch((error) => rej(error));
                    });
                })
            );
            callback(res.map((item) => 'api_file/' + item.url));
        },

        // 点击图片回到顶部方法，加计时器是为了过渡顺滑
        backTop() {
            this.activeName = 1
            document.getElementById('noteView').scrollTop = 0
        },

    },
}
</script>

<style scoped lang="less">
.noteView {
    position: relative;
    height: calc(100vh - 140px);
    overflow-y: auto;
    background-color: #414444;

    .noteBox {
        max-width: 1000px;
        margin: 10px auto auto;
        display: flex;

        .notebook {
            border-right: #5e729b solid 1px;
            position: relative;
            margin-bottom: 10px;
            margin-right: 5px;
            padding-top: 4px;
            padding-right: 3px;
            width: calc(94vw);


            .bJ {
                background-color: #FFFFFF;
                border-radius: 20px;

                .el-collapse {
                    padding: 10px 20px;
                    border-bottom: #04121c;
                    border-top: #04121c;
                }

                .noteBtn {
                    margin: 2px;
                    display: flex;
                    justify-content: right;
                    border-bottom: #eeeeee solid 2px;
                }
            }

            .no-login {
                text-align: center;
                font-size: 22px;
                margin-top: calc(10vh);
                background: linear-gradient(to right, #ec5807, #0bee8c);
                -webkit-background-clip: text;
                color: transparent;
            }
        }

        .right {
            width: calc(5vw);
            margin-left: 2px;
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

#md-editor-v3 {
    background: #f9f9f9;
}


@media (max-width: 767px) {
    .noteView {
        padding: 15px;
    }
}

</style>
