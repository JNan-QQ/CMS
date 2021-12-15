<template>
    <div class="view">
        <div class="title">{{ contents['title'] }}</div>
        <div class="msg">
            <el-row :gutter="20">
                <el-col :span="12"><div class="time">{{ contents['create_time'] }}</div></el-col>
                <el-col :span="12"><div class="author">{{ contents['author__realName'] }}</div></el-col>
            </el-row>
        </div>
        <div class="content" v-html="contents['content']"></div>
    </div>
</template>

<script>
import {getOneNews} from "../../api/News";

export default {
    name: "contentView",
    data() {
        return {
            contents: {},
        }
    },
    mounted() {
        const type = this.$route.query.type
        if (type === 'news') {
            this.news(this.$route.query.id)
        } else if (type === 'message') {
        } else {
        }
        if (this.contents) {

        }
    },
    methods: {
        news(id) {
            getOneNews({news_id: id}, this)
        }
    },
}
</script>

<style scoped>
.view {
    height: 700px;
}

.title {
    text-align: center;
}

.msg {
    text-align: justify;
    border-bottom: 1px solid var(--el-border-color-base);
    margin: 10px 5px 5px;
}
.author{
    float: right;
}

</style>
