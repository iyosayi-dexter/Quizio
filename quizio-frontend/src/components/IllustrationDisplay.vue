<template>
    <section :class='classList'>
        <div class='container__item'>
            <p>{{text}}<router-link v-if="linkText" :to='path' class='container__link --colorPrimary'>{{linkText}}</router-link></p>
        </div>

        <div class='container__illustrationWraper'>
            <img :src='illustrationPath' :alt='text'/>
        </div>
    </section>
</template>


<script lang='ts'>
import {defineComponent} from 'vue'

export default defineComponent({
    props:{
        text:String,
        path:String,
        linkText:String,
        classList:String,
        illustrationPath:String
    }
})
</script>