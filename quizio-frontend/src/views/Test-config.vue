<template>
    <main class='testConfig'>
        <h1 class='testConfig__testName'>{{test}} Test</h1>
    </main>

    <section class='testConfig__mainWrapper'>
        <form class='testConfig__form' @submit.prevent='handleSubmit'>
            <div class='testConfig__field'>
                <label for='duration'>Duration</label>
                <select v-model='dur'>
                    <option value='5_mins'>5 Mins</option>
                    <option value='30_mins'>30 Mins</option>
                    <option value='1_hr'>1 Hour</option>
                </select>
            </div>

            <div class='testConfig__field'>
                <label for='mode'>Mode</label>
                <select v-model='mode'>
                    <option value='basic'>Basic</option>
                    <option value='medium'>Medium</option>
                    <option value='hard'>Hard</option>
                </select>
            </div>

            <div class='testConfig__field'>
                <label for='mode'>Number of Questions</label>
                <select v-model='nques'>
                    <option value='5'>5</option>
                    <option value='25'>25</option>
                    <option value='40'>40</option>
                    <option value='60'>60</option>
                </select>
            </div>
            <button class='testConfig__submitBtn'> Start Test </button>
        </form>

        <div class='testConfig__illustrationWrapper'>
            <p><b> Take a test </b></p>
            <p>Configure your test</p>
            <img :src='exam' alt='Take a test'/>
        </div>
    </section>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import exam from '../assets/illustrations/exams.svg'

export default defineComponent({
    data: function(){
        return {
            exam,
            dur:'',
            mode:'',
            nques:''
        }
    },
    computed: {
        test: function(){
            return this.$route.params.test
        }
    },
    methods:{
        handleSubmit: function(){
            this.$router.push(`/test?course=${this.test}&dur=${this.dur}&mode=${this.mode}&nques=${this.nques}`)
        }
    }
})

</script>
