<template>
    <Transition name='nav'>
    <nav class='nav'>
        <ul class='nav__list'>
            <li class='nav__listItem'><router-link to='/'> Home </router-link> </li>
            <li class='nav__listItem'><router-link to='/leaderboard'> Leaderboard </router-link> </li>
            <li class='nav__listItem'><router-link to='/dashboard'> Dashboard </router-link> </li>
            <li class='nav__listItem'><router-link to='/messages'> Chats </router-link> </li>
            <li class='nav__listItem'><router-link to='/lessons'> Lessons </router-link> </li>
            <li class='nav__listItem'><router-link to='/courses'> Take a test </router-link> </li>
        </ul>
    </nav>
    </Transition>
</template>

<script lang='ts'>
import {defineComponent} from 'vue'
export default defineComponent({
    data(){
        return {
        }
    },
    computed:{

    }
})
</script>