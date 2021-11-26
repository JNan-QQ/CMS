<template>
    <div class="box" v-if="isNoticeShow">
        <h3>{{ title }}</h3>
        <p class="box-content">{{ message }}</p>
    </div>
</template>

<script>
export default {
    name: 'popup',
    props: {
        title: {
            type: String,
            default: ''
        },
        message: {
            type: String,
            default: ''
        },
        duration: {
            type: Number,
            default: 1000
        }
    },
    data() {
        return {
            isNoticeShow: false
        }
    },
    methods: {
        show() {
            this.isNoticeShow = true
            setTimeout(this.hide, this.duration)
        },
        hide() {
            this.isNoticeShow = false
            // 清除自己
            this.remove()
        }
    }
}
</script>