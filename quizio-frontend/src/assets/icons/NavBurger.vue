<template>
    <div class="navBurgerWrapper" @click='onClick'>
        <svg width="30" height="18" viewBox="0 0 30 18" fill="none" xmlns="http://www.w3.org/2000/svg">
        <rect x="4" width="22" height="4" rx="1" fill="black"/>
        <rect x="4" y="14" width="22" height="4" rx="1" fill="black"/>
        <rect y="7" width="30" height="4" rx="1" fill="black"/>
        </svg>
    </div>
</template>

<style lang='scss' scoped>
.navBurgerWrapper{
    display:none;
    cursor:pointer;
}
@media screen and (max-width:700px){
    .navBurgerWrapper{
        display:block;
    }
}
</style>

<script lang='ts'>
import {defineComponent} from 'vue'

export default defineComponent({
    props:{
        onClick:Function
    }
})
</script>