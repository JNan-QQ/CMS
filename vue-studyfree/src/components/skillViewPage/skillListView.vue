<template>
    <div class="skill-list" v-show="!isRead" v-loading="loading_list" element-loading-text="加载中...">
        <el-card v-for="(item,index) in skillList" :key="index" class="skill-item" shadow="hover"
                 body-style="display: flex;justify-content: space-between;" style="margin-top: 5px">
            <div class="skill-item-title">
                <el-avatar :size="28" :src="item['author__aviator']"/>
                <span @click="toRead(item.id)">{{ item.title }}</span>
                <div @click="changeCollection(item.id,index)">
                    <span title="收藏" class="icon collection" v-if="!item['isCollect']"><el-icon color="#409EFC"><Star/></el-icon></span>
                    <span title="取消" class="icon collection" v-else><el-icon :size="18" color="#f39404"><StarFilled/></el-icon></span>
                </div>
            </div>
            <div class="skill-item-opt">
                <div class="icon">
                    <i class="el-ali-browse"></i>
                    <el-icon style="margin-top: 5px" color="#919090">
                        <connection/>
                    </el-icon>
                </div>
                <div class="disc">
                    <span class="clicks">{{ item['clicks'] }}</span>
                    <span style="margin-top: 5px" class="author">{{ item['author__realName'] }}</span>
                </div>
            </div>
        </el-card>
    </div>
    <div class="skill-content" v-show="isRead">
        <el-card class="box-card" v-loading="loading_content" element-loading-text="加载中...">
            <template #header>
                <div class="card-header">
                    <span @click="isRead=false">{{ readInfo.title }}</span>
                    <el-rate v-model="readInfo.rate" allow-half :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
                             @change="changeRate"/>
                </div>
            </template>
            <md-editor-v3 v-model="readInfo.content" previewOnly v-highlight/>
        </el-card>
    </div>
</template>

<script>
import {Star, StarFilled, Connection} from "@element-plus/icons";
import {skillApi} from "@/api/front";

export default {
    name: "skillListView",
    components: {StarFilled, Star, Connection},
    props: ['mode'],
    data() {
        return {
            skillList: [],
            isRead: false,
            readInfo: {},
            modeInfo: ['hot', 'all','my-collection'],
            loading_list: false,
            loading_content: false
        }
    },
    mounted() {
        this.getSkillData()

    },
    watch: {
        'mode'() {
            this.isRead = false
            this.getSkillData()
        }
    },
    methods: {
        // 获取技巧列表
        getSkillData() {
            this.loading_list = true
            skillApi({action: 'list', mode: this.modeInfo[parseInt(this.mode) - 1]}).then(res => {
                if (res) {
                    this.skillList = res['retlist']
                }
                this.loading_list = false
            })
        },
        // 收藏列表
        changeCollection(id, index) {
            this.skillList[index].isCollect = !this.skillList[index].isCollect
            skillApi({action:'collection','skill_id': id})
        },

        // 点击阅读
        toRead(id) {
            this.isRead = true
            this.loading_content = true
            skillApi({action: 'getContent', 'skill_id': id}).then(res => {
                if (res) {
                    this.readInfo = res['retlist']
                }
                this.loading_content = false
            })

        },

        // 改变评分
        changeRate(val) {
            this.readInfo.rate = val
            skillApi({action: 'modify_rate', 'skill_id': this.readInfo.id, rate: val})
        },
    }
}
</script>

<style scoped lang="less">
.skill-list {
    padding: 10px;
    position: relative;

    .skill-item {
        height: 80px;

        .skill-item-title {
            display: flex;
            align-items: center;

            span {
                margin-left: 10px;
            }
        }

        .skill-item-opt {
            display: flex;
            justify-content: space-between;
            align-items: center;

            .icon {
                display: flex;
                flex-direction: column;
                align-items: center;
                margin-right: 5px;

                .el-ali-browse {
                    font-size: 22px;
                    color: #1E9FFF;
                }
            }

            .disc {
                display: flex;
                flex-direction: column;
                align-items: flex-end;

                .clicks {
                    color: #1E9FFF;
                }

                .author {
                    color: #919090;
                }
            }
        }


    }
}

.skill-content {
    padding: 10px;
    position: relative;

    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
}

</style>