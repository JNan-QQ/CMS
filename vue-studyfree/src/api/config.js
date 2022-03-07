
// uploadFile api
const upload_url = 'https://student.waiyutong.org/Practice/compositionUploadImg.html'

const upload_cookies = {
    "PHPSESSID": "acogbchfoacogbchfohu213jefu2ufmb9b3few10",
    "SERVER_NO": "FE-W-10",
    "TsName": "images",
    "TsUserId": "2172393",
    "_waiyutong_org_User_Id": "2172393",
    "_waiyutong_org_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5NGY5ODdkYy1jMmMwLTRjYTEtYmQ4NC01OGNkMmUzYjA0ZjMiLCJqdGkiOiI0NzQyMDA5MjQ1MmIzYzc4ODdjYzdmYTdjZDA5ZDkzM2Y4MGM1YWVkNWNlNDk0NjM2ODhlYTA5NmI1OTkzMTE1NzljMTQ2YTk4MWJhMGU3MyIsImlhdCI6MTY0NjYzODgxNi40OTg0NDgsIm5iZiI6MTY0NjYzODgxNi40OTg0NTEsImV4cCI6MTY3ODE3NDgxNi40OTQ1MTIsInN1YiI6IjIxNzIzOTMiLCJzY29wZXMiOlsicHJzIl19.QP_iDttPs_0gJvdAYYTiOdo7mA675KjpxxS_9-eIXxS8hrZO07zeoUmSZ2ZC3Yu5Pew7W0BdaT8DSZ5qJIkptIyxAjAWJ2tlgfY8J9do__pExUtl7MjaBB7PMdb0nPiQj11FEYNK82iHyYxMCq3YzRAoMf3cP-r4FVrZilPWoRMiUsCRffgPg2eN1bXDvSYJ7teEW0xspKDhRG4fUeQsuDd_DG5fj1T9dl1mENuuIiX1uVjZ_xCRSTqKi7SUQjOqLDq_9sfO-z7Cv4Pn5NdbONkg-veswYH9gcSps3UmQLV7eX9Heb9UjBQiufm7uyf8PdWiFXN5lliNhqAtPGApZELQ84ZxrW1cUxawJBaYgCWcROnyXJTxJdxyXS8nj2gVM61nqhKZYX2Uw011hOhnZvvoDEjKndTYUTDXIGiwxEjq6P5l18jCDCP_X4APWRwToNVGJdXEM8rDagTFrIB71pduOSmxKx3rLDuYMbbEo8yk90ts3IvIoWwsMlJibplpvi7UHmbOy81_374gDW2KGW5NUC8lR_XfAivwLE3E_SOi1n5TEq4VufApF2JWHezi3s26_yRxjg7riHcV3CBg-uzPuaiEFG_DhvjyHnxlnei8HBhD_m7QGHJn1lb7J8u52lN8sBHfOdGagj46nXOhMB5i2ZLCj_Zfca3p4n-RcvA",
    "loginMethod": "web",
    "SERVERID": "ed0dace794fe68d19efd32ef9489c87e|1646638814|1646638814"
}

function dict2str(){
    let str = ''
    for (const key in upload_cookies){
        str += key + '=' + upload_cookies[key]
    }
    return str
}

const upload_headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'Connection': 'keep-alive',
    // 'Referer': 'https://www.waiyutong.org/',
    'X-Requested-With': 'XMLHttpRequest',
    'Sec-Fetch-Mode': 'cors',
    'Cookie':dict2str()
}

export {
  upload_url,upload_headers,upload_cookies
}