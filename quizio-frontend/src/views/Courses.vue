<template>
    <main class='tests'>
        <section class='test__filterWrapper'>
            <input type='text' placeholder='Search Tests...' v-model='test_search'/>
            <select v-model='option'>
                <option value='all'> All</option>
                <option value='web_3'>Web3</option>
            </select>
        </section>

        <section class='test__grid'>
            <Test v-for='course in courses' :slug='course.title' :image-url='course.thumbnail' :title='course.title' />
        </section>
    </main>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import Test from '../components/Test.vue'
import desert_landscape from '../assets/illustrations/desert_landscape.png'

export default defineComponent({
    data: function(){
        return {
            test_search:'',
            option:'All',
        }
    },
    computed: {
        courses: function(){
            return this.$store.state.lesson.courses
        }
    },
    components:{
        Test
    }
})
</script>
