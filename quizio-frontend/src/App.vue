<template>
    <Header/>
    <router-view/>
</template>

<style lang='scss'>
    @import './assets/styles/index.scss';
</style>

<script lang='ts'>
import {defineComponent} from 'vue'
import Header from './components/Header.vue'
import {loadMessages} from './adapters/chat'


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
        token: async function(newToken){
            if(newToken !== null && newToken.trim() !==''){
                const messages = await loadMessages(newToken)
                this.$store.commit('chat/updateMessages', messages)
                this.$store.commit('socket/connect', {token:newToken , callback:this.relayMessage})
            }
        }
    },
    methods: {
        relayMessage: function(message){
            console.log(JSON.parse(message))
            this.$store.commit('chat/appendMessage', JSON.parse(message))
        }
    }
})

</script>