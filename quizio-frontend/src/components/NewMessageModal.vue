<template>
    <main class='newMessageModal'>
        <header class='newMessageModal__header'>
            <h2>
                New Message
            </h2>
        </header>
        <div class='newMessageModal__searchField'>
            <label for='user_search'>icon</label>
            <input type='search' name='user_search' placeholder='Search Users'/>
        </div>
        <section v-for='user in users' class='newMessageModal__user'>
            <div class='newMessageModal__imgWrapper'>
                <img :src='user.profile_image === null ? desert_landscape: user.profile_image' :alt='user.user.username'/>
            </div>
            <div class='newMessageModal__userNameWrapper'>
                <p> {{user.user.username}} </p>
            </div>
        </section>
    </main>
</template>


<script lang='ts'>
import {defineComponent} from 'vue'
import desert_landscape from '../assets/illustrations/desert_landscape.png'

export default defineComponent({
    data(){
        return {
            desert_landscape
        }
    },
    methods: {
        setCurrentChatId:function (user){
            this.$store.commit('chat/setCurrentChatUserId',{id:user.id , username:user.username})
        }
    },
    computed: {
        users: function (){
            return this.$store.state.users
        }
    }
})

</script>