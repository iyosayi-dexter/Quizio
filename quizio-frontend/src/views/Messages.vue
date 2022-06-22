<template>

    <main class='messages'>
        <!-- messages section wrapper -->
        <section class='messages__chats'>
            <div class='messages__chatsHeader'>
                <h3> Messages </h3>
                <div class='message__newMessageIconWrapper' @click='toggleModal'>
                    <MsgIcon/>
                </div>
            </div>
            <input type='text' class='messages__search' placeholder='search message...' v-model='search'/>
            <div class='messages__chatsWrapper'>
                <Chats :search='search'/>
            </div>
        </section>
        <!-- end of message section -->

        <!-- chat section wrapper -->
        <section class='messages__chat messages__chat--overlay-for-small' v-if='currentChatUserId !== null'>
            <!-- chat header -->
            <div class='messages__chatHeader'>

                <div class='messages__toolBar'>
                    <small @click='collapseChat' class='messages__collapseChatIcon'>Back</small>
                    <p> {{currentChatUserId === user_id ? 'You' : currentChatUserUsename}} </p>
                </div>

                <div class='messages__iconWrapper' @click='toggleChatOptionVisibility'>
                    <Vector/>
                </div>

                <!-- Chat option overlay -->
                <div class='messages__chatOptionOverlay' @click='toggleChatOptionVisibility' v-if='chatOptionOpen'></div>
                <!-- Chat options -->
                <Transition name='options-bounce'>
                    <div class='messages__chatOptionsWrapper' v-if='chatOptionOpen'>
                        <ul>
                            <li class='messages__chatOption' @click='blockUser'> <AlertIcon/> Block User </li>
                            <li class='messages__chatOption' @click='deleteConversation'> <DeleteIcon/> Delete conversation</li>
                            <li class='messages__chatOption'><router-link to='user'><ProfileIcon/> View profile</router-link></li>
                            <li class='messages__chatOption' @click='toggleChallangeModal'> <ArrowProjectileMultiple/> Challange </li>
                        </ul>
                    </div>
                </Transition>
            </div>

            <!-- chat thread-> messages are shown here -->
            <div class='messages__threadWrapper'>
                <MessagesThread v-if='hasChats'/>
                <!-- <MessageEmptyState v-else/> -->
            </div>

            <!-- chat footer -->
            <div class='messages__chatFooter'>
                <div class='messages__picUploadWrapper'>
                    <input type='file' hidden id='image_upload' accept='image/*'/>
                    <div class='message__imageUpoadWrapper'>
                        <ImageUploadIcon for='image_upload'/>
                    </div>
                </div>
                <form @submit.prevent='sendMessage' class='mesages__sendMessageForm'>
                    <input placeholder='say something...' class="messages__messageField" v-model='message_text'/>

                    <div class='messages__sendBtnWrapper'>
                        <button><SendIcon/></button>
                    </div>
                </form>
            </div>
        </section>

        <!-- Shown when a chat is selected to be viewed -->
        <section v-else class='messages__chat messages__chat--center messages__chat--hide-for-small'>
            <div class='messages__defaultWrapper'>
                <p class='messages__defaultLargeText'>Select a message </p>
                <p class='messages__defaultSmallText'>Choose an existing conversation or start a new one</p>
                <button class='messages__selectNewBtn' @click='toggleModal'>New Message</button>
            </div>
        </section>
        <!-- end of chat section -->
        <NewMessageModal/>
        <ChallangeModal v-if='showChallangeModal' :hide-modal='toggleChallangeModal' slug='hello world' />
    </main>

</template>

<script lang="ts">
import {defineComponent} from 'vue'


/*
    Icons
*/
import Vector from '../assets/icons/Vector.vue'
import SendIcon from '../assets/icons/SendIcon.vue'
import ImageUploadIcon from '../assets/icons/ImageUploadIcon.vue'
import AlertIcon from '../assets/icons/Alert.vue'
import DeleteIcon from '../assets/icons/Delete.vue'
import ProfileIcon from '../assets/icons/Profile.vue'
import MsgIcon from '../assets/icons/MsgIcon.vue'
import ArrowProjectileMultiple from '../assets/icons/ArrowProjectileMultiple.vue'

/*
    Components
*/
import Chats from '../components/Chats.vue'
import MessagesThread from '../components/MessagesThread.vue'
import {message as messageInterface} from '../store/modules/chat'
import {getCurrentDateTime} from '../utils/date'
import NewMessageModal from '../components/NewMessageModal.vue'
import MessageEmptyState from '../components/MessageEmptyState.vue'
import ChallangeModal from '../components/ChallangeModal.vue'


export default defineComponent({
    data: function(){
        return {
            chatOptionOpen:false,
            message_text:'',
            attachments:null,
            search:'',
            showChallangeModal:false,
        }
    },
    computed:{
        currentChatUserId(){
            return this.$store.state.chat.currentChatUserId
        },
        currentChatUserUsename(){
            return this.$store.state.chat.currentChatUserUsername
        },
        user_id(){
            return this.$store.state.user.id
        },
        hasChats(){
            return this.$store.state.chat.messages.length > 0 ? true: false
        }
    },
    methods: {
        toggleChatOptionVisibility:function(){
            this.chatOptionOpen = !this.chatOptionOpen
        },
        blockUser:function(){
            console.log('blocking user!!!')
        },
        deleteConversation: function(){
            console.log('deleting conversation')
        },
        toggleChallangeModal:function(){
            this.showChallangeModal = !this.showChallangeModal
        },
        toggleModal(){
            this.$store.commit('users/toggleModal')
        },
        collapseChat(){
                this.$store.commit('chat/closeChat');
        },
        sendMessage(){
            if (this.message_text.trim() !== '' | (this.attachments !== null && this.attachments.length>0)){
                let sender={
                        id:this.$store.state.user.id,
                        username:this.$store.state.user.username
                }
                let receiver = {
                    id:this.currentChatUserId,
                    username:this.currentChatUserUsename
                }
                let new_message = {
                    receiver,
                    text:this.message_text,
                    attachments:this.attachments,
                    seen:false,
                    date_sent:getCurrentDateTime()
                }
                if(sender.id === receiver.id){
                    new_message.seen = true
                }
                this.$store.commit('socket/send',new_message)
                this.message_text=''
            }

        }
    },
    // mounted(){
    //     if(this.$store.state.user.is_authenticated !== true){
    //         this.$router.push('/login?next=messages')
    //     }
    // },
    components:{
        Chats,
        MessagesThread,
        Vector,
        SendIcon,
        ImageUploadIcon,
        AlertIcon,
        DeleteIcon,
        ProfileIcon,
        MsgIcon,
        NewMessageModal,
        MessageEmptyState,
        ArrowProjectileMultiple,
        ChallangeModal
    }
})

</script>
