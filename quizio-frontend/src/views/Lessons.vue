<template>
    <main class='filter'>
        <section class='lessons__filterWrapper'>
            <input type='text' placeholder='Search lesson...'/>

            <select>
                <option value='all'> All</option>
                <option value='web_3'>Web3</option>
            </select>

        </section>

        <section class='lessons__section'>
            <h4 class='lesson__sectionHeader'> Newest Lessons </h4>
            <div class='lessons__wrapper'>
                <LessonDisplay v-for='lesson in newest_lessons'
                :topic='lesson.topic'
                :course='lesson.course'
                :thumbnail='lesson.thumbnail'
                :slug='lesson.slug'
                :date_created='lesson.date_created'
                />
            </div>
        </section>

        <section class='lessons__section'>
            <h4 class='lesson__sectionHeader'> Other Lessons </h4>
            <div class='lessons__wrapper'>
                <LessonDisplay v-for='lesson in others'
                :topic='lesson.topic'
                :exert='lesson.exert'
                :thumbnail='lesson.thumbnail'
                :slug='lesson.slug'
                :date_created='lesson.date_created'
                />
            </div>
        </section>

    </main>
</template>

<script lang="ts">

import {defineComponent} from 'vue'
import LessonDisplay from '../components/LessonDisplay.vue'
import desert_landscape from '../assets/illustrations/desert_landscape.png'

export default defineComponent({
    computed: {
        newest_lessons: function(){
            return this.$store.state.lesson.lessons.slice(0,4)
        },
        others: function(){
            return this.$store.state.lesson.lessons.slice(4,)
        }
    },
    components:{
        LessonDisplay
    }
})


</script>
