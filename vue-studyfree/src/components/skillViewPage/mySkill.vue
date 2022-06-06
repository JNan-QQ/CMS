<template>
    <div class="skill-edit-view">
        <div class="btn-group">
            <div class="color">
                <div style="background-color: #0bee8c;">审核通过</div>
                <div style="background-color: #5e3df3;">待审核</div>
                <div style="background-color: #ec5807;">暂存</div>
                <div style="background-color: rgba(84,81,81,0.99);">封禁</div>
            </div>
            <el-button-group>
                <el-button v-if="!isRead&&!isEdit" @click="addSkill">新增</el-button>
                <el-button v-if="isRead&&!isEdit" @click="isEdit=true">编辑</el-button>
                <el-button v-if="isRead&&!isEdit" @click="deleteSkill" :loading="deleteLoadBtn">删除</el-button>
                <el-button v-if="isEdit" @click="saveSkill('temporary')" :loading="saveLoadBtn">暂存</el-button>
                <el-button v-if="isEdit" @click="saveSkill('review')" :loading="saveLoadBtn">提交审核</el-button>
            </el-button-group>
        </div>
        <div class="skill-list" v-show="!isRead">
            <el-card v-for="(item,index) in skillList" :key="index" class="skill-item" shadow="hover"
                     body-style="display: flex;justify-content: space-between;"
                     :style="{marginTop: '5px',backgroundColor:color_status[item.status]}"
                     @click="toRead(item.id)"
            >
                <div class="skill-item-title">
                    <span><strong>{{ item.title }}</strong></span>
                </div>
                <div class="skill-item-opt">
                    <span>点击量：{{ item['clicks'] }}</span>
                    <span style="margin-left: 10px;margin-right: 10px">收藏量：{{ item['collection'] }}</span>
                    <span>评分：{{ item['rate'] }}</span>
                </div>
            </el-card>
        </div>
        <div class="skill-content" v-show="isRead">
            <el-card class="box-card">
                <template #header>
                    <div class="card-header">
                        <span @click="isRead=false" v-if="!isEdit">{{ readInfo.title }}</span>
                        <el-input v-else v-model="readInfo.title" placeholder="请输入标题"></el-input>
                    </div>
                </template>
                <md-editor-v3 v-if="isEdit" v-model="readInfo.content" v-highlight/>
                <md-editor-v3 v-model="readInfo.content" previewOnly v-else v-highlight/>
            </el-card>
        </div>
    </div>
</template>

<script>
import {skillApi} from "@/api/front";

export default {
    name: "mySkill",
    data() {
        return {
            isRead: false,
            isEdit: false,
            readInfo: {},
            skillList: [],
            color_status: ['rgba(84,81,81,0.99)', '#0bee8c', '#ec5807', '#5e3df3'],
            deleteLoadBtn: false,
            saveLoadBtn: false
        }
    },
    components: {},
    mounted() {
        this.getSkillData()
    },
    methods: {
        // 获取技巧列表
        getSkillData() {
            this.loading_list = true
            skillApi({action: 'list', mode: 'myself'}).then(res => {
                if (res) {
                    this.skillList = res['retlist']
                }
                this.loading_list = false
            })
        },

        // 点击阅读
        toRead(id) {
            this.isRead = true
            skillApi({action: 'getContent', 'skill_id': id}).then(res => {
                if (res) {
                    this.readInfo = res['retlist']
                }
            })

        },

        // 新增技巧
        addSkill() {
            this.readInfo = {title: '', content: ''}
            this.isRead = true
            this.isEdit = true
        },

        /*删除技巧*/
        deleteSkill() {
            this.isRead = false
            this.deleteLoadBtn = true
            skillApi({action: 'deleteSkill', skill_id: this.readInfo.id}).then(res => {
                this.deleteLoadBtn = false
                this.readInfo = {}
                this.getSkillData()
            })
        },

        // 保存技巧
        saveSkill(mode) {
            this.saveLoadBtn = true
            let data = this.readInfo
            data.action = 'saveSkill'
            data.mode = mode
            skillApi(data).then(res => {
                this.isEdit = false
                this.saveLoadBtn = false
                this.getSkillData()
            })
        }


    }
}
</script>

<style scoped lang="less">
.skill-edit-view {
    padding: 10px;
    position: relative;

    .btn-group {
        display: flex;
        justify-content: space-between;
        align-items: center;

        .color {
            display: flex;

            div {
                padding: 2px;
                border-radius: 3px;
                margin-left: 5px;
            }
        }
    }
}
</style>