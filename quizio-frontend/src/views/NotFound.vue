<template>
    <main class='notfound__wrapper'>
        <section class='notfound__illustrationWrapper'>
            <img :src='location_search' alt='404 Not found'/>
        </section>
        <section class='notfound__textWrapper'>
            <h1> 404 </h1>
            <p> We're sorry we could not find the page you were looking for :( </p>
            <router-link class='--colorPrimary' to='/'>Back to home</router-link>
        </section>
    </main>
</template>

<script lang='ts'>
import {defineComponent} from 'vue'
import location_search from '../assets/illustrations/location_search.svg'

export default defineComponent({
    data: function(){
        return {
            location_search
        }
    }
})

</script>

<style scoped lang='scss'>
.notfound__wrapper{
    display:flex;
    justify-content:space-around;
    align-items:center;
    margin:2rem auto;
    padding:2rem;
}
.notfound__illustrationWrapper img {
    max-width:70%;
}
.notfound__textWrapper{
    width:fit-content;
}
.notfound__textWrapper h1 {
    font-size:10rem;
}
.notfound__textWrapper p {
    font-size:.8rem;
    color: rgba(black,.5);
    margin:.7rem auto;
}
.notfound__textWrapper a {
    text-decoration:none;
    font-weight:bolder;

    width:inherit;
}
@media screen and (max-width:700px){
    .notfound__wrapper{
        flex-direction:column;
    }
    .notfound__illustrationWrapper{
        text-align:center;
    }
    .notfound__textWrapper{
        h1{
            font-size:6rem;
            text-align:center;
        }
    }
}
</style>