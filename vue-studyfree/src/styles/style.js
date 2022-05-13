export const themes = {
    default: {
        'background-image': "linear-gradient(to bottom right, rgb(180, 189, 241), rgb(193, 160, 238));"
    }
}


// 修改页面中的样式变量值
const changeStyle = (obj) => {
    const ss = document.getElementsByTagName('body')[0]
    for (let key in obj) {
        ss.style.cssText = `${key}:${obj[key]}`
    }
};

// 改变主题的方法
export const setTheme = (rgb1, rgb2) => {
    // 保存主题到本地，下次进入使用该主题
    if (rgb1 !== null && rgb2 !== null) {
        localStorage.setItem('rgb1', rgb1)
        localStorage.setItem('rgb2', rgb2)
        const themeConfig = {'background-image': `linear-gradient(to bottom right, ${rgb1}, ${rgb2});`}
        changeStyle(themeConfig)
    } else {
        changeStyle(themes['default'])
    }

};
