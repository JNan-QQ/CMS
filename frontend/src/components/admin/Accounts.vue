<template>
    <div class="container">
        <!-- 头部导航栏 -->
        <div class="bar">
            <ul>
                <li :id="mode_opt[0]" @click="listAccount('mgr')"><a>管理员</a></li>
                <li :id="mode_opt[1]" @click="listAccount('teacher')"><a>教师</a></li>
                <li :id="mode_opt[2]" @click="listAccount('student')"><a>学生</a></li>
            </ul>
        </div>

        <!-- 搜索栏 -->
        <div class="search">
            <select v-model="selected">
                <option disabled value="">请选择一个搜索类别</option>
                <option value="id">id</option>
                <option value="username">username</option>
                <option value="realName">realName</option>
                <option value="studentNo">studentNo</option>
                <option value="classNo">classNo</option>
                <option value="gradeNo">gradeNo</option>
                <option value="major">gradeNo</option>
            </select>
            <strong style="margin: 0 2px 0 2px">:</strong>
            <input type="text" v-model="searchInput" placeholder="Search here..."/>
            <button @click="searchAccount">SEARCH</button>
            <button class="add" @click="addActive = 1">添加</button>
        </div>

        <!-- 列表内容 -->
        <table>
            <caption>{{ tableTitle }}</caption>
            <tr>
                <th>id</th>
                <th>userName</th>
                <th>realName</th>
                <th v-show="mode_usertype===1000">studentNo</th>
                <th v-show="mode_usertype===1000">classNo</th>
                <th v-show="mode_usertype===1000">gradeNo</th>
                <th v-show="mode_usertype!==1">major</th>
                <th>操作</th>
            </tr>
            <tr v-for="item in items" :key="item.id">
                <td>{{ item['id'] }}</td>
                <td>{{ item['username'] }}</td>
                <td>{{ item['realName'] }}</td>
                <td v-show="mode_usertype===1000">{{ item['studentNo'] }}</td>
                <td v-show="mode_usertype===1000">{{ item['classNo'] }}</td>
                <td v-show="mode_usertype===1000">{{ item['gradeNo'] }}</td>
                <td v-show="mode_usertype!==1">{{ item['major'] }}</td>
                <td><span>编辑</span><span>禁用</span><span>删除</span></td>
            </tr>
        </table>

        <!-- 翻页 -->
        <div class="pages">
            <ul>
                <li>
                    <a href="#" class="prev">
                        <i class="fa fa-chevron-left"></i>
                        Previous
                    </a>
                </li>
                <li><a href="#">1</a></li>
                <li><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li><a href="#" class="active">5</a></li>
                <li><a href="#">6</a></li>
                <li><a href="#">7</a></li>
                <li>
                    <a href="#" class="next">
                        Next
                        <i class="fa fa-chevron-right"></i>
                    </a>
                </li>
            </ul>
        </div>

        <!-- 添加账号弹窗 -->
        <div class="modal" v-if="addActive===1">
            <div class="addView">
                <div class="item"><span>username:</span><input type="text" v-model="userInfo[0]"></div>
                <div class="item"><span>realName:</span><input type="text" v-model="userInfo[1]"></div>
                <div class="item" v-show="mode_usertype===1000"><span>studentNo:</span><input type="text"
                                                                                              v-model="userInfo[2]">
                </div>
                <div class="item" v-show="mode_usertype===1000"><span>classNo:</span><input type="text"
                                                                                            v-model="userInfo[3]"></div>
                <div class="item" v-show="mode_usertype===1000"><span>gradeNo:</span><input type="text"
                                                                                         v-model="userInfo[4]"></div>
                <div class="item" v-show="mode_usertype!==1"><span>major:</span><input type="text"
                                                                                       v-model="userInfo[5]"></div>
                <div class="item" style="color: red">初始密码：123456</div>
                <div class="item">
                    <input class="button" type="button" value="确定" @click="addAccount">
                    <input class="button" type="button" value="取消" @click="addActive = 0">
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "Accounts",
    data() {
        return {
            selected: "",
            searchInput: "",
            tableTitle: "",
            items: [],
            mode_opt: ["active", "", ""],
            mode_usertype: 0,
            addActive: 0,
            userInfo: ['', '', '', '', '', ''],
        };
    },
    mounted() {
        this.first();
    },
    methods: {

        //预加载显示数据
        first() {
            const that = this;
            axios.post("/api/account/", {
                action: "list",
                pagenum: 1,
                pagesize: 10,
                search_items: {usertype: 1},
            }).then(function (response) {
                const data = response.data;
                that.items = data['retlist'];
            });
        },

        //按照 用户 账号类型显示
        listAccount(id) {
            const that = this;
            if (id === "mgr") {
                this.mode_usertype = 1;
                this.mode_opt = ["active", "", ""];
            } else if (id === "teacher") {
                this.mode_usertype = 100;
                this.mode_opt = ["", "active", ""];
            } else {
                this.mode_usertype = 1000;
                this.mode_opt = ["", "", "active"];
            }
            axios.post("/api/account/", {
                action: "list",
                pagenum: 1,
                pagesize: 10,
                search_items: {usertype: this.mode_usertype},
            })
                .then(function (response) {
                    const data = response.data;
                    that.items = data['retlist'];
                });
        },

        // 按照字段查找账号
        searchAccount() {
            const that = this;
            if (this.selected !== '') {
                if (this.searchInput !== '') {
                    const search_item = {};
                    search_item['usertype'] = this.mode_usertype;
                    search_item[this.selected] = this.searchInput;

                    axios.post("/api/account/", {
                        action: "list",
                        pagenum: 1,
                        pagesize: 10,
                        search_items: search_item,
                    })
                        .then(function (response) {
                            const data = response.data;
                            that.items = data['retlist'];
                        });
                } else {
                    alert('请输入搜索字段内容！');
                }
            }
        },

        // 添加账号
        addAccount() {
            const that = this;
            const user_item = {};
            user_item['action'] = 'add';
            user_item['usertype'] = this.mode_usertype;
            user_item['username'] = this.userInfo[0];
            user_item['realName'] = this.userInfo[1];
            user_item['password'] = '123456';
            if (this.userInfo[2] !== '') user_item['studentNo'] = this.userInfo[2]
            if (this.userInfo[3] !== '') user_item['classNo'] = this.userInfo[3]
            if (this.userInfo[4] !== '') user_item['gradeNo'] = this.userInfo[4]
            if (this.userInfo[5] !== '') user_item['major'] = this.userInfo[5]

            axios.post("/api/account/", user_item).then(function (response) {
                const data = response.data
                if (data['ret'] === 0) {
                    alert(data['id']);
                    that.userInfo = ['', '', '', '', '', '']
                    that.addActive = 0
                } else if (data['ret'] === 1) {
                    alert(data['msg']);
                }
            });
        },
    },
};
</script>

