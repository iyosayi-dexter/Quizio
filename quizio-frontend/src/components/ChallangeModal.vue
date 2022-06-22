<template>

    <main class='challangeModal'>

        <!-- Current Step container -->
        <section class='challamgeModal__stepMangerWrapper'>
            <div @click='()=> setCurrentStepIndex(0)' class='challamgeModal__stepWrapper'>

                <CheckOutline v-if='courseSelected' color='#174517'/>
                <Check v-else/>

                <small  :class='isActiveStep(0)'> Select a course </small>
            </div>

            <div @click='()=> setCurrentStepIndex(1)' class='challamgeModal__stepWrapper'>
                <CheckOutline v-if='challangerSelected' color='#174517'/>
                <Check v-else/>
                <small :class='isActiveStep(1)'> Select a challanger </small>
            </div>
        </section>
        <!-- End of container-->

        <!-- Step main-->
        <section class='challangeModal__stepsWrapper'>
            <article v-if='step_index===0' class='challangeModal__courses'>
                <div v-for='course in courses' :class='isSelectedCourse(course)' @click='()=>setCourse(course)'>
                    <img :src='course.thumbnail || desert_landscape'/>
                    <p>{{course.title}}</p>
                </div>
            </article>

            <article v-if='step_index===1' class='challangeModal__users' >
                <div v-for='user in users'
                    :class="isSelectedUser(user)"
                    @click='()=>setChallanger(user)'>

                    <img :src='user.profile_image || desert_landscape'/>
                    <p>{{user.user.username}}</p>
                </div>
            </article>
        </section>
        <!-- end of step main -->

        <section class='challangeModal__btnWrapper'>
            <button class='challangeModal__btn' @click='createChallange'>
                Start Challange!
            </button>
        </section>

    </main>

    <div class='challangeModal__overlay' @click='hideModal'></div>
</template>


<script lang='ts'>
import {defineComponent} from 'vue'
import desert_landscape from '../assets/illustrations/desert_landscape.png'

/*
* Icon imports
*/
import Check from '../assets/icons/Check.vue'
import CheckOutline from '../assets/icons/CheckOutline.vue'

/*
* Adapters
*/
import {sendChallange} from '../adapters/quiz'

export default defineComponent({
    data: function(){
        return {
            step_index:0,
            challanger:{},
            course:{},
            desert_landscape
        }
    },
    computed:{
        courses: function(){
            return this.$store.state.lesson.courses
        },

        users: function(){
            return this.$store.state.users.all
        },
        challangerSelected: function(){
            const hasUsername = this.challanger.username !== undefined
            const hasId = this.challanger.id !== undefined
            const isCorrectLength = Object.keys(this.challanger).length === 2
            return hasUsername && hasId && isCorrectLength
        },
        courseSelected : function(){
            const hasTitle = this.course.title !== undefined
            const hasId = this.course.id !== undefined
            const isCorrectLength = Object.keys(this.course).length === 2
            return hasTitle && hasId && isCorrectLength
        }
    },
    mounted: function (){
        const current_chat_user_id = this.$store.state.chat.currentChatUserId
        const current_chat_user_username = this.$store.state.chat.currentChatUserUsername
        if(current_chat_user_username === null || current_chat_user_id == null){
            return
        }
        this.challanger={username:current_chat_user_username, id:current_chat_user_id }
    },
    methods: {
        isActiveStep: function(step_index:number): string{
            return step_index ===this.step_index ? "--active_step" : ''
        },
        setCurrentStepIndex: function(step_index:number){
            this.step_index = step_index
        },
        setCourse: function(course){
            const {title , id } = course
            this.course = {title , id}
        },
        setChallanger: function(challanger){
            const {user} = challanger
            this.challanger = user
        },
        createChallange: async function(){
            const token = this.$store.state.user.tokens.access
            if(this.courseSelected && this.challangerSelected){
                const res = await sendChallange(this.course, this.challanger, token)
            }
        },
        isSelectedUser: function(challanger){
            const {user} = challanger
            if(this.challanger.username === user.username && this.challanger.id == user.id){
                return 'challangeModal__user challangerModal__user--selected'
            }
            return 'challangeModal__user'
        },
        isSelectedCourse: function(course){
            const {title , id} = course
            if(this.course.title === title && this.course.id == id){
                return 'challangeModal__course challangeModal__course--selected'
            }
            return 'challangeModal__course'
        }
    },
    props: {
        slug:String,
        hideModal:Function,
    },
    components: {
        Check,
        CheckOutline
    }
})

</script>