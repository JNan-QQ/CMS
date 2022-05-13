<template>
    <vue-particles v-if="particles"
                   color="#409EFF"
                   :particleOpacity="0.7"
                   :particlesNumber="60"
                   shapeType="circle"
                   :particleSize="6"
                   linesColor="#409EFF"
                   :linesWidth="1"
                   :lineLinked="true"
                   :lineOpacity="0.4"
                   :linesDistance="150"
                   :moveSpeed="3"
                   :hoverEffect="true"
                   hoverMode="grab"
                   :clickEffect="true"
                   clickMode="push">
    </vue-particles>

    <!--    路由出口函数    -->
    <router-view/>

</template>

<script>
import {setTheme} from '@/styles/style.js'

export default {
    name: 'App',
    data() {
        return {
            particles: false,
        }
    },
    mounted() {
        this.particles = localStorage.getItem('particles') !== 'false'
        setTheme(localStorage.getItem('rgb1'), localStorage.getItem('rgb2'))
    },
    watch: {
        '$store.state.particles'(){
            this.particles = this.$store.state.particles
        }
    },
    methods: {}
}

</script>

<style lang="less">
#particles-js {
    width: 100%;
    height: calc(100% - 100px);
    position: fixed;
}
</style>
