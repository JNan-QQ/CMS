<template>
    <el-tabs type="border-card">
        <el-tab-pane label="轮播图">
            <div v-for="hotNews in hotNewsData">
                <el-input-number v-model="hotNews['news_id']" :min="1" controls-position="right" @change=""/><span>{{hotNews['news_title']}}</span>
            </div>
        </el-tab-pane>
        <el-tab-pane label="校园新闻">Config</el-tab-pane>
        <el-tab-pane label="社会新闻">Role</el-tab-pane>
        <el-tab-pane label="疫情防控">Task</el-tab-pane>
    </el-tabs>
</template>

<script>
export default {
    name: "homepage",
    data(){
        return{
            hotNewsData:[],
        }
    }
}
</script>

<style scoped>

</style>
