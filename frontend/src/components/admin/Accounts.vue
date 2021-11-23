<template>
<div id="search"><input class="input" type="search" placeholder="请输入关键词"></div>
</template>

<script>
export default {
    name: "Accounts"
}
</script>

<style scoped>
[type=search]::-webkit-search-cancel-button{
    -webkit-appearance: none;
    width: 36px;
    height: 36px;
    border: 0;
    background: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'%3E %3Cpath d='M256 8C119 8 8 119 8 256s111 248 248 248 248-111 248-248S393 8 256 8zm121.6 313.1c4.7 4.7 4.7 12.3 0 17L338 377.6c-4.7 4.7-12.3 4.7-17 0L256 312l-65.1 65.6c-4.7 4.7-12.3 4.7-17 0L134.4 338c-4.7-4.7-4.7-12.3 0-17l65.6-65-65.6-65.1c-4.7-4.7-4.7-12.3 0-17l39.6-39.6c4.7-4.7 12.3-4.7 17 0l65 65.7 65.1-65.6c4.7-4.7 12.3-4.7 17 0l39.6 39.6c4.7 4.7 4.7 12.3 0 17L312 256l65.6 65.1z'%3E%3C/path%3E %3C/svg%3E") center no-repeat;
    background-size: 16px;
    cursor: pointer;
    opacity: .4;
    transition: .2s;
}
</style>