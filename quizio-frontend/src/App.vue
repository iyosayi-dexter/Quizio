<template>
    <Header/>
    <router-view/>
</template>

<style lang='scss'>
    @import './assets/styles/index.scss';
</style>

<script lang='ts'>
import {defineComponent} from 'vue'
import Header from './components/Header.vue'

export default defineComponent({
    components:{
        Header
    }
})

</script>