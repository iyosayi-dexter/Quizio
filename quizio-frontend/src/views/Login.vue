<template>
    <NameDisplay/>
    <main class='auth'>

        <section class='auth__main'>
            <div class='auth__headerTextWrapper'>
                <h1>Login</h1>
                <p>Welcome back!</p>
            </div>
            <GoogleOAuth/>
            <form class='auth__form'>

                <div class='auth__formField'>
                    <label for='email'>Email</label>
                    <br/>
                    <input type='email'/>
                </div>

                <div class='auth__formField'>
                    <label for='password'>Password</label>
                    <br/>
                    <input type='password'/>
                </div>

                <div class='auth__passwordResetLinkWrapper'>
                    <router-link to='/password-reset'>
                        Forgot password?
                    </router-link>
                </div>
                <button type='submit' class='auth__submitBtn'>Login</button>
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

export default defineComponent({
    components:{
        NameDisplay,
        GoogleOAuth
    },
    data: function(){
        return {
            maker_launch
        }
    }
})
</script>