<style scoped>
/*整体界面*/
.container {
    display: flex;
    flex-direction: column;
    min-height: 540px;
    box-shadow: 1px 1px 24px rgba(0, 0, 0, 0.15);
    border-radius: 12px;
    padding: 15px 10px;
    background-color: rgb(245, 248, 252);
}

/*导航栏*/
.bar {
    box-shadow: 1px 1px 24px rgba(0, 0, 0, 0.15);
    border-radius: 10px;
    margin-bottom: 10px;
}

.bar ul {
    list-style-type: none;
    margin-left: 10px;
    margin-top: 2px;
    margin-bottom: 3px;
    text-align: center;
    font-size: 14px;
}

.bar li {
    float: left; /*改动的地方*/
    width: 80px;
    padding: 10px;
    background-color: #ff9137;
    border-radius: 10px;
}

a:link,
a:visited,
a:hover,
a:active {
    color: #fff;
    text-decoration: none;
}

.bar a {
    display: block; /*整体变为可点击区域，而不只是字*/
}

/*搜索栏*/
.search {
    box-shadow: 1px 1px 24px rgba(0, 0, 0, 0.15);
    border-radius: 10px;
    margin-bottom: 10px;
    min-height: 40px;
}

.search > select {
    margin-left: 10px;
    border-radius: 5px;
    margin-top: 10px;
    margin-bottom: 10px;
    height: 20px;
    width: auto;
}

