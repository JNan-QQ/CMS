<template>
    <div class="top">
        <div class="title">
            <div class="md_name">
                <el-icon @click="toArticle">
                    <d-arrow-left/>
                </el-icon>
                <span>{{ title }}</span></div>
            <div class="btn-class">
                <el-button @click="downloadMarkdown">下载</el-button>
            </div>
        </div>
    </div>
    <div class="markdown-body" v-html="articleContent"></div>
</template>

<script>
import {marked} from "marked"
import {downloadFree, getContent} from "@/api/common";
import {DArrowLeft} from "@element-plus/icons";
import {ElMessage, ElMessageBox} from "element-plus";

export default {
    name: "markdownView",
    data() {
        return {
            articleContent: "",
            baseArticleContent: "",
            title:"",
        }
    },
    components: {DArrowLeft},
    mounted() {
        const param = this.$route.query
        getContent({action: 'markdownContent', tag_id: param['id']}).then(res => {
            this.baseArticleContent = res['mdContent']
            this.title = res['title']
            this.articleContent = marked(res['mdContent'])
        })
    },
    methods: {
        toArticle() {
            window.close();
        },
        downloadMarkdown() {
            ElMessageBox.confirm(
                '确认花费 50 F币下载文章吗？',
                'Warning',
                {
                    confirmButtonText: '确认',
                    cancelButtonText: '取消',
                    type: 'warning',
                }
            ).then(() => {
                downloadFree(50).then(res => {
                    if (res) {
                        const blob = new Blob([this.baseArticleContent], {type: 'text/plain'})
                        const url = window.URL.createObjectURL(blob);
                        // 上面这个是创建一个blob的对象连链接，
                        const link = document.createElement('a');
                        // 创建一个链接元素，是属于 a 标签的链接元素，所以括号里才是a，
                        link.href = url;
                        // 把上面获得的blob的对象链接赋值给新创建的这个 a 链接
                        link.setAttribute('download', this.title + ".md")
                        // 设置下载的属性（所以使用的是download），这个是a 标签的一个属性
                        // 后面的是文件名字，可以更改
                        link.click();
                        // 使用js点击这个链接
                    }
                })

            }).catch(() => {

            })

        }
    }
}
</script>

<style scoped lang="less">

.top {
    width: 100%;
    height: calc(10vh);
    border-bottom: #FFFFFF solid 1px;
    margin-top: 2px;
    margin-bottom: 5px;
    background-color: #5e729b;
    position: sticky;
    top: 0;
    right: 0;
    left: 0;
    color: #FFFFFF;

    .title {
        max-width: 980px;
        height: 100%;
        margin: 0 auto;
        display: flex;
        align-items: center;
        justify-content: space-between;

        .md_name {
            font-size: 20px;
            display: flex;
            align-items: center;

            .el-icon {
                background-color: #313b42;
                border-radius: 4px;
                width: 30px;
                height: 30px;
            }

            span {
                margin-left: 10px;
            }
        }
    }
}


.markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
    position: relative;
    height: calc(90vh - 10px);
    overflow-y: auto;
}

@media (max-width: 767px) {
    .markdown-body {
        padding: 15px;
    }
}

</style>
