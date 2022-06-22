<template>
        <section>
            <div class='lesson__imageWrapper'>
                <img :src='lesson_image_url' :alt='title'/>
            </div>
            <div>
                <p> {{title}} </p>
            </div>
        </section>

</template>

<script>
import {defineComponent} from 'vue'

export default defineComponent({
    props:{
        title:String,
        lesson_image_url:String
    }

})

</script>