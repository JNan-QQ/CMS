<template>
    <div class="main-article">
        <div class="slide-item-table">
            <div class="text-center"><h2 class="slider_title">StudyFree，学习笔记好帮手！</h2>
                <p class="product-desctext">开开心心学习，快快乐乐生活</p>
            </div>
            <div class="tag_items">
                <ul>
                    <li v-for="(item,index) in tagList" :class="{active: isActive === index}"
                        @click="getTagContent(index)">{{ item.tag_name }}
                    </li>
                </ul>
            </div>
        </div>
        <div class="courseListBox">
            <div class="course_stage_item" v-for="(tag2,index) in contentTagList">
                <h2>
                    <span class="cro_icon1">{{ index + 1 }}</span>
                    <span>第{{ chineseIndex[index] }}阶段：{{ tag2.tag_name }}</span>
                </h2>
                <div class="path-course-r">
                    <div class="content" v-for="tag3 in tag2.content" @click="toMarkdown(tag3.id)">
                        <el-image fit="fill" :src="`api/static/` + tag3.images"></el-image>
                        <div>
                            <h3>{{ tag3.tag_name }}</h3>
                            <p>这是一个描述</p>
                            <div class="views">
                                <el-icon>
                                    <pointer/>
                                </el-icon>
                                <span>23354</span></div>
                        </div>
                    </div>
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
import {getContentTags, getSlideTags} from "@/api/common";
import {Pointer} from '@element-plus/icons';

export default {
    name: "articleView",
    data() {
        return {
            isActive: 0,
            tagList: [{id: 0, tag_name: ''}],
            contentTagList: [{
                id: 0,
                tag_name: '',
                content: [{id: 1, tag_name: '', images: 'images/python-default.png'}]
            }],
            chineseIndex: ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
        }
    },
    components: {Pointer},
    watch: {
        isActive() {
            const tag_id = this.tagList[this.isActive].id
            getContentTags({action: 'contentTags', 'tag_id': tag_id}).then(res => {
                if (res) {
                    this.contentTagList = res['retlist']
                }
            })
        }
    },
    mounted() {
        getSlideTags().then(res => {
            if (res) {
                this.tagList = res['retlist']
                getContentTags({action: 'contentTags', 'tag_id': this.tagList[this.isActive].id}).then(res => {
                    if (res) {
                        this.contentTagList = res['retlist']
                    }
                })
            }
        })


    },
    methods: {
        getTagContent(i) {
            this.isActive = i;
        },
        toMarkdown(id) {
            // this.$router.push('/?id=' + id)
            let routeUrl = this.$router.resolve({
                path: '/md',
                query: {id: id}
            })
            window.open(routeUrl.href, '_blank')
        }
    },
}
</script>

<style lang="less" scoped>
.main-article {
    //background-color: #e0dddd;
    position: relative;
    height: calc(100vh - 140px);
    overflow-y: auto;

    .slide-item-table {
        height: 280px;
        background-image: url("../../assets/coursebg.jpg");
        border-top: #FFFFFF solid 1px;
        border-bottom: #FFFFFF solid 1px;
        color: #FFFFFF;

        .text-center {
            text-align: center;
            margin-top: 110px;
            margin-bottom: 10px;

            .slider_title {
                font: 36px 'Arial Rounded MT Bold';
            }

            .product-desctext {
                font-size: 14px;
                margin-top: 10px;
            }
        }

        .tag_items {

            text-align: center;
            margin-top: 40px;
            color: #FFFFFF;

            ul {
                list-style: none;

                li {
                    display: inline-block;
                    margin-right: 10px;
                    margin-left: 10px;
                    font: 14px Helvetica Neue;
                    color: #FFFFFF;
                    border-radius: 4px;
                    border: 1px solid var(--el-border-color-base);
                    padding: 5px 10px;
                    width: 65px;


                }

                li.active {
                    background-color: aquamarine;
                    color: #fa9507;
                }

                li:hover {
                    background-color: aquamarine;
                }

                li:active {
                    color: #04121c;
                }
            }

        }
    }

    .courseListBox {
        margin-top: 20px;
        border-left: 1px solid #eaeaea;
        margin-right: auto;
        margin-left: auto;
        padding-right: 15px;
        padding-left: 15px;
        width: 100%;
        min-height: 310px;

        .course_stage_item {
            position: relative;
            margin-bottom: 10px;
            margin-left: 12px;
            padding-top: 4px;

            h2 {
                color: #1E9FFF;
                font-size: 22px;
                padding-top: 0;
                font-weight: bold;

                .cro_icon1 {
                    width: 30px;
                    height: 30px;
                    background-color: #1E9FFF;
                    position: absolute;
                    left: -42px;
                    top: 0;
                    border-radius: 50%;
                    z-index: 3;
                    text-align: center;
                    line-height: 30px;
                    font-size: 18px;
                    color: #fff;
                }
            }

            .path-course-r {
                display: flex;
                flex-wrap: wrap;
                margin-top: 15px;

                .content {
                    width: 20%;
                    height: 250px;
                    text-align: center;
                    padding: 15px;
                    background-color: #FFFFFF;
                    margin: 1.5%;
                    border-radius: 4px;

                    .el-image {
                        height: 66.66%;
                        border-radius: 4px;
                    }

                    div {
                        height: 33.33%;

                        h3 {
                            font-size: 16px;
                            font-weight: 600;
                            line-height: 22px;
                            color: #233d63;
                            text-align: left;
                        }

                        p {
                            line-height: 20px;
                            margin-bottom: 10px;
                            font-size: 13px;
                            color: #999;
                            display: -webkit-box;
                            display: flex;
                            -webkit-box-pack: justify;
                            justify-content: space-between;
                        }

                        .views {
                            text-align: right;
                            margin-top: 5px;

                            .el-icon {
                                margin-right: 2px;
                            }
                        }

                    }
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

</style>
