import hljs from "highlight.js";
// import 'highlight.js/styles/atom-one-dark.css'

// 代码高亮
export default (app) => {
    app.directive("highlight", function (el) {
        let blocks = el.querySelectorAll("pre code");
        blocks.forEach(block => {
            hljs.highlightBlock(block);
        });
    })
}