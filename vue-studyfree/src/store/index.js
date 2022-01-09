import {createStore} from 'vuex'

export default createStore({
    state: {
        userdata: {
            username: '',
            realName: '',
            aviator:'',
            coins: 0,
            usertype: 0,
            isLogin: false
        }
    },
    mutations: {
        changeUserInfo(state, payload) {
            for (let key in payload) {
                if (key in state.userdata) {
                    state.userdata[key] = payload[key]
                }
            }
            if (!state.userdata.isLogin){
                state.userdata.isLogin = true
            }
        },
        deleteUserInfo(state) {
            state.userdata = {
                username: '',
                realName: '',
                aviator:'',
                coins: 0,
                usertype: 0,
                isLogin: false
            }
        }
    },
    actions: {},
    modules: {}
})
