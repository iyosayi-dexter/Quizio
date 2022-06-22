<template>
    <main class='newMessageModal' v-if='showModal'>
        <header class='newMessageModal__header'>
            <div class='newMessageModal__iconWrapper' @click='toggleModal'>
                <CloseIcon/>
            </div>
            <h2>
                New Message
            </h2>
        </header>
        <div class='newMessageModal__searchField'>
            <label for='user_search'><SearchIcon/></label>
            <input type='text' name='user_search' placeholder='Search Users...' v-model='search'/>
        </div>
        <section v-for='user_profile in users' class='newMessageModal__user' @click='()=>setCurrentChatId(user_profile.user)'>
            <div class='newMessageModal__imgWrapper'>
                <img :src='user_profile.profile_image === null ? desert_landscape: user_profile.profile_image' :alt='user_profile.user.username'/>
            </div>
            <div class='newMessageModal__userNameWrapper'>
                <p> {{user_profile.user.username}} </p>
            </div>
        </section>
    </main>
    <div class='newMessageModal__overlay' @click='toggleModal' v-if='showModal'></div>
</template>


<script lang='ts'>
import {defineComponent} from 'vue'
import desert_landscape from '../assets/illustrations/desert_landscape.png'
import CloseIcon from '../assets/icons/Close.vue'
import SearchIcon from '../assets/icons/Search.vue'

export default defineComponent({
    data(){
        return {
            desert_landscape,
            search:'',
        }
    },
    methods: {
        setCurrentChatId:function (user){
            this.$store.commit('chat/setCurrentChatUserId',{id:user.id , username:user.username})
            this.$store.commit('users/toggleModal')
        },
        toggleModal: function(){
                this.$store.commit('users/toggleModal')
        }
    },
    computed: {
        users: function (){
            const users_store = this.$store.state.users.all
            if(this.search.trim() !==''){
                return users_store.filter(user_profile => user_profile.user.username.includes(this.search))
            }
            return users_store
        },
        showModal: function(){
            return this.$store.state.users.show_users_modal
        }
    },
    components: {
        CloseIcon,
        SearchIcon
    }
})

</script>