<template>
    <div class="title">{{ accountType }}</div>

    <div class="container">
        <span>请选择文件：</span>
        <input
            type="file"
            accept=".xls,.xlsx"
            class="upload_file"
            @change="readExcel($event)"
        />
        <el-button type="primary" size="mini" @click="checkInfo">核对编号</el-button>
        <el-button type="success" size="mini" :disabled="btnFlg">开始录入</el-button>
    </div>

    <el-table :data="lists" style="width: 100%" :row-class-name="tableRowClassName" height="600">
        <el-table-column type="index" width="50"/>
        <el-table-column prop="realName" label="姓名" width="180"/>
        <el-table-column prop="No" label="学号" width="180"/>
        <el-table-column prop="major" label="专业"/>
        <el-table-column prop="grade" label="年级"/>
        <el-table-column prop="class" label="班级"/>
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
            btnFlg:true
        };
    },
    watch: {
        '$route': 'before',
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
                that.upload_file = files[0].name;
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
                            grade: item["年级"],
                            class: item["班级"],
                        });
                    });
                } catch (e) {
                    return false;
                }
            };
            fileReader.readAsBinaryString(files[0]);
        },

        checkInfo() {
            accountMain('check', this, {data: this.lists}).then(res => {
                    this.btnFlg = !('编号重复' in res['retlist'])
                console.log(('编号重复' in res['retlist']))
                    for (let i = 0; i < this.lists.length; i++) {
                        this.lists[i].result = res['retlist'][i]
                    }
                }
            )
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

.warning-row {
    --el-table-tr-bg-color: var(--el-color-warning-lighter);
}

.success-row {
    --el-table-tr-bg-color: var(--el-color-success-lighter);
}

</style>
