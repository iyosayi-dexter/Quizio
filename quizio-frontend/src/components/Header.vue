<template>
    <header class='header'>
        <NameDisplay/>
        <Nav/>
    </header>
</template>

<script lang='ts'>
import {defineComponent} from 'vue'

import Nav from './Nav.vue'
import NameDisplay from './NameDisplay.vue'

export default defineComponent({
    components:{
        Nav,
        NameDisplay
    }
})

</script>
