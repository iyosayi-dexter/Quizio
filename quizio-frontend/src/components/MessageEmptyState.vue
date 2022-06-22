<template>
    // <img :src='location_search' alt='No messages yet'/>
    <small> You currently don't have any messages </small>
</template>

<script lang='ts'>
import {defineComponent} from 'vue'
import location_search from '../assets/illustrations/location_search.svg'

export default defineComponent({
    data: function(){
        return {
            location_search
        }
    }
})
</script>

<style lang='scss' scoped>
img {
    border:1px solid red;
}
small {
    font-size:3000rem;
}
</style>