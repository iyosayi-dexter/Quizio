<template>
    <Header/>
    <router-view/>
</template>

<style lang='scss'>
    @import './styles/index.scss';
</style>

<script lang='ts'>
import {defineComponent} from 'vue'
import Header from './components/Header.vue'
import {loadMessages} from './adapters/chat'
import {fetchUsers} from './adapters/auth'
import {fetchCourses} from './adapters/lesson'


export default defineComponent({
    components:{
        Header
    },
    computed: {
        token: function(){
            return this.$store.state.user.tokens?.access
        },
        socket: function(){
            return this.$store.state.socket.connection
        }
    },
    watch:{
        token:function(newToken){
            if(newToken !== null && newToken.trim() !==''){
                this.load_messages(newToken)
                this.fetch_users(newToken)
                this.connect_socket(newToken)
            }
        }
    },
    created:async function(){
        const res = await fetchCourses()
        this.$store.commit('lesson/setCourses', res)
    },
    methods: {
        relay_message: function(message){
            this.$store.commit('chat/appendMessage', JSON.parse(message))
        },
        fetch_users:async function(token){
            const users = await fetchUsers(token)
            this.$store.commit('users/setUsers', users)
        },
        load_messages:async function(token){
            const messages = await loadMessages(token)
            this.$store.commit('chat/updateMessages', messages)
        },
        connect_socket: function(token){
            this.$store.commit('socket/connect', {token , callback:this.relay_message})
        }
    }
})

</script>