import {createStore} from 'vuex'

export default createStore({
    state: {
        userdata_base: {
            user_id: 0,
            username: '',
            realName: '',
            aviator: '' || 'api_file/static/images/aviator_base.png',
            email: '',
            coins: 0,
            lv: 0,
            deadline: '',
            usertype: 0,
            isLogin: false,
            qd: '签到',
        },
        userdata: {
            user_id: 0,
            username: '',
            realName: '',
            aviator: '' || 'api_file/static/images/aviator_base.png',
            email: '',
            coins: 0,
            lv: 0,
            deadline: '',
            usertype: 0,
            isLogin: false,
            qd: '签到',
        },
        nowUrl: localStorage.nowUrl || '/home',
        loading: false
    },
    mutations: {
        changeUserInfo(state, payload) {
            for (let key in payload) {
                if (key in state.userdata) {
                    if (key === 'qd') {
                        if (payload[key] === false) {
                            state.userdata[key] = '签到'
                        } else {
                            state.userdata[key] = '已签到'
                        }
                    } else if (key === 'deadline') {
                        state.userdata[key] = payload[key].replace('T', ' ').split('.')[0]
                    } else if (key === 'aviator') {
                        state.userdata[key] = "api_file/" +　payload[key]
                    }else {
                        state.userdata[key] = payload[key]
                    }
                }
            }
            if (!state.userdata.isLogin) {
                state.userdata.isLogin = true
            }
        },
        deleteUserInfo(state) {
            state.userdata = state.userdata_base
        },
        upDataUrl(state, url) {
            state.nowUrl = url
            localStorage.nowUrl = url
        },
        loadingChange(state, payload) {
            state.loading = payload
        },
    },
    actions: {},
    modules: {}
})
