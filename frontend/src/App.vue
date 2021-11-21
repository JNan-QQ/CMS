<template>
    <main>
        <loginviwe></loginviwe>
    </main>
</template>

<script>
import loginviwe from './components/Login'

export default {
    name: 'App',
    components: {
        loginviwe,
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
