<template>
    <main class='leaderboard'>
        <section class='leaderboard__header'>
            <h1> Leaderboard,</h1>
            <small class='leaderboard__smallText'>Top xp scorers</small>
        </section>
        <section class='leaderboard__users'>

            <article class='leaderboard__userWrapper' v-for='user in users'>
                <div class='leaderboard__userProfileWrapper'>
                    <img :src='desert_landscape' :alt='user.user.username' class='leaderboard__userProfileImage'/>
                    <p class='leaderboard__userUsername'>{{user.user.username}}</p>
                </div>
                <p class='leaderboard__userXp'>
                        {{user.xp}}xp
                </p>
            </article>

        </section>
    </main>
</template>

<script lang='ts'>
import {defineComponent} from 'vue'
import desert_landscape from '../assets/illustrations/desert_landscape.png'

export default defineComponent({
    data: function(){
        return {
            desert_landscape
        }
    },
    computed:{
        users: function(){
            return this.$store.state.users.all
        }
    }
})

</script>