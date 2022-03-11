// 获取时间戳
function time_salt() {
    let unix_time = new Date()
    const Y = unix_time.getFullYear() + '-'
    const M = (unix_time.getMonth() + 1 < 10 ? '0' + (unix_time.getMonth() + 1) : unix_time.getMonth() + 1) + '-'
    const D = unix_time.getDate() + ' '
    unix_time = Date.parse(new Date(Y + M + D + '00:00:00'))
    return unix_time.toString().slice(0, 8)
}

// 随机字符
function randomString(length) {
    let result = ''
    let chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for (let i = length; i > 0; --i) result += chars[Math.floor(Math.random() * chars.length)]
    return result
}

export function encrypt(s) {
    // 盐值用于加密钥生成
    let salt_base = `%@*${time_salt().split('').reverse().join('')}*@%`

    let n = parseInt(s.length / salt_base.length)

    //  加密钥
    let salt = salt_base.repeat(n + 1)

    let encry_str = ''

    for (let i = 0; i < s.length; i++) {

        let ss = (s[i].charCodeAt() + salt[i].charCodeAt()).toString()

        let cc = ss.split("")

        for (let _ = 0; _ < 5 - ss.length; _++) {

            cc.splice(Math.random() * (cc.length - 1), 0, randomString(1))
        }
        encry_str += cc.join('')
    }
    return encry_str

}