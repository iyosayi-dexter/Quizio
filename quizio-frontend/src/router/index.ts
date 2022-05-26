import { createRouter , createWebHistory } from "vue-router";
import Home from '../views/Home.vue'


const routes = [
    {
        path:'/',
        name:'Home',
        component:Home
    },
    {
        path:'/dashboard',
        name:'Dashboard',
        component:()=> import ('../views/Dashboard.vue')
    }
    ,
    {
        path:'/login',
        name:'Login',
        component:()=> import ('../views/Login.vue')
    },
    {
        path:'/signup',
        name:'SignUp',
        component:()=> import ('../views/SignUp.vue')
    },
    {
        path:'/messages',
        name:'Messages',
        component:()=> import ('../views/Messages.vue')
    },
    {
        path:'/test',
        name:'Test',
        component:()=> import ('../views/Test.vue')
    },
    {
        path:'/tests',
        name:'Tests',
        component:()=> import ('../views/Tests.vue')
    },
    {
        path:'/test-config',
        name:'Test-config',
        component:()=> import ('../views/Test-config.vue')
    },
    {   path: '/404',
        alias:'*',
        component: ()=> import ('../views/NotFound.vue')
    },
    {
        path: '*',
        redirect: '/404'
    },
]


const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router