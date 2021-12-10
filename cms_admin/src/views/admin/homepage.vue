<template>
    <el-tabs type="border-card">
        <el-tab-pane label="轮播图">

            <el-button-group>
                <el-button type="success" @click="addHomeImg">添加</el-button>
            </el-button-group>

            <div style="display: flex;flex-direction: row;flex-wrap: wrap;">
                <div v-for="hotNews in hotNewsData"
                     style="width: 45%;margin: 2%;border: 2px dashed var(--el-border-color-base);">
                    <span>新闻id：
                        <el-input-number v-model="hotNews['news']" :min="1" controls-position="right" size="small"
                                         @change="modifyNews(hotNews['news'],hotNews.id)"/>&nbsp;&nbsp;{{
                            hotNews['news__title']
                        }}
                    </span>
                    <div style="height: 350px;margin-top: 10px">
                        <el-image :src="'/api'+hotNews.img" style="margin: 2px;height: 340px;width:auto">
                            <template #error>
                                <el-icon size=32>
                                    <icon-picture/>
                                </el-icon>
                            </template>
                        </el-image>
                    </div>
                    <div style="float: right">
                        <el-button-group>
                            <el-button type="warning" @click="modifyImg(hotNews.id,hotNews.img)">修改图片</el-button>
                            <el-button type="danger" @click="deleteHomeImg(hotNews.id)">删除</el-button>
                        </el-button-group>
                    </div>
                </div>
            </div>
        </el-tab-pane>
        <el-tab-pane label="校园新闻">Config</el-tab-pane>
        <el-tab-pane label="社会新闻">Role</el-tab-pane>
        <el-tab-pane label="疫情防控">Task</el-tab-pane>
    </el-tabs>

    <el-dialog v-model="dialogVisible" title="上传图片" width="30%" destroy-on-close>
        <el-upload drag action="/api/files" :data="{action:'upload'}" name="files" list-type="picture" :multiple="false"
                   style="text-align: center;" :on-success="changeImg">
            <el-icon class="el-icon--upload">
                <upload-filled/>
            </el-icon>
            <div class="el-upload__text">
                Drop file here or <em>click to upload</em>
            </div>
            <template #tip>
                <div class="el-upload__tip">
                    jpg/png files with a size less than 500kb
                </div>
            </template>
        </el-upload>
    </el-dialog>
</template>

<script>
import {Picture as IconPicture, UploadFilled} from '@element-plus/icons'
import {markRaw} from "vue"
import request from "../../utils/request";
import {ElMessage} from "element-plus";

export default {
    name: "homepage",
    data() {
        return {
            hotNewsData: [],
            dialogVisible: false,
            modifyID: 0,
            baseImg: '',
        }
    },
    components: {IconPicture: markRaw(IconPicture), UploadFilled: markRaw(UploadFilled)},
    mounted() {
        this.before()
    },
    methods: {
        // 请求列表函数
        before() {
            const that = this
            request.post('/api/notice/news', {
                action: 'pageImg'
            }).then(res => {
                const data = res.data
                if (data['ret'] === 0) {
                    that.hotNewsData = data['retlist']
                }
            })
        },

        // 显示dialog窗口
        modifyImg(id, img) {
            this.dialogVisible = true
            this.modifyID = id
            this.baseImg = img

        },

        // 改变上传图片
        changeImg(response, file, fileList) {
            const that = this
            // 上传图片到服务器，成功后写入数据库
            request.post('/api/notice/news', {
                action: 'modifyImg',
                id: this.modifyID,
                img: response['file_url'],
            }).then(res => {
                // 写入成功后删除旧图片
                if (res.data['ret'] === 0) {
                    if (that.baseImg !== '') {
                        request.get('/api/files?action=delete&files_path=' + that.baseImg)
                    }
                    that.dialogVisible = false
                    that.before()
                } else {
                }
            })
        },

        // 改变新闻id
        modifyNews(news_id, id) {
            const that = this
            request.post('/api/notice/news', {
                action: 'modifyImg',
                id: id,
                news_id: news_id,
            }).then(res => {
                if (res.data['ret'] === 0) {
                    that.before()
                } else {
                    ElMessage({message: `ID:${news_id} 新闻不存在`, type: 'warning',})
                }
            })

        },

        // 删除对应轮播图
        deleteHomeImg(id) {
            const that = this
            request.post('/api/notice/news', {
                action: 'deleteImg',
                id: id,
            }).then(res => {
                that.before()
            })
        },

        // 添加一个空白新闻
        addHomeImg() {
            const that = this
            request.post('/api/notice/news', {
                action: 'addImg',
            }).then(res => {
                that.before()
            })
        },
    },
}
</script>

<style scoped>

</style>
