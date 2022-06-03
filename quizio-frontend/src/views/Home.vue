<template>
    <section class='container'>

        <section class='container__itemWrapper'>
            <h1 class='container__largeText'>Welcome to <span class='container__appName'>Quizio</span></h1>

            <div class='container__linkWrapper'>
                <router-link  to='/test' class='container__link container --bgPrimary'>
                    Take a test
                </router-link>

                <router-link  to='/login' class='container__link container__link--bgFade'>
                    Login
                </router-link>
            </div>

        </section>

        <section class='container__imageWrapper'>
            <img :src='cover_image' alt='Cover Image'/>
        </section>

    </section>

    <IllustrationDisplay text='Test our your knowledge by' :illustration-path='professor' link-text='taking a test' class-list='container container--reverse' path='/tests'/>
    <IllustrationDisplay text='Track your progress from your interactive' :illustration-path='pie_graph' link-text='Dashboard' class-list='container' path='/dashboard'/>
    <IllustrationDisplay text='Become part of the community and learn with others' :illustration-path='chat'  class-list='container container--reverse'/>
    <IllustrationDisplay text='Browse through our vast catalogue of' :illustration-path='studying'  class-list='container' link-text='lessons' path='/lesson'/>

</template>

<script lang="ts">
import {defineComponent} from 'vue'
import IllustrationDisplay from '../components/IllustrationDisplay.vue'
import cover_image from '../assets/cover_image.svg'
import professor from '../assets/illustrations/professor.svg'
import pie_graph from '../assets/illustrations/pie_graph.svg'
import chat from '../assets/illustrations/chat.svg'
import studying from '../assets/illustrations/studying.svg'

    export default defineComponent({
        data: function(){
            return {
                cover_image,
                professor,
                pie_graph,
                chat,
                studying
            }
        },
        components: {
                IllustrationDisplay
        }
    })
</script>
