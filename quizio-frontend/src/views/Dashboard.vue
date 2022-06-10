<template>

    <section class='dashboard__topSection'>

        <!--<div class='dashboard__utils'>
            <ul>
                <li> <router-link to='/messages'> Chat </router-link> </li>
                <li> <router-link to='/settings'> Edit profile </router-link> </li>
                <li @click='logout' class='dashboard__logoutBtn'> Logout </li>
            </ul>
        </div>-->

        <div class='dashboard__user'>
            <div class='dashboard__text'>
                <img src='' class='dashboard__userProfilePic'/>
                <div class='dashboard__messageWrapper'>
                    <p> Hi <span class='dashboard__userUsername'>{{user_username}},</span></p>
                    <small class='dashboard__message'>Welcome to your dashboard</small>
                </div>
            </div>
            <div class='dashboard__illustrationWrapper'>
                <img :src='pie_graph' alt='Pie Graph'/>
            </div>
        </div>

        <div>

        </div>
    </section>

    <section>
        <h3 class='dashboard__progess'> Progress Over Time</h3>

        <div class='dashboard__dataFilterWrapper'>
            <select class='dashboard__dataFilter'>
                <option value='basic'>Basic</option>
                <option value='medium'>Medium</option>
                <option value='hard'>Hard</option>
            </select>
            <select class='dashboard__dataFilter'>
                <option value='today'>today</option>
                <option value='All_time'>All time</option>
                <option value='one_week'>1 week</option>
            </select>
        </div>

        <div class='dashboard__graphWrapper'>
        </div>

    </section>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import pie_graph from '../assets/illustrations/pie_graph.svg'

export default defineComponent({
    data: function(){
        return {
            pie_graph
        }
    },
    computed:{
        user_username(){
            return this.$store.state.user.username
        }
    },
    methods:{
        logout:function (){
            console.log('loggin out')
        }
    }
})

</script>