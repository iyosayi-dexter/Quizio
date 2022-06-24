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
        component:()=> import('../views/Dashboard.vue')
    }
    ,
    {
        path:'/login',
        name:'Login',
        component:()=> import('../views/Login.vue')
    },
    {
        path:'/signup',
        name:'SignUp',
        component:()=> import('../views/SignUp.vue')
    },
    {
        path:'/messages',
        name:'Messages',
        component:()=> import('../views/Messages.vue')
    },
    {
        path:'/test',
        name:'Test',
        component:()=> import('../views/Test.vue')
    },
    {
        path:'/courses',
        name:'courses',
        component:()=> import('../views/Courses.vue')
    },
    {
        path:'/tests/:test',
        name:'Test-config',
        component:()=> import('../views/Test-config.vue')
    },
    {   path: '/leaderboard',
        name:'leaderboard',
        component:()=> import('../views/Leaderboard.vue')
    },
    {
        path:'/lessons/:slug',
        name:':lessson-detail',
        component:()=> import('../views/LessonDetail.vue')
    },
    {
        path:'/notfound',
        name:'notfound',
        component:()=> import('../views/NotFound.vue')
    },
    {
        path:'/lessons',
        name:'lessons',
        component:()=> import('../views/Lessons.vue')
    },
    {
        path: '/:pathMatch(.*)*',
        name: 'NotFound',
        component:()=> import('../views/NotFound.vue')
    }
]


const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router