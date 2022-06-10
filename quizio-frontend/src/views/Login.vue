<template>
    <main class='auth'>

        <section class='auth__main'>
            <div class='auth__headerTextWrapper'>
                <h1>Login</h1>
                <p>Welcome back!</p>
            </div>
            <GoogleOAuth/>
            <form class='auth__form' @submit.prevent='login'>

                <div class='auth__formField'>
                    <label for='email'>Email</label>
                    <br/>
                    <input type='email' v-model='email' required/>
                </div>

                <div class='auth__formField'>
                    <label for='password'>Password</label>
                    <br/>
                    <input type='password' v-model='password' required/>
                </div>

                <div class='auth__passwordResetLinkWrapper'>
                    <router-link to='/password-reset'>
                        Forgot password?
                    </router-link>
                </div>
                <button type='submit' :class='submitBtnClass'>{{btnInnerText}}</button>
                <div class='auth__footer'>
                    Don't have an account? <router-link to='/signup' class='--colorPrimary'>Create Account</router-link>
                </div>
            </form>
        </section>

        <aside class='auth__aside'>
            <div class='auth__headerTextWrapper'>
                <h1>Welcome back</h1>
                <p>Login to your account</p>
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
import {loginRequest} from '../adapters/auth'

export default defineComponent({
    components:{
        NameDisplay,
        GoogleOAuth
    },
    data: function(){
        return {
            maker_launch,
            email:'',
            password:'',
            loading:false
        }
    },
    methods: {

        async login(){
            if(this.loading){
                return
            }

            this.loading = true
            const credentials = {
                email:this.email,
                password:this.password
            }

            const data = await loginRequest(credentials)
            if(Object.keys(data).length === 2){
                await this.$store.commit('user/set_user' , data)
                this.$router.push('/dashboard')
            }
            this.loading= false
        }
    },
    mounted: function (){
        if(this.$store.state.user.is_authenticated === true ){
            this.$router.push('/dashboard')
        }
    },
    computed:{
        submitBtnClass(){
            return `auth__submitBtn auth__submitBtn--loading-${this.loading}`
        },
        btnInnerText(){
            return this.loading ? 'Loading...' : 'Login'
        }
    }
})
</script>
