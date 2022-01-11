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

    </div>
</template>

<script>
import {getContentTags, getSlideTags} from "@/api/common";

export default {
    name: "article",
    data() {
        return {
            isActive: 0,
            tagList: [{id: 1, tag_name: 'Python'}, {id: 2, tag_name: 'Java'}],
            contentTagList: []
        }
    },
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
            }
        })
    },
    methods: {
        getTagContent(i) {
            this.isActive = i;
        },
    },
}
</script>

<style lang="less">
.main-article {
    height: auto;
    background-color: #FFFFFF;
    color: #FFFFFF;
    position: relative;

    .slide-item-table {
        height: 280px;
        background-image: url("../../assets/coursebg.jpg");
        border-top: #FFFFFF solid 1px;

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
    }

    .tag_items {

        text-align: center;
        margin-top: 40px;

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


</style>
