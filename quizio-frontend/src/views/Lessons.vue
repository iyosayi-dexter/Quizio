<template>
    <main class='filter'>
        <section class='lessons__filterWrapper'>
            <input type='text' placeholder='Search lesson...'/>

            <select>
                <option value='all'> All</option>
                <option value='web_3'>Web3</option>
            </select>

        </section>

        <section class='lessons__newest'>
            <h4> Newest Lessons </h4>
        </section>

        <section class='lessons__all'>
            <h4> Other Lessons </h4>
        </section>

    </main>
</template>

<script lang="ts">

import {defineComponent} from 'vue'

export default defineComponent({
    data(){
        return {

        }
    }
})


</script>