.search > input {
    border: 1px solid #7cb47e;
    border-radius: 5px 0 0 5px;
    color: #9e9c9c;
    margin-top: 10px;
    margin-bottom: 10px;
    height: 20px;
    width: auto;
}

.search > button {
    right: 0;
    background: #a7b8b9;
    border-radius: 0 5px 5px 0;
    margin-top: 10px;
    margin-bottom: 10px;
    height: 20px;
    width: auto;
}

.search > button.add {
    border-radius: 5px;
    margin-left: 10px;
    height: 20px;
}

#active {
    color: #50ab36;
    box-shadow: 0 0 24px rgba(0, 0, 0, 0.5);
}

/*列表*/
table {
    box-shadow: 1px 1px 24px rgba(0, 0, 0, 0.15);
    border-radius: 10px;
    margin-bottom: 10px;
}

th {
    font-weight: bold;
    background-color: #eff6fe;
    color: #90c0fe;
}

th,
td {
    font-size: 0.95em;
    text-align: center;
    padding: 4px;
    border-collapse: collapse;
}

th,
td {
    border: 1px solid #ffffff;
}

th {
    border: 1px solid #eff6fe;
}

td {
    border: 1px solid #eeeeee;
}

tr {
    border: 1px solid #ffffff;
    margin-left: 10px;
}

tr:nth-child(odd) {
    background-color: #f7f7f7;
}

tr:nth-child(even) {
    background-color: #ffffff;
}

/*分页*/
.pages {
    list-style: none;
    display: inline-block;
    padding: 0;
    margin: auto auto 0 auto;
}

.pages li {
    display: inline;
    text-align: center;
}

.pages a {
    float: left;
    display: block;
    font-size: 14px;
    text-decoration: none;
    padding: 5px 12px;
    color: #fff;
    margin-left: -1px;
    border: 1px solid transparent;
    line-height: 1.5;
}

.pages a.active {
    cursor: default;
}

.pages a:active {
    outline: none;
}

.pages a {
    margin: 0 5px;
    padding: 0;
    width: 30px;
    height: 30px;
    line-height: 30px;
    -moz-border-radius: 100%;
    -webkit-border-radius: 100%;
    border-radius: 100%;
    background-color: #f7c12c;
}

.pages a.prev {
    -moz-border-radius: 50px 0 0 50px;
    -webkit-border-radius: 50px;
    border-radius: 50px 0 0 50px;
    width: 100px;
}

.pages a.next {
    -moz-border-radius: 0 50px 50px 0;
    -webkit-border-radius: 0;
    border-radius: 0 50px 50px 0;
    width: 100px;
}

.pages a:hover {
    background-color: #ffa500;
}

.pages a.active, .pages a:active {
    background-color: #ffa100;
}

/*添加账号弹窗*/
.modal {
    position: fixed;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    background-color: rgba(0, 0, 0, 0.5);
}

.addView {
    max-width: 400px;
    height: auto;
    box-shadow: 0 0 24px rgba(0, 0, 0, 0.15);
    border-radius: 24px;
    padding: 48px 28px;
    background-color: rgb(245, 246, 252);
    margin: 100px auto;
}

.addView .item {
    position: relative;
    display: flex;
    align-items: center;
}

.addView .item input {
    padding: 16px 20px 16px 20px;
    border-radius: 48px;
    border: none;
    outline: none;
    box-shadow: 0 0 24px rgba(0, 0, 0, 0.08);
    width: 280px;
    font-size: 16px;
    color: #626262;
    margin-top: 10px;
    margin-bottom: 10px;
    margin-left: 10px;
}

.addView .item span {
    width: 100px;
}

.addView .button {
    display: inline-block;
    padding: 25px 25px;
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
    margin-right: auto;
}

</style>