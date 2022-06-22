import {createStore } from 'vuex'
import nav from './modules/nav'
import user from './modules/user'
import chat from './modules/chat'
import users from './modules/users'
import socket from './modules/socket'
import lesson from './modules/lesson'

const store = createStore({
    modules:{
        nav,
        chat,
        user,
        users,
        socket,
        lesson
    },
})

export default store