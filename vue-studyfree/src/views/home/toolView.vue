<template>
    <div class="tool-view">
        <div class="driver-box ss">
            <div class="headline">
                <strong>WebDriver
                    <span>浏览器类型：</span>{{ browser.type }}
                    <span>浏览器版本：</span>{{ browser.version }}
                    <span v-if="browser.bankel">浏览器内核：</span>{{ browser.bankel }}
                </strong>
            </div>
            <div class="tool-box" style="display: block">
                <ul>
                    <li v-for="item in tools_dict['WebDriver']">
                        <a :title="item.name" :href="item['jump_url']" target="_blank">
                            <el-image :src="item['icon_url']" fit="fill"
                                      class="icon"/>
                            <p>{{ item.name }}</p>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="web-box ss">
            <div class="headline">
                <strong>工具网址</strong>
            </div>
            <div class="tool-box" style="display: block">
                <ul>
                    <li v-for="item in tools_dict['UrlCollection']">
                        <a :href="item['jump_url']" target="_blank">
                            <el-image :src="item['icon_url']" fit="fill" class="icon"/>
                            <span>{{ item.name }}</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
        <div class="other-box ss web-box">
            <div class="headline">
                <strong>自定义</strong>
                <el-input v-model="localFileName" placeholder="输入json文件路径" size="small" class="file">
                    <template #append>
                        <el-button :icon="Refresh" size="small" @click="readLocalFile"></el-button>
                    </template>
                </el-input>
            </div>
            <div class="tool-box" style="display: block">
                <ul>
                    <li v-for="item in otherList">
                        <a :href="item['jump_url']" target="_blank">
                            <el-image :src="item['icon_url']" fit="fill" class="icon"/>
                            <span>{{ item.name }}</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<script>
import {WebConfigApi} from "@/api/admin";
import {Refresh} from "@element-plus/icons";
import {markRaw} from "vue";
import request from "@/api/request";
import axios from "axios";

export default {
    name: "toolsView",
    data() {
        return {
            browser: {},
            tools_dict: {},
            otherList: [],
            localFileName: '',
            Refresh: markRaw(Refresh)
        }
    },
    components: {},
    mounted() {
        this.getBrowser()
        this.getTools()
        this.readLocalFile()
    },
    watch: {
    },
    methods: {
        getBrowser() {
            const UserAgent = navigator.userAgent.toLowerCase()
            const browserInfo = {}
            if (UserAgent.indexOf('edg/') > -1) {
                browserInfo.type = 'Edge'
                browserInfo.bankel = UserAgent.match(/chrome\/[\d.]+/)[0]
                browserInfo.version = UserAgent.match(/edg\/([\d.]+)/)[1]
            } else if (UserAgent.indexOf('chrome/') > -1) {
                browserInfo.type = 'Chrome'
                browserInfo.version = UserAgent.match(/chrome\/([\d.]+)/)[1]
            } else if (UserAgent.indexOf('firefox/') > -1) {
                browserInfo.type = 'FireFox'
                browserInfo.version = UserAgent.match(/firefox\/([\d.]+)/)[1]
            } else if (UserAgent.indexOf('Opera')) {
                browserInfo.type = 'Opera'
                browserInfo.version = UserAgent.match(/opera\/([\d.]+)/)[1];
            }
            this.browser = browserInfo
        },
        getTools() {
            WebConfigApi({action: 'admin_list_webConfig', title: 'tools'}).then(res => {
                this.tools_dict = eval('(' + res['retlist'][0]['config'] + ')')
            })
        },
        readLocalFile() {
            const localUrl = localStorage.getItem('localUrl')
            if (localUrl && this.localFileName === '') {
                this.localFileName = localUrl
            } else {
                localStorage.setItem('localUrl', this.localFileName)
            }
            if (this.localFileName !== '') {
                axios.get(this.localFileName).then((res) => {
                    console.log(res)
                })
            }
        },
    }
}
</script>

<style scoped lang="less">
.tool-view {
    max-width: 1100px;
    margin: auto;

    .ss {
        margin-bottom: 14px;
        border-radius: 4px;
        background: #fff;
        margin-top: 20px;

        .headline {
            padding: 15px 20px 0;

            strong {
                display: inline-block;
                position: relative;
                margin-left: -20px;
                padding-left: 20px;
                vertical-align: top;
                font-weight: 500;
            }

            strong:before {
                position: absolute;
                top: 50%;
                left: 0;
                width: 6px;
                height: 16px;
                margin-top: -8px;
                background: #2777f8;
                border-radius: 0 2px 2px 0;
                content: "";
            }
        }
    }

    .driver-box {
        .headline {
            strong {
                span {
                    font-size: 10px;
                    font-weight: 100;
                    color: #545c64;
                    margin-left: 20px;
                }
            }
        }

        .tool-box {
            ul {
                padding: 5px 10px;
                list-style: none;
                display: flex;

                li {
                    position: relative;
                    width: 110px;
                    margin: 0 10px;
                    padding: 15px 7px 7px;
                    border-radius: 10px;

                    a {
                        display: block;
                        color: #666;
                        font-size: 12px;
                        text-align: center;
                        transition: color 0.2s;

                        .icon {
                            position: relative;
                            border: 1px dashed #eee;
                            background: #fafafa;
                            box-sizing: border-box;
                            transition: border 0.2s, background 0.2s;
                            display: block;
                            width: 60px;
                            height: 60px;
                            margin: 0 auto 5px;
                            border-radius: 8px;
                            padding: 8px;
                        }
                    }
                }
            }
        }
    }

    .web-box {
        .tool-box {
            ul {
                padding: 10px 15px 12px 15px;
                justify-content: flex-start;
                display: flex;
                flex-wrap: wrap;
                list-style: none;

                li {
                    margin: 7px 5px;
                    width: calc(100% / 8 - 10px);

                    a {
                        display: inline-flex;
                        max-width: 100%;
                        align-items: center;
                        transition: color 0.2s;
                        text-decoration: none;
                        color: #34495e;
                        outline: none;
                        position: relative;

                        .icon {
                            width: 16px;
                            height: 16px;
                        }

                        span {
                            font-size: 13px;
                            margin-left: 5px;
                        }
                    }
                }
            }
        }
    }

    .other-box {
        .headline {
            display: flex;
            justify-content: space-between;

            .file {
                position: relative;
                width: 200px;
            }
        }
    }
}

</style>
