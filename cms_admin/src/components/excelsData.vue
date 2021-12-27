<template>
    <div class="title">{{ accountType }}</div>

    <div class="container">
        <span>请选择文件：</span>
        <a href="javascript:" class="file gradient">选择文件
            　　<input
                type="file"
                accept=".xls,.xlsx"
                @change="readExcel($event)"
            />
        </a>
        <!--        <input-->
        <!--            type="file"-->
        <!--            accept=".xls,.xlsx"-->
        <!--            @change="readExcel($event)"-->
        <!--            id="UpFile"-->
        <!--        />-->
        <el-button type="primary" size="mini" @click="checkInfo">核对编号</el-button>
        <el-button type="success" size="mini" :disabled="btnFlg" @click="entryMost">开始录入</el-button>
        <el-button type="info" size="mini" @click="this.lists=[];">清除数据</el-button>
    </div>

    <el-table :data="lists" style="width: 100%" :row-class-name="tableRowClassName" height="600">
        <el-table-column type="index" width="50"/>
        <el-table-column prop="realName" label="姓名" width="180"/>
        <el-table-column prop="No" label="学号" width="180"/>
        <el-table-column prop="major" label="专业"/>
        <el-table-column prop="gradeNo" label="年级"/>
        <el-table-column prop="classNo" label="班级"/>
        <el-table-column prop="result" label="结果"/>
    </el-table>

</template>

<script>
import XLSX from "xlsx"
import {ElMessage} from "element-plus"
import {accountMain} from "../api/Account";

export default {
    data() {
        return {
            upload_file: "",
            lists: [],
            // 用户类型
            accountType: '',
            accountTypeNum: 0,
            btnFlg: true
        };
    },
    watch: {
        '$route': 'before',
        accountType: function () {
            if (this.accountType === 'student') {
                this.accountTypeNum = 1000
            } else if (this.accountType === 'teacher') {
                this.accountTypeNum = 100
            } else if (this.accountType === 'mgr') {
                this.accountTypeNum = 1
            }
        },
    },
    mounted() {
        this.before()
    },
    methods: {
        before() {
            this.accountType = this.$route.query.type
        },

        readExcel(e) {
            // 读取表格文件
            let that = this;
            const files = e.target.files;
            if (files.length <= 0) {
                return false;
            } else if (!/\.(xls|xlsx)$/.test(files[0].name.toLowerCase())) {
                ElMessage({
                    message: "上传格式不正确，请上传xls或者xlsx格式",
                    type: "warning"
                });
                return false;
            } else {
                // 更新获取文件名
                that.upload_file = that.accountType + files[0].name;
            }

            const fileReader = new FileReader();
            fileReader.onload = ev => {
                try {
                    const data = ev.target.result;
                    const workbook = XLSX.read(data, {
                        type: "binary"
                    });
                    const wsName = workbook.SheetNames[0]; //取第一张表
                    const ws = XLSX.utils.sheet_to_json(workbook.Sheets[wsName]); //生成json表格内容
                    that.lists = [];
                    // 从解析出来的数据中提取相应的数据
                    ws.forEach(item => {
                        that.lists.push({
                            realName: item["姓名"],
                            username: item["学号"],
                            No: item["学号"],
                            major: item["专业"],
                            gradeNo: item["年级"],
                            classNo: item["班级"],
                            usertype: this.accountTypeNum
                        });
                    });
                } catch (e) {
                    return false;
                }
            };
            fileReader.readAsBinaryString(files[0]);
        },

        // 检查账号是否重复
        checkInfo() {
            const nos = []
            for (let i = 0; i < this.lists.length; i++) {
                if (nos.indexOf(this.lists[i]['No']) !== -1) {
                    return ElMessage({
                        message: `表格中编号 ${this.lists[i]['No']} 重复，请检查！`,
                        type: "warning"
                    });
                } else {
                    nos.push(this.lists[i]['No'])
                }

            }
            accountMain('check', this, {data: this.lists}).then(res => {
                    this.btnFlg = !res['flg']
                    for (let i = 0; i < this.lists.length; i++) {
                        this.lists[i].result = res['retlist'][i]
                    }
                }
            )
        },

        // 录入
        entryMost() {
            for (let i = 0; i < this.lists.length; i++) {
                accountMain('add', '', this.lists[i]).then(res => {
                    console.log(res['ret'])
                    if (res['ret'] === 0) {
                        this.lists[i].result = '录入成功'
                    } else {
                        this.lists[i].result = '录入失败'
                    }
                })
            }
        },

        // 改变颜色
        tableRowClassName({row, rowIndex}) {
            if (row.result === '核对通过' || row.result === '录入成功') {
                return 'success-row'
            } else {
                return 'warning-row'
            }
        },

    }
}
</script>

<style lang="less">
.title {
    text-align: center;
    font-size: 20px;
    color: #50ab36;
}

.container {
    margin-top: 10px;
    margin-bottom: 10px;
    height: 30px;

    input {
        line-height: 30px;
        margin-left: 5px;
    }

}

.el-table tr {
    /* background-color: var(--el-table-tr-background-color); */
}

.warning-row {
    background-color: #e9d1c3;
}

.success-row {
    background-color: #d6f3cf;
}

.file {
    position: relative;
    display: inline-block;
    background: #ccc;
    border: 1px solid #333;
    padding: 4px 20px;
    overflow: hidden;
    text-decoration: none;
    text-indent: 0;
    line-height: 20px;
    border-radius: 20px;
    color: #333;
    font-size: 13px;

    input {
        position: absolute;
        font-size: 100px;
        right: 0;
        top: 0;
        opacity: 0;
    }

}



</style>
