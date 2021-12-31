<template>
    <div class="order">
        <el-tabs type="border-card">
            <el-tab-pane label="介绍">
                <p>开发语言：vue</p>
                <p>操作系统：跨平台</p>
                <p>功能简介：CMS测试平台是一款免费开源的自动化测试平台，最大的特点是全纬度覆盖了接口自动化、WEB</p>
                <p>UI自动化、APP自动化，并且支持分布式测试，测试关键字驱动也很大程度上解决了测试同学代码基础弱的问题。</p>
                <p>同时我们知道测试永远都只是质量保障的其中一个手段，所以也集成了质量管理相关的一些功能。</p>

                <p>分布式测试：使用Web-Client的方式，Web端负责基本信息管理展示，Client负责用例执行，任意无限扩展客户端。</p>
                <p>专业用例管理：自动化用例的专业管理方式，让您编写自动化用例更简单，直观。</p>
                <p>质量管理：Web端不仅仅有用来管理自动化相关的模块，更可以做一些简单的质量数据收集分析以及数据的多图表展示。</p>
                <p>多线程执行用例：客户端执行用例可以指定线程数量，用例运行更快速。</p>
                <p>多语言驱动：支持JAVA以及Python语言编写测试驱动，自动化测试手段更加灵活多变。</p>
                <p>定时任务调度：支持自定义配置调度任务，包括指定线程数，指定执行客户端，远程执行shell重启tomcat,对jenkins中的项目进行构建等。</p>
                <p>测试过程监控：客户端运行用例采用命令行的方式，在客户端可以实时查看过程。Web端可以通过任务查询查看测试进度。</p>
                <p>日志定位：客户端LOG4J+数据库记录测试过程日志，2种方式都可以通过Web端实时查看定位问题。</p>
            </el-tab-pane>
            <el-tab-pane label="套餐">
                <el-card class="box-card" v-for="product in products">
                    <template #header>
                        <div class="card-header">
                            <span>{{ product['title'] }}</span>
                            <el-button class="button" @click="createOrder(product['id'])">订购</el-button>
                        </div>
                    </template>
                    <div>
                        <p>时长：{{ product['time'] }}</p>
                        <p>价格：{{ product['price'] }}</p>
                        <p>说明：{{ product['desc'] }}</p>
                    </div>
                </el-card>
            </el-tab-pane>
            <el-tab-pane label="订单查询">Config</el-tab-pane>
            <el-tab-pane label="个人中心">Task</el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
import {ElMessage} from "element-plus";
import request from "../../utils/request";
import {UserFilled, Promotion} from "@element-plus/icons"
import {markRaw} from "vue";
import {loginMain} from '../../api/Login'

export default {
    name: "LoginIndex",
    data() {
        return {
            products: [
                {title: '包月套餐', time: '一月', price: 100.00, desc: '按月收费，当套餐到期后将无法使用。不享受优惠活动', id: 1},
                {title: '包年套餐', time: '一年', price: 1000.00, desc: '按年收费，当套餐到期后将无法使用。享受优惠活动', id: 2}
            ]
        }
    },
    components: {},
    methods: {
        createOrder(id) {
            request.get(`/api/Order?action=createOrder&product_id=${id}`).then(res => {
                    window.open(res['url'])
                }
            )
        },
    },
}
</script>

<style lang="less">
.card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.text {
    font-size: 14px;
}

.item {
    margin-bottom: 18px;
}

.box-card {
    width: 480px;
    margin: 10px;
}

</style>
