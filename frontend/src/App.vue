<template>
    <main>
        <login_view v-on:view_mode="view_mode" v-if="mode==='登录'"></login_view>
        <home_view v-else-if="mode==='主页'"></home_view>
        <admin_view v-else-if="mode==='后台'"></admin_view>
    </main>
</template>

<script>
import login_view from './pages/Login.vue'
import home_view from './pages/Home.vue'
import admin_view from './pages/Admin.vue'

export default {
    name: 'App',
    data() {
        return {
            mode: '',
        }
    },
    components: {
        home_view: home_view,
        login_view: login_view,
        admin_view: admin_view,
    },
    methods: {
        view_mode(e) {
            console.log(e)
            this.mode = e;
        }

    }
}
</script>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: Helvetica, "PingFang SC", "Microsoft Yahei", sans-serif;
}

/* 整个页面 */
main {
    width: 100vw;
    min-height: 100vh;
    padding: 10vh 0;
    display: grid;
    align-items: start;
    justify-items: center;
    background: #d8dfff;
}

</style>
