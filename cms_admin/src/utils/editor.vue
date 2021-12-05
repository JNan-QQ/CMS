<template>
    <!-- ref配置 dom获取属性 -->
    <div ref="editorElem" style="text-align: left"></div>

</template>

<script>
import wangeditor from "wangeditor";

export default {
    data() {
        return {
            editor: null,
            editorContent: "",
        }
    },
    props:['baseTxt'],
    watch: {
        onEditorData(value) {
            console.log(value)
        },
    },
    mounted() {
        this.createEditor()
    },
    methods: {
        createEditor() {
            //获取dom元素 this.$refs.名字  进入富文本初始化  const editor = new E('#div1')
            this.editor = new wangeditor(this.$refs.editorElem);
            //配置 onchange 函数之后，用户操作（鼠标点击、键盘打字等）导致的内容变化之后，会自动触发 onchange 函数执行
            this.editor.config.onchange = (html) => {
                this.editorContent = html; //获取输入的值
                //把富文本器  里面输入的内容 传递给父组件使用数据
                this.$emit("onEditor", this.editorContent)
            }
            this.editor.config.uploadImgServer = '/api/files'
            this.editor.config.uploadFileName = 'files'
            this.editor.config.uploadImgParams = {
                action: 'upload',
            }
            this.editor.config.uploadImgHooks = {
                customInsert: function (insertImg, result, editor) {
                    // 图片上传并返回结果，自定义插入图片的事件（而不是编辑器自动插入图片！！！）
                    // insertImg 是插入图片的函数，editor 是编辑器对象，result 是服务器端返回的结果
                    // 举例：假如上传图片成功后，服务器端返回的是 {url:'....'} 这种格式，即可这样插入图片：
                    insertImg('/api' + result['file_url'])
                    // result 必须是一个 JSON 格式字符串！！！否则报错
                }
            }

            this.editor.config.menus = [
                // 菜单配置
                "head", // 标题
                "bold", // 粗体
                "fontSize", // 字号
                "fontName", // 字体
                "italic", // 斜体
                "underline", // 下划线
                "strikeThrough", // 删除线
                "foreColor", // 文字颜色
                "backColor", // 背景颜色
                "link", // 插入链接
                "list", // 列表
                "justify", // 对齐方式
                "quote", // 引用
                "emoticon", // 表情
                "image", // 插入图片
                "table", // 表格
                "code", // 插入代码
                "undo", // 撤销
                "redo", // 重复
            ];
            //创建富文本实例
            this.editor.create()
            //创建编辑器之后，使用 editor.txt.html(...) 设置编辑器内容   重新设置编辑器内容
            if (this.baseTxt){
                this.editor.txt.html(this.baseTxt)}

        }
    }
}
</script>

<style scoped>

</style>