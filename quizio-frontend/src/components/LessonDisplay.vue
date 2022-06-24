<template>
    <article class='lessonDisplay'>
        <router-link :to='`/lessons/${slug}/`' class='lessonDisplay__linkWrapper'>
            <img :src='thumbnail' :alt='topic' class='lessonDisplay__thumbnail'/>
            <div>
                <p class='lessonDisplay__topic'> {{topic}} </p>
                <p class='lessonDisplay__exert'> lorem ipsium dolor manad fadfn dfasdf asdf asdf asd fasdfa sdfansdf asd fasdfasdf adfasdf asdf asdf asdf asdf asdf asd fasda sd fa sdfasdf</p>
            </div>
        </router-link>
    </article>
</template>


<script lang='ts'>
import {defineComponent} from 'vue'

export default defineComponent({
    props: {
        topic:String,
        exert:String,
        thumbnail:String,
        date_created:String,
        slug:String
    },
})

</script>