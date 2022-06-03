<template>
    <div class='message' v-for='message in messages.slice().reverse()' :class='message.sender.id === user_id? "message--right" : "message--left" '>
        <p class='message__text'> {{message.text}} </p>
        <small class='message__date'> {{message.date}} </small>
    </div>
</template>

<script lang='ts'>
import {defineComponent} from 'vue'

export default defineComponent({
    computed:{
        messages(){
            const messages = this.$store.state.chat.messages
            const currentChatUserId = this.$store.state.chat.currentChatUserId

            if(currentChatUserId === this.user_id){
                return messages.filter(message => message.sender.id === this.user_id && message.receiver.id === this.user_id)
            }else return messages.filter(message => message.sender.id === currentChatUserId | message.receiver.id === currentChatUserId)

        },
        user_id(){
            return this.$store.state.user.id
        }
    },
})

</script>