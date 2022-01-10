<template>
    <div class="main-article">
        <div class="slide-item-table">
            <div class="text-center"><h2 class="slider_title">StudyFree，学习笔记好帮手！</h2>
                <p class="product-desctext">开开心心学习，快快乐乐生活</p>
            </div>
            <div class="tag_items">
                <el-tag size="large">Tag 1</el-tag>
                <el-tag class="ml-2" type="success">Tag 2</el-tag>
                <el-tag class="ml-2" type="info">Tag 3</el-tag>
                <el-tag class="ml-2" type="warning">Tag 4</el-tag>
                <el-tag class="ml-2" type="danger">Tag 5</el-tag>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: "article"
}
</script>

<style lang="less">
.main-article {
    height: auto;
    background-color: #FFFFFF;
    color: #FFFFFF;
    position: relative;

    .slide-item-table {
        height: 280px;
        background-image: url("../../assets/coursebg.jpg");
        border-top: #FFFFFF solid 1px;

        .text-center {
            text-align: center;
            margin-top: 110px;
            margin-bottom: 10px;

            .slider_title {
                font: 36px 'Arial Rounded MT Bold';
            }

            .product-desctext {
                font-size: 14px;
                margin-top: 10px;
            }
        }
    }

    .tag_items {

        text-align: center;
        margin-top: 40px;

        .el-tag {
            margin-left: 6px;
            margin-right: 6px;
            background-color:transparent;
            color: #FFFFFF;
        }
    }
}

</style>
