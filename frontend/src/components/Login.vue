<template>
    <div class="container">
        <h1>Login</h1>
        <div class="item">
            <i class="fa fa-github-alt" style="font-size:24px"></i>
            <input type="text" placeholder="Username" v-model="state.username">
        </div>
        <div class="item">
            <i class="fa fa-search" style="font-size:24px"></i>
            <input type="text" placeholder="Password" v-model="state.password">
        </div>
        <div class="item">
            <input class="button" type="button" value="登陆" @click="signin">
        </div>

    </div>
</template>

<script>

import {ref} from "vue";
import {axios} from "axios"

export default {
    name: "Login",
    setup() {

        let username=ref('');
        let password=ref('');

        function signin() {
            axios.post()
        }

    }
}
</script>

<style scoped>
.container {
    width: 60%;
    max-width: 400px;
    box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.15);
    border-radius: 24px;
    padding: 48px 28px;
    background-color: rgb(245, 246, 252);
}

/* 标题 */
h1 {
    margin: 24px 0;
    font-size: 28px;
    color: #414873;
    text-align: center;
}

/* 添加框 */
.item {
    position: relative;
    display: flex;
    align-items: center;
}

.item input {
    padding: 16px 52px 16px 18px;
    border-radius: 48px;
    border: none;
    outline: none;
    box-shadow: 0px 0px 24px rgba(0, 0, 0, 0.08);
    width: 100%;
    font-size: 16px;
    color: #626262;
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 10px;
}

.button {
    display: inline-block;
    padding: 15px 25px;
    font-size: 16px;
    cursor: pointer;
    text-align: center;
    text-decoration: none;
    outline: none;
    color: #fff;
    background-color: #a7e8de;
    border: none;
    border-radius: 15px;
    box-shadow: 0 9px #999;
    margin-right: 10px;
}

.button:hover {
    background-color: #5c7a5d
}

.button:active {
    background-color: #7cb47e;
    box-shadow: 0 5px #666;
    transform: translateY(4px);
}

</style>