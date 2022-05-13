<template>
    <div :style="styleObject">
        <el-pagination
            :layout="layout"
            :current-page.sync="current_page"
            :page-size="page_size"
            :page-sizes="page_sizes"
            background
            :total="total"
            :hide-on-single-page="btn_background"
            @current-change="handleCurrentChange"
            @size-change="handleSizeChange"
        />
    </div>
</template>

<script>
export default {
    name: "pages",
    data() {
        return {
            page_size: 10,
            current_page: 1,
        }
    },
    props: {
        total: {
            type: Number,
            default: 0
        },
        layout: {
            type: String,
            default: "prev, pager, next, sizes"
        },
        page_sizes: {
            type: Array,
            default: [5, 10, 15, 20]
        },
        btn_background: {
            type: Boolean,
            default: true
        },
        styleObject: {
            type: Object,
            default: {
                textAlign: 'center',
                position: 'relative'
            }
        }
    },
    methods: {
        // 翻页
        handleCurrentChange: function (currentPage) {
            this.current_page = currentPage
            this.$emit('get-data', this.current_page, this.page_size)
        },
        // 改变每页尺寸
        handleSizeChange: function (number) {
            this.current_page = 1
            this.page_size = number
            this.$emit('get-data', this.current_page, this.page_size)
        }
    }
}
</script>

<style scoped>

</style>