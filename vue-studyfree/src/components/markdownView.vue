<template>
    <div class="markdown-body" v-html="articleContent"></div>
</template>

<script>
import {marked} from "marked"
import request from "@/api/request";

export default {
    name: "markdownView",
    data() {
        return {
            articleContent: ""
        }
    },
    components: {},
    mounted() {
        request.get(`/fileStream?action=list&filename=编写测试用例.md&type=md`).then(res => {
            this.articleContent = marked(res['mdContent'])
        })
    }
}
</script>

<style scoped>
.markdown-body {
    box-sizing: border-box;
    min-width: 200px;
    max-width: 980px;
    margin: 0 auto;
    padding: 45px;
    position: relative;
}

@media (max-width: 767px) {
    .markdown-body {
        padding: 15px;
    }
}

</style>
