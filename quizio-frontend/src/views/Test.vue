<template>
    <main class='test__page'>
        <section class='test__screen'>
            {{currentQuestion_question}}
        </section>
        <section class='test__options'>
            <div class='test__optionsWrapper'>
                <input name='question_option' type='radio' @click='()=>selectOption("A")' :checked='option_selected.A'/>
                <p>{{option_a}}</p>
            </div>
            <div class='test__optionsWrapper'>
                <input name='question_option' type='radio' @click='()=>selectOption("B")' :checked='option_selected.B'/>
                <p>{{option_b}}</p>
            </div>
            <div class='test__optionsWrapper'>
                <input name='question_option' type='radio' @click='()=>selectOption("C")' :checked='option_selected.C'/>
                <p>{{option_c}}</p>
            </div>
            <div class='test__optionsWrapper'>
                <input name='question_option' type='radio' @click='()=>selectOption("D")' :checked='option_selected.D'/>
                <p>{{option_d}}</p>
            </div>
        </section>

        <section class='test__controls'>
            <button @click='prevQuestion'>Prev</button>
            <button @click='submit'>Submit</button>
            <button @click='nextQuestion'>Next</button>
        </section>
    </main>


    <Transition name='modal-bounce'>
        <div class='test__confirmModal' v-if='showConfirmModal'>
            <p> Are you sure you want to submit? </p>
            <div class='test__confirmModalButtonContainer'>
                <button @click='closeModal'> Cancel </button>
                <button @click='(e)=> submit(e,true)'> Submit </button>
            </div>
        </div>
    </Transition>
    <div class='test__confirmModalOverlay' v-if='showConfirmModal'></div>

</template>

<script lang="ts">
import {defineComponent} from 'vue'
import {fetchQuestions, submitTest} from '../adapters/quiz'


export default defineComponent({
    data: function(){
        return {
            questions:[],
            users_answers:{},
            current_question_index:0,
            showConfirmModal:false
        }
    },
    created: async function(){
        const questions = await fetchQuestions(this.$route.query)
        this.questions = questions
    },
    computed: {
        currentQuestion: function(){
            const ques = this.questions[this.current_question_index]
            if (ques === undefined){
                return {}
            }
            return ques
        },

        currentQuestion_question: function(){
            return this.currentQuestion.question
        },

        option_a: function(){
            return this.currentQuestion.option_a
        },

        option_b: function(){
            return this.currentQuestion.option_b
        },

        option_c: function(){
            return this.currentQuestion.option_c
        },

        option_d: function(){
            return this.currentQuestion.option_d
        },

        option_selected: function(){
            const choice = this.users_answers[this.current_question_index]?.choice
            if(choice === undefined){
                return {
                    A:false,
                    B:false,
                    C:false,
                    D:false,
                }
            }
            return {
                A: choice === 'A',
                B: choice === 'B',
                C: choice === 'C',
                D: choice === 'D',
            }
        }

    },

    methods: {

        submit: async function(e,confirmed=false){
            if(confirmed){
                const course = this.$route.query.course?.toLowerCase()
                const mode = this.$route.query.mode?.toUpperCase()

                await submitTest(this.users_answers, course, mode)
                this.showConfirmModal = false
            }else {
                this.showConfirmModal = true
            }
        },

        selectOption: function(choice){
            this.users_answers = {...this.users_answers, [this.current_question_index]:{
                choice,
                id: this.currentQuestion.id
            }}
        },

        closeModal: function(){
            this.showConfirmModal= false
        },

        nextQuestion: function(){
            if( this.current_question_index+1 < this.questions.length ){
                this.current_question_index +=1
            }
        },

        prevQuestion: function(){
            if(this.current_question_index-1 >= 0){
                this.current_question_index -=1
            }
        },
    }


})

</script>
