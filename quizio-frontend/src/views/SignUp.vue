<template>
    <main class='auth'>

        <section class='auth__main'>
            <div class='auth__headerTextWrapper'>
                <h1>Signup</h1>
                <p>Join the community</p>
            </div>
            <GoogleOAuth/>
            <form class='auth__form' @submit.prevent='signup'>

                <div class='auth__formField'>
                    <label for='email'>Email</label>
                    <br/>
                    <input required type='email' v-model='email'/>
                </div>

                <div class='auth__formField'>
                    <label for='username'>Username</label>
                    <br/>
                    <input required type='username' v-model='username'/>
                </div>

                <div class='auth__formField'>
                    <label for='password'>Password</label>
                    <br/>
                    <input required type='password' v-model='password'/>
                </div>

                <div class='auth__formField'>
                    <label for='re_password'>Confirm Password</label>
                    <br/>
                    <input required type='password' name='re_password' v-model='re_password'/>
                </div>

                <button type='submit' :class='submitBtnClass'>{{btnInnerText}}</button>
                <div class='auth__footer'>
                    Already have an account? <router-link to='/login' class='--colorPrimary'>Login</router-link>
                </div>
            </form>
        </section>

        <aside class='auth__aside'>
            <div class='auth__headerTextWrapper'>
                <h1>Welcome to Quizio</h1>
                <p>Get started by creating your account</p>
            </div>
            <img :src='maker_launch' alt='Login to your account'/>
        </aside>

    </main>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import NameDisplay from '../components/NameDisplay.vue'
import GoogleOAuth from '../components/GoogleOAuth.vue'
import maker_launch from '../assets/illustrations/maker_launch.svg'
import {signupRequest} from '../adapters/auth'

export default defineComponent({
    components:{
        NameDisplay,
        GoogleOAuth,

    },
    data: function(){
        return {
            maker_launch,
            username:'',
            email:'',
            password:'',
            re_password:'',
            loading:false
        }
    },
    methods: {
        async signup(){
            if(this.loading){
                return
            }
            this.loading = true
            const body = {
                email:this.email,
                password:this.password,
                re_password:this.re_password,
                username:this.username
            }
            // await const success = await signupRequest(body)
            this.loading = false

        },
    },
    computed: {
        submitBtnClass(){
            return `auth__submitBtn auth__submitBtn--loading-${this.loading}`
        },
        btnInnerText(){
            return this.loading ? 'Loading...' : 'Signup'
        }
    }
})
</script>
