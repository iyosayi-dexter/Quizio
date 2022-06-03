<template>
  <div class='nameDisplayWrapper'>
    <NavBurger :onClick='toggleNav'/>
    <router-link to='/'>
      <img :src="logo" alt='logo'/>
      <h3> Quizio </h3>
    </router-link>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue'
import logo from '../assets/logo.svg'
import NavBurger from '../assets/icons/NavBurger.vue'


export default defineComponent({
  data:function(){
    return {
      logo,
    }
  },
  components:{
    NavBurger
  },
  methods:{
    toggleNav(){
      this.$store.commit('nav/toggle_nav')
    }
  },
})

</script>


<style lang='scss' scoped>
.nameDisplayWrapper > a{
  display:flex;
  justify-content:flex-start;
  align-items:center;
  text-decoration:none;
  color:black;
}

@media screen and (max-width:700px){
  .nameDisplayWrapper{
    display:flex;
    justify-content:space-between;
    align-items:center;
    width:100%;
  }
}
</style>