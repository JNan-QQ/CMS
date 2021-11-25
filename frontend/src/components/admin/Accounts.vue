<template>
  <div class="container">
    <div class="bar">
      <ul>
        <li :id="mode_opt[0]" @click="listAccount('mgr')"><a>管理员</a></li>
        <li :id="mode_opt[1]" @click="listAccount('teacher')"><a>教师</a></li>
        <li :id="mode_opt[2]" @click="listAccount('student')"><a>学生</a></li>
      </ul>
    </div>
    <div class="search">
      <select v-model="selected">
        <option disabled value="">请选择一个搜索类别</option>
        <option>id</option>
        <option>username</option>
        <option>class</option>
      </select>
      <strong style="margin: 0 2px 0 2px">:</strong>
      <input type="text" name="uname" placeholder="Search here..." />
      <button>SEARCH</button>
      <button class="add">添加</button>
    </div>
    <table>
      <caption>
        {{
          tableTitle
        }}
      </caption>
      <tr>
        <th>id</th>
        <th>userName</th>
        <th>realName</th>
        <th>studentNo</th>
        <th>classNo</th>
        <th>gradeNo</th>
        <th>major</th>
        <th>操作</th>
      </tr>
      <tr v-for="item in items" :key="item.id">
        <td>{{ item.id }}</td>
        <td>{{ item.username }}</td>
        <td>{{ item.realName }}</td>
        <td>{{ item.studentNo }}</td>
        <td>{{ item.classNo }}</td>
        <td>{{ item.gradeNo }}</td>
        <td>{{ item.major }}</td>
        <td><span>编辑</span><span>禁用</span><span>删除</span></td>
      </tr>
    </table>
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Accounts",
  data() {
    return {
      selected: "",
      tableTitle: "",
      items: [],
      mode_opt: ["active", "", ""],
    };
  },
  mounted() {
    this.first();
  },
  methods: {
    first() {
      const that = this;
      axios
        .post("/api/account/", {
          action: "list",
          pagenum: 1,
          pagesize: 5,
        })
        .then(function (response) {
          const data = response.data;
          that.items = data.retlist;
        });
    },
    listAccount(id) {
      const usertype = 0;
      if (id === "mgr") {
        usertype = 1;
        this.mode_opt = ["active", "", ""];
      } else if (id === "teacher") {
        usertype = 100;
        this.mode_opt = ["", "active", ""];
      } else {
        usertype = 1000;
        this.mode_opt = ["", "", "active"];
      }
      axios
        .post("/api/account/", {
          action: "list",
          pagenum: 1,
          pagesize: 5,
          seacher_type: { usertype: usertype },
        })
        .then(function (response) {
          const data = response.data;
          that.items = data.retlist;
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

.pages a.active,
.pages a:active {
  background-color: #ffa100;
}
</style>