<template>
    <main>
        <h1> {{lesson?.topic}} </h1>
        <img :src='lesson?.thumbnail' :alt='lesson?.topic'/>
        <div v-html="lesson?.content" />
    </main>

</template>

<script lang='ts'>
import {defineComponent} from 'vue'
import {fetchLessonDetail} from '../adapters/lesson'
import desert_landscape from '../assets/illustrations/desert_landscape.png'

export default defineComponent({
    data: function(){
        return {
            lesson:{}
        }
    },
    created:async  function(){
        const slug = this.$route.params?.slug
        const {is404 , data} = await fetchLessonDetail(slug)
        if(is404){

        }else {
            this.lesson = data
        }
    }
})

</script>