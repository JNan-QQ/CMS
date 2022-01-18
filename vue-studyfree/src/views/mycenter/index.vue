<template>
    <div class="my-center">
        <div style="display: flex;justify-content: space-between;">
            <div style="display: flex; flex-direction: column; align-items: center;">
                <el-image style="width: 200px; height: 200px" :src="userdata.aviator" fit="fill"></el-image>
                <el-button>修改头像</el-button>
            </div>
            <div style="">123</div>
        </div>
        <div>

        </div>
    </div>
</template>

<script>
export default {
    name: "index",
    data() {
        return {
            userdata: this.$store.state.userdata,
        }
    }
}
</script>

<style scoped lang="less">
.my-center {
    width: 960px;
    min-height: calc(80vh);
    margin: calc(5vh) auto;
    border-radius: 15px;
    padding: 40px 40px;
    background-color: #eeeeee;
    position: relative;
    box-shadow: #e0dddd ;
}

</style>
