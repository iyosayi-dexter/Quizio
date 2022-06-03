import {createStore } from 'vuex'
import nav from './modules/nav'
import user from './modules/user'
import chat from './modules/chat'

const store = createStore({
    modules:{
        nav,
        chat,
        user
    },
})

export default store