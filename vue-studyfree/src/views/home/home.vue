<template>
    <div class="main-view">
        <div class="product_name">
            <el-image :src="require('../../assets/studyfree_home.png')" fit="fill"
                      style="width: 360px;"></el-image>
        </div>
        <p class="product-desc">{{ cq }}</p>
        <p class="product-desc product-desc1">生活明朗，万物可爱，人间值得，未来可期</p>
        <div class="button-area">
            <router-link to="/Article">
                <el-button :icon="Notebook" size="large" color="#28c58d">文章</el-button>
            </router-link>
            <router-link to="/Note">
                <el-button :icon="Document" size="large" color="#4d2c8b">笔记</el-button>
            </router-link>
            <router-link to="/Skill">
                <el-button :icon="Flag" size="large" color="#b1149e">技巧</el-button>
            </router-link>
        </div>
    </div>
</template>

<script>
import {getCq} from "@/api/common";
import {markRaw} from "vue";
import {Document, Flag, Notebook} from "@element-plus/icons";

export default {
    name: "home",
    data(){
        return {
            Notebook: markRaw(Notebook), Document: markRaw(Document), Flag: markRaw(Flag),
            cq:''
        }
    },
    mounted() {
        getCq().then(res => {
            this.cq = res['retlist'].content
        })
    }

}
</script>

<style lang="less">

.main-view {
    position: absolute;
    left: 0;
    top: 44%;
    transform: translateY(-50%);
    box-sizing: border-box;
    max-width: 960px;
    text-align: center;
    padding: 40px;
    margin: 0 auto;
    right: 0;

    .product_name {
        display: inline-block;
    }

    .product-desc {
        height: 36px;
        font-size: 28px;
        font-family: Avenir-Medinum, serif;
        margin: 20px 10px 0;
        color: #FFFFFF;
    }

    .product-desc1 {
        font-size: 16px;
    }

    .button-area {
        font: 14px "Microsoft YaHei UI Light";
        margin: 55px 0 0;

        .el-button {
            margin-right: 10px;
            margin-left: 10px;
            padding: 0 40px;
            color: #FFFFFF;
        }
    }
}

</style>
