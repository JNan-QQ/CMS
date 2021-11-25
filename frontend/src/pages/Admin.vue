<template>
    <div class="container">
        <!--头部-->
        <div class="top">
            <span>头部</span>
        </div>
        <!--内容-->
        <div class="content">
            <!--左侧导航栏-->
            <div class="items_left">
                <ul>
                    <li @click="ViewContent('account')"><a :class="{active:isActive[0]}">账号管理</a></li>
                    <li @click="ViewContent('news')"><a :class="{active:isActive[1]}">新闻管理</a></li>
                    <li @click="ViewContent('notices')"><a :class="{active:isActive[2]}">通知管理</a></li>
                    <li><a>其他（待添加）</a></li>
                </ul>
            </div>
            <!--内容展示-->
            <div class="tables_right">
                <account_table v-if="mode==='account'"></account_table>
                <news_table v-else-if="mode==='news'"></news_table>
                <notices_table v-else-if="mode==='notices'"></notices_table>
                <div v-else>欢迎管理员登录</div>
            </div>
        </div>
    </div>
</template>

<script>
import account_table from '../components/admin/Accounts.vue'
import news_table from '../components/admin/News.vue'
import notices_table from '../components/admin/Notices.vue'

export default {
    name: "Admin",
    data() {
        return {
            isActive: [1, 0, 0],
            mode: ''
        }
    },
    components: {
        account_table: account_table,
        news_table: news_table,
        notices_table: notices_table,
    },
    methods: {
        ViewContent(id) {
            if (id === "account") {
                this.isActive = [1, 0, 0];
            } else if (id === "news") {
                this.isActive = [0, 1, 0];
            } else if (id === 'notices') {
                this.isActive = [0, 0, 1];
            }
            this.mode = id;
            console.log(this.mode);

        }
    }

}
</script>


<style scoped>
/*container定义为伸缩盒，其子元素在y轴排列*/

.active {
    background-color: #42b983;
    box-shadow: 2px 2px 24px rgba(0, 0, 0, 0.15);
}

.container {
    display: flex;
    flex-direction: column;
    box-shadow: 1px 1px 24px rgba(0, 0, 0, 0.15);
    border-radius: 12px;
    padding: 15px 10px;
    background-color: rgb(245, 248, 252);
}

.top {
    /*基础高度为120px*/
    flex-basis: 120px;
    min-width: 1200px;
    background-color: lightblue;
    margin-bottom: 5px;

}

.container > .top > .logo {
    font-size: 26px;
    line-height: 120px;
    padding: 0 2em;
    font-weight: bolder;
    text-align: center;
}

/*内容框分配剩余空间,内容框作为伸缩盒，让子元素在x轴排列*/
.content {
    flex-grow: 1;
    background: #ededed;
    display: flex;
    flex-direction: row;
    overflow-y: scroll;
    flex-basis: 600px;
}

.content > .items_left {
    /*基础宽度200px*/
    flex-basis: 200px;
    padding-top: 50px;
    background-color: #FCEDED;
    margin-right: 5px;

}

/*right 分配content的剩余空间*/
.content > .tables_right {
    flex-grow: 1;
    padding: 1em;
    box-sizing: border-box;
}

ul{
    padding: 0;
}

.content > .items_left > ul > li {
    width: 200px;
    background-color: #ADD8E6;
    border-top: 1px solid #fff;
    line-height: 3em;
    text-align: center;
    font-size: 15px;
    list-style: none;

}

.content > .items_left > ul > li:first-child {
    border-top: none;
}

.content > .items_left > ul > li > a {
    color: #fff;

}

.content > .items_left > ul > li > a:hover {
    color: #FF9800;
}

.content > .items_left > ul > li:hover {
    box-shadow: inset 0 0 3px #fff;
}


</style>