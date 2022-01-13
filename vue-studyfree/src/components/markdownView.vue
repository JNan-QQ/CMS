<template>
    <div class="top">
        <div class="title">
            <div class="md_name"><el-icon @click="toArticle"><d-arrow-left /></el-icon><span>这是一个标题</span></div>
            <div class="btn-class">
                <el-button>下载</el-button>
            </div>
        </div>
    </div>
    <div class="markdown-body" v-html="articleContent"></div>
</template>

<script>
import {marked} from "marked"
import {getContent} from "@/api/common";
import {DArrowLeft} from "@element-plus/icons";

export default {
    name: "markdownView",
    data() {
        return {
            articleContent: ""
        }
    },
    components: {DArrowLeft},
    mounted() {
        const param = this.$route.query
        getContent({action: 'markdownContent', tag_id: param['id']}).then(res => {
            this.articleContent = marked(res['mdContent'])
        })
    },
    methods:{
        toArticle(){
            window.close();
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

        .md_name{
            font-size: 20px;
            display: flex;
            align-items: center;
            .el-icon{
                background-color: #313b42;
                border-radius: 4px;
                width: 30px;
                height: 30px;
            }
            span{
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
