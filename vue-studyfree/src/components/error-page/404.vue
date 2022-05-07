<template>
    <div class="lose-main">
        <div class="lose-box">
            <img src="../../assets/error-page/404.png" alt="404">
            <p>抱歉，没有找到您请求的页面</p>
            <p class="lose-en">Sorry, didn't find the page you requet.</p>
            <router-link to="/home">返回首页</router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "404"
}
</script>

<style scoped lang="less">
.lose-main {
    background: url(../../assets/error-page/404-backgroud.png) 0 0 no-repeat;
    background-size: 100%;
    min-height: 540px;

    .lose-box {
        width: 440px;
        height: 450px;
        position: absolute;
        left: 50%;
        top: 50%;
        margin: -225px 0 0 -220px;

        img {
            margin-bottom: 50px;
        }

        p {
            margin: 0;
            color: #fff;
            line-height: 30px;
            text-align: center;
            font-size: 18px;
        }

        .lose-en {
            font-size: 14px;
        }

        a {
            width: 218px;
            height: 50px;
            display: block;
            margin: 50px auto 0 auto;
            border: solid 1px #fff;
            border-radius: 3px;
            text-align: center;
            line-height: 50px;
            color: #fff;
            text-decoration: none;
            transition: all ease-out .4s;
        }
    }
}
</style>