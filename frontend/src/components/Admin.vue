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
                    <li class="active"><a>账号管理</a>
                        <ul>
                            <li><a>管理员</a></li>
                            <li><a>教师</a></li>
                            <li><a>学生</a></li>
                        </ul>
                    </li>
                    <li><a>新闻管理</a></li>
                    <li><a>通知管理</a></li>
                    <li><a>其他（待添加）</a></li>
                </ul>
            </div>
            <!--内容展示-->
            <div class="tables_right">
                <account_table>表格</account_table>
                <news_table>表格</news_table>
                <notices_table>表格</notices_table>
            </div>
        </div>
    </div>
</template>

<script>
import account_table from './admin/Accounts.vue'
import news_table from './admin/News.vue'
import notices_table from './admin/Notices.vue'

export default {
    name: "Admin",
    data() {
        return {

        }
    },
    components: {
        account_table: account_table,
        news_table: news_table,
        notices_table: notices_table,
    },

}
</script>


<style scoped>
/*container定义为伸缩盒，其子元素在y轴排列*/

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

.content > .tables_right > .wrapper {
    height: 100%;
    background-color: #fff;
    border-radius: 5px;
    overflow-y: auto; /*在y轴方向如果内容过多，会出现滚动条*/
    box-shadow: 0 0 5px #ccc;
}

.content > .items_left > ul > li {
    width: 200px;
    background-color: #ADD8E6;
    border-top: 1px solid #fff;
    line-height: 3em;
    text-align: center;
    font-size: 15px;

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

.items_left > ul > li > ul {
    display: none;
}

.items_left > ul > li:hover > ul {
    display: block;
}

.items_left > ul > li > ul a:hover {
    color: #FF9800;
}

.items_left > ul > li > ul > li {
    margin-top: 3px;
    background-color: #116f8d;
}


</style>