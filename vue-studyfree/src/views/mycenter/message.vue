<template>
    <div class="content">
        <div v-for="(item,index) in messageList">
            <span>{{ index + 1 }}</span>
            <span>{{ item.title }}</span>
        </div>
    </div>
</template>

<script>
import {MessageApi} from "@/api/common";

export default {
    name: "message",
    data() {
        return {
            messageList: []
        }
    },
    mounted() {
        this.getMessageApi()
    },
    methods: {
        // 通知列表
        getMessageApi() {
            MessageApi({action: 'list'}).then(res => {
                if (res) {
                    this.messageList = res['retlist']
                }
            })
        },
    }
}
</script>

<style scoped>

</style>