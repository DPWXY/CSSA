import {createRouter, createWebHashHistory} from "vue-router";
import Home from "../views/home.vue"
import Music from "../components/music.vue";
import Content1 from "../views/content1.vue";
import Movie from "../components/movie.vue";
import Content2 from "../views/content2.vue";
import Content3 from "../views/content3.vue";
import Login from "../views/login.vue";

const routes = [
    {
        path: "/",
        component: Home,
        alias: "/home"
    },
    {
        path: "/content1",
        component: Content1,
        redirect: "/content1/movie",
        children: [
            {
                path: "movie",
                component: Movie
            },
            {
                path: "music",
                component: Music
            }
        ]
    },
    {
        path: "/content2",
        component: Content2
    },
    {
        path: "/content3",
        component: Content3
    },
    {
        path: "/login",
        component: Login
    }
]

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

const loginRequiredPages = [
    "/content1",
    "/content1/movie",
    "/content1/music",
    "/content2"
]

router.beforeEach(
    // TODO (to, from, next)=>{}
    (to, from, next)=>{
        if (loginRequiredPages.includes(to.path) && !localStorage.getItem("token")) {
            next({path: "/login", query: {destination: to.path}})
        } else{
            next()
        }
    }
)

export default router
