import {createStore } from 'vuex'
import nav from './modules/nav'
import user from './modules/user'
import chat from './modules/chat'
import users from './modules/users'
import socket from './modules/socket'

const store = createStore({
    modules:{
        nav,
        chat,
        user,
        users,
        socket
    },
})

export default store