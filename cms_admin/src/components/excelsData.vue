<template>
    <div>
        <div class="container">
            {{ upload_file || "导入" }}
            <input
                type="file"
                accept=".xls,.xlsx"
                class="upload_file"
                @change="readExcel($event)"
            />
        </div>
        <el-table :data="lists" style="width: 100%">
            <el-table-column prop="username" label="姓名" width="180"/>
            <el-table-column prop="No" label="学号" width="180"/>
            <el-table-column prop="major" label="专业"/>
            <el-table-column prop="grade" label="年级"/>
            <el-table-column prop="class" label="班级"/>
        </el-table>
    </div>
</template>

<script>
import XLSX from "xlsx"
import {ElMessage} from "element-plus"

export default {
    data() {
        return {
            upload_file: "",
            lists: []
        };
    },
    methods: {
        submit_form() {
            // 给后端发送请求，更新数据
            console.log("假装给后端发了个请求...");
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

                        });
                    });
                } catch (e) {
                    return false;
                }
            };
            fileReader.readAsBinaryString(files[0]);
        }
    }
}
</script>

<style scoped>

</style>
