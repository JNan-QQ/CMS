<template>
    <el-tabs type="border-card">
        <el-tab-pane>
            <template #label>
                <span style="text-align: center">
                    <el-icon><picture-filled/></el-icon>
                    图片
                </span>
            </template>
            Route
        </el-tab-pane>
        <el-tab-pane label="Config">Config</el-tab-pane>
        <el-tab-pane label="Role">Role</el-tab-pane>
        <el-tab-pane label="Task">Task</el-tab-pane>
    </el-tabs>
</template>

<script>
import {PictureFilled} from "@element-plus/icons"
import {markRaw} from "vue";

export default {
    name: "index",
    data() {
        return {}
    },
    components:{PictureFilled:markRaw(PictureFilled)},
}
</script>

<style lang="less">
.icon{
    text-align: center;
}

</style>
