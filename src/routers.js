import {createRouter, createWebHistory} from "vue-router";
import Home from "@/components/Home";
import Create from "@/components/Create";
import ActorDetail from "@/components/ActorDetail";
import ActorEdit from "@/components/ActorEdit";
import ActorsHome from "@/components/ActorsHome";
import MoviesHome from "@/components/FilmsHome"

const routes = [
    {
        path:'/',
        name:'Home',
        component:Home
    },
    {
        path:'/actorshome',
        name:'actorshome',
        component:ActorsHome
    },
    {
        path:'/movieshome',
        name:'movieshome',
        component:MoviesHome
    },
    {
        path:'/actor_create',
        name:'create',
        component: Create
    },
    {
        path:'/actor_detail/:actor_id',
        name:'detail',
        component: ActorDetail,
        props:true
    },
    {
        path:'/actor_edit/:actor_id',
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