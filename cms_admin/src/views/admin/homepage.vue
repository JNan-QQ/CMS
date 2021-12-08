<template>
    <el-tabs type="border-card">
        <el-tab-pane label="轮播图" style="display: flex;flex-direction: row;flex-wrap: wrap;">
            <el-row v-for="hotNews in hotNewsData" style="width: 45%;margin: 2%">
                <el-col>新闻id：
                    <el-input-number v-model="hotNews['news']" :min="1" controls-position="right" size="small"
                                     @change=""/>
                </el-col>
                <el-col style="margin-top: 3px;margin-bottom: 3px;">title：{{ hotNews['news__title'] }}</el-col>
                <el-image :src="hotNews.img" style="margin: auto" @click="modifyImg(hotNews['news'])">
                    <template #error>
                        <el-icon size=32>
                            <icon-picture/>
                        </el-icon>
                    </template>
                </el-image>
            </el-row>
        </el-tab-pane>
        <el-tab-pane label="校园新闻">Config</el-tab-pane>
        <el-tab-pane label="社会新闻">Role</el-tab-pane>
        <el-tab-pane label="疫情防控">Task</el-tab-pane>
    </el-tabs>

    <el-dialog v-model="dialogVisible" title="Tips" width="36%" destroy-on-close>
        <el-upload drag action="/api/files" :data="{action:'upload'}" name="files"
                   @on-success="changeImg(response,file,fileList)">
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

export default {
    name: "homepage",
    data() {
        return {
            hotNewsData: [
                {
                    news_id: 20,
                    news_title: '测试用titerc',

                }, {
                    news_id: 20,
                    news_title: '测试用titer',
                    img: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
                }, {
                    news_id: 20,
                    news_title: '测试用titer',
                    img: 'https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg'
                },
            ],
            dialogVisible: false,
        }
    },
    components: {IconPicture: markRaw(IconPicture), UploadFilled: markRaw(UploadFilled)},
    mounted() {
        this.before()
    },
    methods: {
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
        modifyImg(id) {
            this.dialogVisible = true
        },
        changeImg(response,file,fileList){

        }
    },
}
</script>

<style scoped>

</style>
