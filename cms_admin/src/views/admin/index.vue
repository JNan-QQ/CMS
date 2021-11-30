<template>
    <el-row class="tac">
        <el-col>
            <div style="display: flex;background-color: #545c64;margin-bottom: 1px;">
                <el-image style="width: auto; height: 80px;margin-left: auto" src="./favicon.ico" fit="fit"></el-image>
                <span style="line-height: 80px;margin-left: 5px;margin-right: auto">CMS-ADMIN</span>
            </div>
            <el-menu active-text-color="#ffd04b" background-color="#545c64" class="el-menu-vertical-demo"
                     default-active="2" text-color="#fff">
                <el-sub-menu index="1">
                    <template #title>
                        <user style="width: 30px;height: 30px;margin-right: 10px;margin-top: 10px;margin-bottom: 10px"/>
                        <span>账号管理</span>
                    </template>
                    <el-menu-item index="1-1">item one</el-menu-item>
                    <el-menu-item index="1-2">item one</el-menu-item>

                </el-sub-menu>
                <el-menu-item index="2">
                    <el-icon>
                        <icon-menu/>
                    </el-icon>
                    <span>Navigator Two</span>
                </el-menu-item>
                <el-menu-item index="3" disabled>
                    <el-icon>
                        <document/>
                    </el-icon>
                    <span>Navigator Three</span>
                </el-menu-item>
                <el-menu-item index="4">
                    <el-icon>
                        <setting/>
                    </el-icon>
                    <span>Navigator Four</span>
                </el-menu-item>
            </el-menu>
        </el-col>
    </el-row>
</template>

<script>
import {User} from "@element-plus/icons"
import request from "../../utils/request";
import {ElMessage, ElMessageBox} from "element-plus";

export default {
    name: 'admin',
    data() {
        return {
            userdata: {}
        }
    },
    components: {User},

    mounted() {
        this.before()
    },

    methods: {
        before() {
            const that = this
            request.post('/api/sign/', {action: 'checkLogin'}).then(res => {
                if (res.data['ret'] === 0) {
                    this.userdata = res.data
                    if (res.data['usertype'] !== 1) {
                        ElMessageBox.confirm('你登录的不是管理员账号，无法访问此页面奥！', 'Warning',
                            {
                                confirmButtonText: '登录',
                                cancelButtonText: '取消',
                                type: 'warning',
                            }).then(() => {
                            ElMessage({
                                type: 'success',
                                message: '进入登录界面',
                            })
                            that.$router.push('/login')
                        }).catch(() => {
                            ElMessage({
                                type: 'success',
                                message: '进入首页',
                            })
                            that.$router.push('/')
                        })
                    }
                }
            })
        },

    }

}
</script>

<style lang="less" scoped>
.tac {
    width: 260px;
}

.el-sub-menu {
    min-height: 50px;

    span {
        line-height: 50px;
        margin-left: 5px;
    }
}

</style>
