import {createRouter, createWebHistory} from "vue-router";
import Home from "@/components/Home";
import ActorCreate from "@/components/ActorCreate";
import ActorDetail from "@/components/ActorDetail";
import ActorEdit from "@/components/ActorEdit";
import ActorsHome from "@/components/ActorsHome";
import FilmCreate from "@/components/FilmCreate";
import FilmDetail from "@/components/FilmDetail";
import FilmEdit from "@/components/FilmEdit";
import FilmsHome from "@/components/FilmsHome";

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
        path:'/actor_create',
        name:'actor_create',
        component: ActorCreate
    },
    {
        path:'/actor_detail/:actor_id',
        name:'actor_detail',
        component: ActorDetail,
        props:true
    },
    {
        path:'/actor_edit/:actor_id',
        name:'actor_edit',
        component: ActorEdit,
        props:true
    },
    {
        path:'/filmshome',
        name:'filmshome',
        component:FilmsHome
    },
    {
        path:'/film_create',
        name:'film_create',
        component: FilmCreate
    },
    {
        path:'/film_detail/:film_id',
        name:'film_detail',
        component: FilmDetail,
        props:true
    },
    {
        path:'/film_edit/:film_id',
        name:'film_edit',
        component: FilmEdit,
        props:true
    },
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router