import {createRouter, createWebHistory} from "vue-router";
import Home from "@/components/Home";
import Create from "@/components/Create";
import ActorDetail from "@/components/ActorDetail";
import ActorEdit from "@/components/ActorEdit";

const routes = [
    {
        path:'/',
        name:'Home',
        component:Home
    },
    {
        path:'/create',
        name:'Create',
        component: Create
    },
    {
        path:'/detail/:actor_id',
        name:'detail',
        component: ActorDetail,
        props:true
    },
    {
        path:'/edit/:actor_id',
        name:'actoredit',
        component: ActorEdit,
        props:true
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router