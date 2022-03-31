<template>
    <div class="content">
        <div v-for="(item,index) in messageList" class="message-item" :class="{read:item['isRead']}"
             @click="getOneMessage(index)">
            <i class="bgd-left" v-if="item['isRead']">.</i>
            <el-icon size="22" class="message-icon">
                <bell v-if="item['message_type']===1"/>
                <timer v-if="item['message_type']===2"/>
                <shopping-cart v-if="item['message_type']===3"/>
                <present v-if="item['message_type']===4"/>
            </el-icon>
            <div class="message">
                <span class="title">{{ item.title }}</span>
                <span class="time">{{ item['creat_time'].split('T')[0] }}</span>
            </div>
        </div>
    </div>
    <div style="text-align: center">
        <el-pagination layout="prev, pager, next" :current-page.sync="current_page" :page-size="page_size"
                       :total="total" @current-change="handleCurrentChange"/>
    </div>

    <el-dialog v-model="dialogVisible" :title="message.title" width="30%" center destroy-on-close :draggable="true">
        <div v-html="message.content"></div>
    </el-dialog>

</template>

<script>
import {MessageApi} from "@/api/common";
import {Bell, ShoppingCart, Timer, Present} from "@element-plus/icons";

export default {
    name: "message",
    data() {
        return {
            messageList: [],
            total: 0,
            page_size: 10,
            current_page: 1,
            dialogVisible: false,
            message: {title: '', content: ''},
        }
    },
    components: {Bell, ShoppingCart, Timer, Present},
    mounted() {
        this.getMessageApi()
    },
    watch: {
        'current_page'() {
            this.getMessageApi()
        }
    },
    methods: {
        // 通知列表
        getMessageApi() {
            MessageApi({action: 'list', page_num: this.current_page, page_size: this.page_size}).then(res => {
                if (res) {
                    this.messageList = res['retlist']
                    this.total = res['total']
                }
            })
        },
        // 翻页
        handleCurrentChange: function (currentPage) {
            this.current_page = currentPage
        },
        // 获取对应通知内容
        getOneMessage(index) {
            this.message.title = this.messageList[index].title
            this.message.content = this.messageList[index].content
            this.dialogVisible = true
            this.messageList[index].isRead = false
            MessageApi({action: 'getOneMessage',message_id:this.messageList[index].id})
        }
    }
}
</script>

<style scoped lang="less">
.content {
    height: 600px;
}

.message-item {
    height: 50px;
    padding: 3px;
    display: flex;
    align-items: center;
    color: #919090;
    position: relative;

    .message-icon {
        margin-left: 10px;
        box-shadow: -6px 3px 4px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        border-radius: 5px 0 0 5px;
        border-right: #cce6ff solid 1px;
        padding: 8px;
    }

    .message {
        margin-right: 10px;
        width: 100%;
        box-shadow: 2px 5px 4px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        border-radius: 0 5px 5px 0;
        padding: 8px;
        display: flex;
        justify-content: space-between;

        .time {
            margin-right: 10px;
        }
    }


    .bgd-left {
        position: absolute;
        right: 8px;
        top: 8px;
        transform: scale(0.82);
        font-size: 12px !important;
        border: 1px solid #eee;
        border-radius: 10px;
        background: red;
        color: #fff;
        padding: 0 6px;
        text-align: center;
        font-style: initial;
    }

}

.message-item:hover {
    background-color: #dbfada;
}

.read {
    color: #fc4c00;
}

</style>