<template>
    <div class="box upDown">
        <div class="handler ">
            <span>你好？？</span>

        </div>
        <div class="rl">
            <div class="items_list">
                <ul>
                    <li><a class="active">账号管理</a></li>
                    <li><a>新闻管理</a></li>
                    <li><a>通知管理</a></li>
                    <li><a>其他（待添加）</a></li>
                </ul>
            </div>
            <div class="content" >
                <span>表格</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Admin"
}
</script>

<style scoped>
/*********** 声明顶部样式 ***********/

/*********** 声明左侧列表样式 ***********/
.upDown {
    margin: auto;
    width: 50%;
    border: 3px solid green;
    padding: 10px;
}
.rl{
    float: left;
    width: 300px;
    border: 3px solid #73AD21;
    padding: 10px;
}

ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    width: 200px;
    background-color: #f1f1f1;
    border: 1px solid #555;
}

li a {
    display: block;
    color: #000;
    padding: 8px 16px;
    text-decoration: none;
}

li {
    text-align: center;
    border-bottom: 1px solid #555;
}

li:last-child {
    border-bottom: none;
}

li a.active {
    background-color: #4CAF50;
    color: white;
}

li a:hover:not(.active) {
    background-color: #555;
    color: white;
}

</style>