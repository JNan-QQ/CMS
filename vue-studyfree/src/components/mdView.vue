
<script setup>
import {marked} from 'marked';
// 代码高亮
import hljs from 'highlight.js';
// 获取路由参数
import {useRoute} from 'vue-router'
// 自选代码高亮样式
// import 'highlight.js/scss/atom-one-dark.scss';
import {DArrowLeft} from "@element-plus/icons";
import {getArticleContent} from "@/api/common";
import {ref} from "vue";

// 用于记录标题数，根据业务代替
let count = 0;
// 记录标题内容
const head_stamp = [];

const param = useRoute().query

// marked设置
const rendererMD = new marked.Renderer();

// 调整标题内容
rendererMD.heading = (text, level) => {
    head_stamp.push({text, level});
    count++;
    return `<h${level} id="heading-${count}"><span class="h-text">${text}</span></h${level}>`;
};

// 设置图片内容，统一显示一张缓存图，用于懒加载~
rendererMD.image = (href, _, text) =>
    `<img data-src="${href}" src="/cos/2020/1211175603.png" alt="${text}">`;

marked.setOptions({
    highlight(code) {
        return hljs.highlightAuto(code).value
    },
    renderer: rendererMD
});


const rifle = getArticleContent({action: 'markdownContent', tag_id: param['id']}).then(res => {
    let mdArticleContent;
    mdArticleContent = res['mdContent']
    const title = res['title'];
    return [title,mdArticleContent]
})
console.log(rifle)

// 这里的html就是插入到页面的元素文本了
const html = marked(rifle[1]);

</script>


<template>
    <div class="top">
        <div class="title">
            <div class="md_name">
                <el-icon @click="this.$router.push('/Article');">
                    <d-arrow-left/>
                </el-icon>
                <span>{{ rifle[0] }}</span></div>
            <div class="btn-class">
                <el-button @click="">下载</el-button>
            </div>
        </div>
    </div>
    <!--    <div class="markdown-body" v-html="articleContent"></div>-->
    <div class="md-view">
        <div v-html="html"></div>
    </div>
</template>

<style scoped>

</style>