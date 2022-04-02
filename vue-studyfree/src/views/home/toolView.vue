<template>
    <div class="tool-view">

        <div class="b_searchboxForm">
            <input class="searchBox" maxlength="100" v-model="search_str"
                   @keydown.enter="search_b" autofocus="autofocus">
            <el-icon size="18" color="#7fb8e4" v-if="search_str!==''" @click="search_str=''">
                <close-bold/>
            </el-icon>
            <el-icon size="24" color="#7fb8e4" @click="search_b">
                <search/>
            </el-icon>
        </div>

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
                <el-button-group>
                    <el-button type="primary" :icon="Edit" size="small" @click="editBtn=true"></el-button>
                    <el-button type="primary" :icon="Plus" size="small" @click="dialogVisible=true"></el-button>
                    <el-button type="primary" :icon="Select" size="small" v-if="saveBtn" @click="save"></el-button>
                    <el-button type="primary" :icon="CloseBold" size="small" v-if="saveBtn" @click="getWebUrl">
                    </el-button>
                </el-button-group>
            </div>
            <div class="tool-box" style="display: block">
                <ul>
                    <li v-for="(item,index) in otherList">
                        <a :href="item['jump_url']" target="_blank">
                            <el-image :src="item['icon_url']" fit="fill" class="icon"/>
                            <span>{{ item.title }}</span>
                        </a>
                        <el-icon class="rightTopIcon" v-if="editBtn" @click="localDelete(index)">
                            <close-bold/>
                        </el-icon>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <el-dialog v-model="dialogVisible" title="添加工具网址" width="30%" @close="closeDialog">
        <el-form ref="formRef" :model="newWebTool" label-width="120px">
            <el-form-item label="标签名称">
                <el-input v-model="newWebTool.title"></el-input>
            </el-form-item>
            <el-form-item label="标签链接网址">
                <el-input v-model="newWebTool.jump_url" @change="changeIcon"></el-input>
            </el-form-item>
            <el-form-item label="标签图标">
                <div style="display: flex;align-items: center;">
                    <el-input v-model="newWebTool.icon_url" :disabled="icon_mode"></el-input>
                    <span style="min-width: 30px;margin: 3px">默认</span>
                    <el-switch
                        v-model="icon_mode"
                        inline-prompt
                        active-color="#13ce66"
                        inactive-color="#ff4949"
                        active-text="Y"
                        inactive-text="N"
                        @change="changeIcon"
                    />
                </div>
            </el-form-item>
            <el-form-item label="图标预览">
                <el-image fit="fill" :src="newWebTool.icon_url"></el-image>
            </el-form-item>
        </el-form>
        <template #footer>
            <span class="dialog-footer">
                <el-button @click="saveLocal">确认</el-button>
                <el-button @click="dialogVisible=false">取消</el-button>
            </span>
        </template>
    </el-dialog>
</template>

<script>
import {WebConfigApi} from "@/api/admin";
import {Edit, Plus, Select, CloseBold, Search} from "@element-plus/icons";
import {markRaw} from "vue";
import {ElMessage} from "element-plus";
import {CommonApi} from "@/api/common";

const {UserConfigApi} = require("../../api/pay");

export default {
    name: "toolsView",
    data() {
        return {
            browser: {},
            tools_dict: {},
            otherList: [],
            Edit: markRaw(Edit),
            Plus: markRaw(Plus),
            Select: markRaw(Select),
            CloseBold: markRaw(CloseBold),
            dialogVisible: false,
            newWebTool: {title: '', jump_url: '', icon_url: ''},
            icon_mode: true,
            btnLoading: false,
            saveBtn: false,
            editBtn: false,
            search_str: ''
        }
    },
    components: {CloseBold, Search},
    mounted() {
        this.getBrowser()
        this.getTools()
        this.getWebUrl()
    },
    watch: {},
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
            CommonApi({action: 'list_webConfig', title: 'tools'}).then(res => {
                this.tools_dict = eval('(' + res['retlist'][0]['config'] + ')')
            })
        },
        getWebUrl() {
            UserConfigApi({action: 'listWebUrl'}).then((res) => {
                if (res) {
                    if (res['web_url'].hasOwnProperty('web_url')) {
                        this.otherList = res['web_url']['web_url']
                    }
                    this.saveBtn = false
                    this.editBtn = false
                }
            })
        },
        changeIcon() {
            if (this.icon_mode) {
                let icon = ''
                if (this.newWebTool.jump_url.endsWith("/")) {
                    icon = 'favicon.ico'
                } else {
                    icon = '/favicon.ico'
                }
                this.newWebTool.icon_url = this.newWebTool.jump_url + icon
            }
        },
        saveLocal() {
            this.otherList.push(this.newWebTool)
            this.dialogVisible = false
            this.saveBtn = true
        },
        localDelete(index) {
            console.log(index)
            this.otherList.splice(index, 1)
            this.saveBtn = true
        },
        save() {
            const ss = {'web_url': this.otherList}
            this.btnLoading = true
            UserConfigApi({action: 'modify', 'web_url': ss}).then(res => {
                if (res) {
                    this.closeDialog()
                    this.getWebUrl()
                    this.dialogVisible = false
                    this.saveBtn = false
                    this.editBtn = false
                    ElMessage.success(res['msg'])
                }
                this.btnLoading = false
            })
        },
        closeDialog() {
            this.newWebTool = {title: '', jump_url: '', icon_url: ''}
            this.icon_mode = true
        },
        search_b(){
            const url = 'https://cn.bing.com/search?q=' + this.search_str
            window.open(url)
        }
    }
}
</script>

<style scoped lang="less">
.tool-view {
    max-width: 1100px;
    margin: auto;

    .b_searchboxForm {
        width: 650px;
        height: 48px;
        border-radius: 24px;
        position: relative;
        font: 18px/normal 'Microsoft YaHei', Arial, Helvetica, Sans-Serif;
        box-shadow: 0 0 0 1px #0000000d, 0 2px 4px 1px #0000000d;
        border-left: 1px solid transparent;
        border-right: none;
        border-top: 1px solid transparent;
        border-bottom: 1px solid transparent;
        background-color: #fff;
        margin: 60px auto;
        display: flex;
        align-items: center;
        justify-content: space-between;

        .searchBox {
            width: 535px;
            border-radius: 24px;
            -webkit-appearance: none;
            font-size: 16px;
            margin: 1px 0 1px 1px;
            padding: 0 10px 0 19px;
            border: 0;
            max-height: none;
            outline: none;
            box-sizing: border-box;
            height: 44px;
            vertical-align: top;
            background-color: transparent;
        }

        .el-icon {
            margin-right: 20px;
            cursor: pointer;
        }
    }

    .ss {
        margin-bottom: 14px;
        border-radius: 4px;
        background: #fff;
        margin-top: 20px;
        position: relative;

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
        }

        .tool-box {
            .rightTopIcon {
                width: 10px;
                top: -9px;
                right: -6px;
                position: relative;
            }
        }
    }
}

</style>
