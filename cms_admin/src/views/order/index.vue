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
                <div style="display: flex;flex-direction: row;flex-wrap: wrap;">
                    <el-card class="box-card" v-for="product in productsList">
                        <template #header>
                            <div class="card-header">
                                <span>{{ product['title'] }}</span>
                                <el-button class="button" @click="createOrder(product['id'])">订购</el-button>
                            </div>
                        </template>
                        <div>
                            <p>时长：{{ product['timeDays'] }} 天</p>
                            <p>价格：{{ product['price'] }} 元</p>
                            <p>说明：{{ product['desc'] }}</p>
                        </div>
                    </el-card>
                </div>
            </el-tab-pane>
            <el-tab-pane label="订单查询">
                <el-button type="primary" @click="listOrder" style="float: right">刷新</el-button>
                <el-table :data="orderList" stripe style="width: auto" height="600">
                    <el-table-column prop="orderNo" label="订单号" width="220"/>
                    <el-table-column prop="money" label="付款金额" width="180"/>
                    <el-table-column prop="product" label="套餐" width="180"/>
                    <el-table-column prop="create_time" label="创建时间" width="180"/>
                    <el-table-column prop="status" label="订单状态"/>
                </el-table>
            </el-tab-pane>
            <el-tab-pane label="个人中心">
                <el-descriptions :column="3">
                    <el-descriptions-item label="用户名：">{{ userInfo['user__username'] }}</el-descriptions-item>
                    <el-descriptions-item label="服务截止时间：">
                        <el-tag size="small">{{ userInfo['endTime'] }}</el-tag>
                    </el-descriptions-item>
                    <el-descriptions-item label="">
                        <el-button type="danger" size="small" @click="toLogout">退出登录</el-button>
                    </el-descriptions-item>
                    <el-descriptions-item label="设备1：">{{ userInfo['machineCode1'] }}</el-descriptions-item>
                    <el-descriptions-item label="设备2：">{{ userInfo['machineCode2'] }}</el-descriptions-item>
                    <el-descriptions-item label="设备3：">{{ userInfo['machineCode3'] }}</el-descriptions-item>
                </el-descriptions>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
import request from "../../utils/request";
import {loginMain} from "../../api/Login";
import userdata from '../../utils/gloab'

export default {
    name: "LoginIndex",
    data() {
        return {
            productsList: [],
            orderList: [],
            userInfo: {},
            userdata
        }
    },
    components: {},
    mounted() {
        this.listOrder()
        this.listProducts()
        this.listUserInfo()
    },
    methods: {
        before() {
        },
        createOrder(id) {
            request.get(`/Order?action=createOrder&product_id=${id}`).then(res => {
                    window.open(res['url'])
                }
            )
        },
        listOrder() {
            request.get('/Order?action=listOrder').then(res => {
                this.orderList = res['retlist']
                for (let i = 0; i < this.orderList.length; i++) {
                    const status = this.orderList[i]['status']
                    if (status === 1) {
                        this.orderList[i]['status'] = '未付款'
                    } else if (status === 2) {
                        this.orderList[i]['status'] = '已付款'
                    }
                }
            })
        },
        listProducts() {
            request.get('/Product?action=listProducts').then(res => {
                this.productsList = res['retlist']
            })
        },
        listUserInfo() {
            request.get('/Token?action=userInfo').then(res => {
                this.userInfo = res['retlist']
            })
        },
        // 退出登录函数
        toLogout() {
            loginMain('signout')
            this.userdata = {
                realName: '未登录',
                aviator: '',
                id: 0,
                usertype: 0
            }
            this.$router.push('/login')
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
