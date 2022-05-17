<template>
    <div class="note-view">
        <!--        笔记操作        -->
        <el-card class="opt"
                 :body-style="{ borderRight: '#444040 dashed 1px',borderRadius:'3px 0 0 3px',
                 backgroundImage:`url(${random_image})`,height: '94%',display:'flex',flexDirection: 'column',
                 alignItems: 'center',justifyContent: 'space-between'}"
                 v-if="active_page!==-1">
            <div class="book-title">
                {{ page_lm[active_page] }}&nbsp;{{ bjList[active_page].title }}&nbsp;
                <el-icon @click="modifyTitle(bjList[active_page].id)" class="edit-title">
                    <edit/>
                </el-icon>
            </div>

            <!--        页签          -->
            <div class="page-label1">
                <el-button-group>
                    <el-button @click="isEdit=true" v-if="!isEdit" :icon="Edit" title="编辑该笔记" size="large"
                               type="primary"
                               circle/>
                    <el-button v-if="isEdit" @click="isEdit=false" :icon="Close" title="返回，不保存" size="large"
                               type="info" circle/>
                    <el-button v-if="isEdit" @click="saveNoteBook(bjList[active_page].id,bjList[active_page].content)"
                               :loading="saveLoading" title="保存该笔记" size="large" type="success" circle :icon="Check"/>
                </el-button-group>
                <el-button-group>
                    <el-button :icon="DocumentAdd" size="large" type="warning" circle @click="addNoteBook"
                               title="新增笔记章"/>
                    <el-button @click="deleteNoteBook(bjList[active_page].id)" :loading="deleteLoading" :icon="Remove"
                               title="删除笔记" size="large" type="danger" circle/>
                </el-button-group>
            </div>
        </el-card>

        <!--        笔记主题            -->
        <el-card
            :body-style="{ padding: '3px 2px 3px 0',borderLeft: '#444040 dashed 1px',borderRadius:'0 3px 3px 0',height:'100%',zIndex: 1}"
            class="book">
            <el-image :src="random_image" fit="cover" class="cover" v-if="active_page===-1"/>

            <div style="margin: 2px;" v-else>
                <md-editor v-if="isEdit" v-model="bjList[active_page].content"
                           @onSave="saveNoteBook(bjList[active_page].id,bjList[active_page].content)"
                           @onUploadImg="onUploadImg" :preview="false"
                />
                <md-editor v-else v-model="bjList[active_page].content" previewOnly/>
            </div>
        </el-card>
        <el-icon v-if="active_page===-1" style="z-index: 2;position: absolute" :size="30" class="view-tools"
                 @click="changeNoteBookCover">
            <Setting/>
        </el-icon>
        <el-icon class="book-flg" @click="backTop" :class="{opens:active_page!==-1,'not-opens':active_page===-1}">
            <CollectionTag/>
        </el-icon>
        <!--        标签          -->
        <div class="page-label">
            <div :style="styleObject[index]" v-for="(item,index) in bjList" :title="item.title" @click="goToPage(index)"
                 :class="{'show-page-flg':active_page===index,'not-show-page-flg':active_page!==index}">
                {{ page_lm[index] }}
            </div>
        </div>


    </div>

</template>

<script>
import {noteContent} from "@/api/common";
import Pages from "@/components/pages";
import {Edit, DocumentAdd, CollectionTag, Remove, Close, Check, Setting} from "@element-plus/icons";
import MdEditor from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'
import {ElMessage, ElMessageBox} from "element-plus";
import request from "@/api/request";
import {markRaw} from "vue";

