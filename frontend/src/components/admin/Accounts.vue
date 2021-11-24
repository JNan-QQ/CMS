<template>
    <div class="container">
        <div class="bar">
            <ul>
                <li><a>管理员</a></li>
                <li><a>教师</a></li>
                <li><a>学生</a></li>
            </ul>
        </div>
        <div class="search">
            <select v-model="selected">
                <option disabled value="">请选择一个搜索类别</option>
                <option>id</option>
                <option>username</option>
                <option>class</option>
            </select>
            :
            <input type="text" name="uname" placeholder="Search here...">
            <button>SEARCH
                <span class="t"></span>
            </button>
        </div>
        <table>
            <caption>{{ tableTitle }}</caption>
            <tr>
                <th>id</th>
                <th>userName</th>
                <th>realName</th>
                <th>studentNo</th>
                <th>classNo</th>
                <th>gradeNo</th>
                <th>major</th>
            </tr>
            <tr v-for="item in items">
                <td>{{ item.id }}</td>
                <td>{{ item.username }}</td>
                <td>{{ item.realName }}</td>
                <td>{{ item.studentNo }}</td>
                <td>{{ item.classNo }}</td>
                <td>{{ item.gradeNo }}</td>
                <td>{{ item.major }}</td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: "Accounts",
    data() {
        return {
            selected: '',
            tableTitle: '',
            items: [{
                "id": "1",
                "username": "jj",
                "realName": "cc",
                "studentNo": "1360541",
                "classNo": "1604",
                "gradeNo": "2018",
                "major": "自动化"
            }],
        }
    }
}
</script>

<style scoped>
/*整体界面*/
.container {
    display: flex;
    flex-direction: column;

    box-shadow: 1px 1px 24px rgba(0, 0, 0, 0.15);
    border-radius: 12px;
    padding: 15px 10px;
    background-color: rgb(245, 248, 252);
}

/*导航栏*/
.bar ul {
    list-style-type: none;
    margin: auto; /*margin:100px auto无效,不能使ul左右居中*/
    text-align: center;
    font-size: 14px;
}

li {
    float: left; /*改动的地方*/
    width: 80px;
    padding: 10px;
    background-color: #ff9137;
}

a:link, a:visited, a:hover, a:active {
    color: #fff;
    text-decoration: none;
}

a {
    display: block; /*整体变为可点击区域，而不只是字*/
}

/*搜索栏*/

/*列表*/
th {
    font-weight: bold;
    background-color: #eff6fe;
    color: #90c0fe
}

th, td {
    font-size: 0.95em;
    text-align: center;
    padding: 4px;
    border-collapse: collapse;
}

th, td {
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
}

tr:nth-child(odd) {
    background-color: #f7f7f7;
}

tr:nth-child(even) {
    background-color: #ffffff;
}


</style>