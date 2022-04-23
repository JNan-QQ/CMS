<template>
    <div class="top">
        <div class="title">
            <div class="md_name">
                <el-icon @click="this.$router.push('/Article');">
                    <d-arrow-left/>
                </el-icon>
                <span>{{ title }}</span></div>
            <div class="btn-class">
                <el-button @click="downloadMarkdown">下载</el-button>
            </div>
        </div>
    </div>

    <div class="md-view">
        <md-editor v-model="baseArticleContent" previewOnly/>
    </div>

    <el-collapse v-model="activeName" accordion class="mu-lu">
        <el-collapse-item :title="item.title" :name="index+1" v-for="(item,index) in headlamp">
            <ul>
                <li v-for="item1 in item.child"><a :href="'#'+item1.title">{{ item1.title }}</a></li>
            </ul>
        </el-collapse-item>
    </el-collapse>

</template>

<script>
import {marked} from "marked"
import {downloadFree, getArticleContent} from "@/api/common";
import {DArrowLeft} from "@element-plus/icons";
import {ElMessageBox} from "element-plus";
import MdEditor from 'md-editor-v3';

export default {
    name: "markdownView",
    data() {
        return {
            baseArticleContent: "",
            title: "",
            headlamp: [],
            activeName: 1
        }
    },
    components: {DArrowLeft, MdEditor},
    mounted() {
        const param = this.$route.query
        getArticleContent({action: 'markdownContent', tag_id: param['id']}).then(res => {
            this.baseArticleContent = res['mdContent']
            this.title = res['title']
        })
    },
    watch: {
        'baseArticleContent'() {
            this.H_title()
        },
    },
    methods: {
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

        },

        H_title() {
            // marked设置
            const rendererMD = new marked.Renderer();

            // 调整标题内容
            rendererMD.heading = (text, level) => {
                if (level === 2) {
                    this.headlamp.push({title: text.replace(/&#39;/g,"'"), level: 2, child: []})
                } else if (level === 3) {
                    this.headlamp[this.headlamp.length - 1].child.push({title: text.replace(/&#39;/g,"'"), level: 3})
                }
            };

            marked.setOptions({
                renderer: rendererMD
            });

            // 这里的html就是插入到页面的元素文本了
            marked(this.baseArticleContent)
            console.log(this.headlamp)
        },
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

.mu-lu {
    width: 200px;
    margin-top: 10px;
    position: absolute;
    top: calc(10vh);
    right: 5px;
    border-radius: 4px;

    ul {
        padding: 5px;
        list-style-type: none;

        li {
            white-space: nowrap;
            text-overflow: ellipsis;
            overflow: hidden;
            margin-top: 4px;
            margin-bottom: 4px;
            font-size: 16px;

            a {
                color: wheat;
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

.md-previewOnly {
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
    .markdown-body, .md-previewOnly {
        padding: 15px;
    }
}

</style>
