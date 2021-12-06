<template>

</template>

<script>
export default {
    name: "account",
    data(){
      return {
          accountData:[],
      }
    },
    mounted() {
        this.before()
    },
    methods:{
        before(){
            console.log(this.$route.query)
        }
    },
}
</script>

<style scoped>

</style>
