<template>
    <section class='chat__message' v-for='message in messages' @click='()=>setCurrentChatId(message.sender, message.receiver)'>
        <div class='chat__userWrapper'>
            <img :src='desert_landscape' :alt='message.sender.id === user_id ? message.receiver.username : message.sender.username' class='chat__userProfilePic'/>
            <small class='chat__unread' v-if='message.sender.id !== user_id && countUnread(message.sender, message.receiver)>0'>{{countUnread(message.sender , message.receiver)}}</small>
        </div>
        <div class='chat__textWrapper'>
            <p class='chat__user' v-if='message.sender.id === user_id && message.receiver.id === user_id'>You</p>
            <p class='chat__user' v-else>{{message.sender.id === user_id ? message.receiver.username : message.sender.username}}</p>
            <p class='chat__mostRecentMessage'>{{message.text.length > 15 ? `${message.text.slice(0,15)}...`: message.text}}</p>
        </div>
    </section>
</template>


<script lang='ts'>
import {defineComponent} from 'vue'
import desert_landscape from '../assets/illustrations/desert_landscape.png'



export default defineComponent({
    data(){
        return{
            desert_landscape
        }
    },
    props:{
        search:String
    },
    computed:{
        /*
        * @returns latest uqniue chats
        */
        messages(){
            // latest unqiue: an array containing only unique message threads
            let latest_unique = []
            const messages = this.$store.state.chat.messages

            messages.forEach((message , index)=>{
                // first message is added on
                if(index === 0){
                    latest_unique = latest_unique.concat(message);
                    return;
                }

                let _exists = false

                /*
                * @notice Checks if a message by this user alredy exists in latest unqiue
                */
                latest_unique.forEach((item)=>{
                    /*
                    * @notice when a user sends a note to self
                    */
                    if(message.sender.id === this.user_id && message.receiver.id === this.user_id){
                        /*
                        * @notice checks if a note to self alreay exists in latest unque
                        */
                        const self_notes = latest_unique.filter(message => message.sender.id == this.user_id && message.receiver.id === this.user_id)
                        if(self_notes.length === 0){
                            latest_unique = latest_unique.concat(message);
                        }
                    }

                    /*
                        * @notice When its not a note to self
                    */
                    if(message.sender.id === this.user_id){
                        if(message.receiver.id === item.receiver.id | message.receiver.id === item.sender.id){
                            _exists = true
                        }
                    }else if(message.sender.id === item.receiver.id | message.sender.id === item.sender.id){
                            _exists = true
                    }

                })

                // adds a new unique message thread
                if(_exists === false){
                    latest_unique = latest_unique.concat(message);
                }

            })

            /*
            * @notice filtering messages based on search term
            */
            if(this.search.trim() !==''){
                return latest_unique.filter(message=>{
                    if(message.sender.id === this.user_id){
                        return message.receiver.username.includes(this.search)
                    }else{
                        return message.sender.username.includes(this.search)
                    }
                })
            }

            /*
            * @returns latest unique messages when no search term is applied
            */
            return latest_unique
        },
        user_id(){
            return this.$store.state.user.id
        },
        token(){
            return this.$store.state.user.tokens.access
        }
    },
    methods:{
        /*
        * notice sets the current chat when the user click on a chat
        */
        setCurrentChatId(sender , receiver){
            const token = this.token
            if(sender.id === this.user_id){
                this.$store.commit('chat/setCurrentChatUserId',{id:receiver.id , username:receiver.username})
                if(receiver.id !== this.user_id){
                    this.$store.commit('chat/markAsRead',{user:receiver , token})
                }
                return
            }
            this.$store.commit('chat/setCurrentChatUserId',{id:sender.id , username:sender.username})
            if(sender.id !== this.user_id){
                this.$store.commit('chat/markAsRead',{user:sender,token})
            }
        },

        /*
        * @returns the number of unread messages
        */
        countUnread(sender , receiver){
            const messages = this.$store.state.chat.messages
            if(sender.id === this.user_id){
                // sender === current logged in user -> return a length of messages seen based on the receiver's id
                return messages.filter(message => message.sender.id !== this.user_id && (message.sender.id === receiver.id | message.receiver.id === receiver.id) && message.seen===false).length
            }
            // sender !== current logged in user -> return a length of messages seen based on the sender's id
            else return messages.filter(message => message.sender.id !== this.user_id && (message.sender.id === sender.id | message.receiver.id === sender.id) && message.seen===false).length
        },

    }

})

</script>