export default {
    name: "noteView_test",
    components: {Pages, Edit, MdEditor, Remove, Close, Check, CollectionTag, Setting},
    data() {
        return {
            bjList: [],
            active_page: -1,
            isEdit: false,
            saveLoading: false,
            deleteLoading: false,
            random_image: localStorage.getItem('book-view')||require('@/assets/others/notebookCover.jpg'),
            styleObject: [],
            page_lm: ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ'],
            DocumentAdd: markRaw(DocumentAdd),
            Edit: markRaw(Edit),
            Remove: markRaw(Remove),
            Close: markRaw(Close),
            Check: markRaw(Check)
        }
    },
    mounted() {
        this.before()
        this.changeStyle()
    },
    watch: {},
    methods: {
        // 获取 笔记数据
        before(mode = null) {
            this.loading = true
            noteContent({action: 'listNoteBook'}).then(res => {
                if (res) {
                    this.bjList = res['retlist']
                }
                this.loading = false
                if (mode) {
                    this.active_page = 0
                }
            })
        },
        // 笔记页面跳转
        goToPage(index) {
            this.isEdit = false
            this.active_page = index
        },

        // 点击图片回到顶部方法，加计时器是为了过渡顺滑
        backTop() {
            if (this.active_page === -1 && this.bjList.length === 0) {
                this.addNoteBook(true)
            } else if (this.active_page === -1 && this.bjList.length !== 0) {
                this.active_page = 0
            } else if (this.active_page !== -1) {
                this.isEdit = false
                this.active_page = -1
            }
        },

        // 样式表
        changeStyle() {
            // 颜色
            let color_flg = [
                '#ff4500',
                '#ff8c00',
                '#ffd700',
                '#1e90ff',
                '#c71585',
                'rgba(255, 69, 0, 0.68)',
                'rgb(255, 120, 0)',
                'hsl(181, 100%, 37%)',
                'hsla(209, 100%, 56%, 0.73)',
                '#c7158577',
            ]
            // 背景图
            // let back_img = [
            //     'https://tse4-mm.cn.bing.net/th/id/OIP-C._BGhMuCP3y7uYFc2XJD8XwHaEK?pid=ImgDet&rs=1',
            // ]
            // let user_image_book = localStorage.getItem('book-view')
            // if (user_image_book){
            //     this.random_image = user_image_book
            // }else {
            //     this.random_image = back_img[Math.floor(Math.random() * (back_img.length - 1))]
            // }

            for (let i = 0; i < this.page_lm.length; i++) {
                this.styleObject.push({
                    backgroundColor: color_flg[Math.floor(Math.random() * (color_flg.length - 1))],
                    marginTop: `${Math.floor(Math.random() * (40 - 10))}px`,
                    marginBottom: `${Math.floor(Math.random() * (40 - 10))}px`,
                })
            }
        },

        //添加书籍
        addNoteBook(mode = null) {
            noteContent({action: 'addNoteBook'}).then(res => {
                this.before(mode)
            })
        },

        // 保存
        saveNoteBook(id, text) {
            this.saveLoading = true
            noteContent({action: 'modifyNoteBook', 'note_id': id, 'content': text}).then(res => {
                this.before();
                this.saveLoading = false
                this.isEdit = false
                ElMessage({
                    message: '保存成功',
                    type: 'success',
                })
            })
        },

        // 删除书籍
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
                    this.active_page -= 1
                    ElMessage({
                        type: 'success',
                        message: '删除笔记成功',
                    })
                })
            }).catch(() => {
            })
        },

        // 修改书籍名称
        modifyTitle(id) {
            ElMessageBox.prompt('请输入笔记名称', 'edit...', {
                confirmButtonText: 'OK',
                cancelButtonText: 'Cancel',
                inputPattern: /^[\u4e00-\u9fa5\w\s]{1,20}$/,
                inputErrorMessage: '请输入1~20字符，不包含特殊字符',
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

        // 上传图片
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

        changeNoteBookCover() {
            ElMessageBox.prompt('请图片url链接', 'input...', {
                confirmButtonText: 'OK',
                inputPattern: /^((http|https):\/\/)?(([A-Za-z0-9]+-[A-Za-z0-9]+|[A-Za-z0-9]+)\.)+([A-Za-z]+)[/\?\:]?.*$/,
                inputErrorMessage: 'https://.....',
            }).then(({value}) => {
                localStorage.setItem('book-view',value)
                this.random_image = value
            })
        },
    }
}
</script>

<style scoped lang="less">
.note-view {
    position: relative;
    height: calc(100vh - 120px);
    max-width: 1100px;
    margin: 10px auto auto;
    display: flex;
    align-items: center;
    justify-content: center;

    .el-card.opt, .el-card.book {
        height: 72%;
        box-shadow: 4px 4px 5px 1px #8b8b8b;
    }

    .el-card.opt {
        width: 16%;
        z-index: 1;

        .noteBtn {
            display: flex;
            flex-direction: column;
            align-items: center;
            height: 46%;

            button {
                margin: 10px 0;
            }
        }

        .down {
            justify-content: flex-end;
        }

        .book-title {
            font-size: 22px;
            writing-mode: vertical-lr;
            box-shadow: 10px 10px 5px grey;
            background-color: white;
            color: black;
            mix-blend-mode: difference;

            .edit-title:hover {
                color: cadetblue;
            }
        }

        .page-label1 {
            display: flex;
            flex-direction: column;
            align-items: center;

            .el-button-group {
                margin-top: 10px;
            }
        }
    }

    .el-card.book {
        width: 84%;
        z-index: 1;

        .el-image.cover {
            width: 100%;
            height: 99%;
        }

    }

    .view-tools {
        color: rgba(0, 0, 0, 0);
    }

    .view-tools:hover {
        color: #fa9507;
    }

    .book-flg {
        position: inherit;
        bottom: -37%;
        background-color: yellowgreen;
        height: 40px;

        svg {
            margin-top: 80%;
            color: #fa9507;
        }
    }

    .book-flg.opens {
        right: 80%;
    }

    .book-flg.not-opens {
        right: 84%;
    }

    .book-flg:hover {
        box-shadow: inset 0 0 9px #c92a15;
    }

    .page-label {
        height: 72%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        position: inherit;
        right: 20px;

        div {
            height: 22px;
            width: 40px;
            text-align: center;
            border-radius: 0 2px 2px 0;
            background-color: #efe3b4;
            position: relative;
            transition: 0.3s;
            opacity: 0;
            transform: translateY(100%);

        }

        div:hover {
            box-shadow: inset 0 0 9px #00ff90;
        }

        .show-page-flg {
            z-index: 1;
        }

        .not-show-page-flg {
            z-index: 0;
        }
    }

    .page-label:hover div {
        opacity: 1;
        transform: translateY(0);

    }
}

#md-editor-v3 {
    height: calc(60vh);
}

#md-preview {
    height: calc(60vh);
    overflow-y: auto;
}
</style>