<template>
    <div class="top">
        <div class="title">
            <div class="md_name">
                <el-icon @click="this.$router.push('/Article');">
                    <d-arrow-left/>
                </el-icon>
                <span class="md-title">{{ title }}</span>
                <div class="author"><span>--&nbsp;&nbsp;{{ author }}</span></div>
            </div>
            <div class="btn-class">
                <el-button @click="downloadMarkdown">下载</el-button>
            </div>
        </div>
    </div>

    <div class="md-view">
        <md-editor v-model="baseArticleContent" previewOnly/>
    </div>

    <el-collapse v-model="activeName" accordion class="mu-lu">
        <el-collapse-item :title="item.title" :name="index+1" :key="index+'fist'" v-for="(item,index) in headlamp"
                          @click="activeFist=index">
            <ul>
                <li><a :href="'#'+item.title">0. 进入模块</a></li>
                <li v-for="(item1,index1) in item.child" :key="index1+'two'">
                    <a :href="'#'+item1.title" @click="changeActiveTwo(index1)" :class="item1.child_class">
                        {{ item1.title }}
                    </a>
                </li>
            </ul>
        </el-collapse-item>
    </el-collapse>

</template>

<script>
import {marked} from "marked"
import {downloadFree, getArticleContent} from "@/api/common";
import {DArrowLeft, AddLocation} from "@element-plus/icons";
import {ElMessageBox} from "element-plus";
import MdEditor from 'md-editor-v3';

export default {
    name: "markdownView",
    data() {
        return {
            baseArticleContent: "",
            title: "",
            author: "",
            headlamp: [],
            activeName: 1,
            activeFist: 0,
            activeTwo: [0, 0]
        }
    },
    components: {DArrowLeft, MdEditor, AddLocation},
    mounted() {
        const param = this.$route.query
        getArticleContent({action: 'markdownContent', tag_id: param['id']}).then(res => {
            this.baseArticleContent = res['mdContent']
            this.title = res['title']
            this.author = res['author']
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

        // 统计章节目录
        H_title() {
            // marked设置
            const rendererMD = new marked.Renderer();

            // 调整标题内容
            rendererMD.heading = (text, level) => {
                if (level === 2) {
                    this.headlamp.push({title: text.replace(/&#39;/g, "'").replace(/<.*?>/g, ''), level: 2, child: []})
                } else if (level === 3) {
                    this.headlamp[this.headlamp.length - 1].child.push({
                        title: text.replace(/&#39;/g, "'").replace(/<.*?>/g, ''),
                        level: 3,
                        child_class: ''
                    })
                }
            };

            marked.setOptions({
                renderer: rendererMD
            });

            // 这里的html就是插入到页面的元素文本了
            marked(this.baseArticleContent)
        },
        changeActiveTwo(index) {
            this.headlamp[this.activeTwo[0]].child[this.activeTwo[1]].child_class = ''
            this.headlamp[this.activeFist].child[index].child_class = 'active'
            this.activeTwo = [this.activeFist, index]
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

            .md-title {
                margin-left: 10px;
            }

            .author {
                margin-left: 5px;
                font-size: 5px;
                height: 26px;
                display: flex;
                align-items: flex-end;
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
    background: #FFFFFF;

    .el-collapse-item {
        margin-left: 5px;
    }

    ul {
        padding: 5px;
        list-style-type: none;

        li {
            white-space: nowrap;
            text-overflow: ellipsis;
            overflow: hidden;
            font-size: 16px;

            a {
                padding: 2px;
                color: #ffffff;
            }

            a.active {
                color: #fa9507;
            }
        }

        li:nth-child(even) {
            background: #e1dede; /*偶数行变色，黄色*/
        }

        li:nth-child(odd) {
            background: rgba(217, 213, 213, 0.99); /*奇数行颜色，红色*/
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
