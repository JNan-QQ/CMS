<template>
    <md-editor
        v-if="isEdit"
        v-model="text"
    />
    <md-editor
        v-if="isView"
        v-model="text"
        previewOnly
    />
</template>

<script>
import MdEditor from 'md-editor-v3';
import 'md-editor-v3/lib/style.css';

export default {
    name: "noteView",
    data() {
        return {
            text: '',
            isView: false,
            isEdit: false,
        }
    },
    components: {MdEditor},
}
</script>

<style scoped lang="less">
#md-editor-v3 {
    min-width: 200px;
    max-width: 1140px;
    margin: 20px auto 0;
    padding: 15px 45px;
    position: relative;
    height: calc(90vh - 10px);
}

@media (max-width: 767px) {
    #md-editor-v3 {
        padding: 15px;
    }
}
</style>