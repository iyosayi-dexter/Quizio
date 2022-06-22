<template>
    <article class='testComp' @click='changeRoute'>
        <div class='testComp__imageWrapper'>
            <img :src='imageUrl || desert_landscape' :alt='title'/>
        </div>
        <p class='testComp__title'> {{title}} </p>
    </article>
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
    props: {
        slug:String,
        imageUrl:String,
        title:String
    },
    methods: {
        changeRoute(){
            this.$router.push(`/tests/${this.slug}`)
        }
    }
})

</script>