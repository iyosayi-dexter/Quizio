<template>
    <NameDisplay/>
    <main class='auth'>

        <section class='auth__main'>
            <div class='auth__headerTextWrapper'>
                <h1>Signup</h1>
                <p>Join the community</p>
            </div>
            <GoogleOAuth/>
            <form class='auth__form'>

                <div class='auth__formField'>
                    <label for='email'>Email</label>
                    <br/>
                    <input type='email'/>
                </div>

                <div class='auth__formField'>
                    <label for='username'>Username</label>
                    <br/>
                    <input type='username'/>
                </div>

                <div class='auth__formField'>
                    <label for='password'>Password</label>
                    <br/>
                    <input type='password'/>
                </div>

                <div class='auth__formField'>
                    <label for='re_password'>Confirm Password</label>
                    <br/>
                    <input type='re_password'/>
                </div>

                <button type='submit' class='auth__submitBtn'>Signup</button>
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
