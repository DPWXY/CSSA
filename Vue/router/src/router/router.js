import {createRouter, createWebHashHistory} from "vue-router";
import Home from "../components/home.vue"
import Music from "../components/music.vue";
import Content1 from "../components/content1.vue";
import Movie from "../components/movie.vue";
import Content2 from "../components/content2.vue";

const routes =[
    // TODO 定义Home的路由
    {
        path:"/home",
        alias: "/",
        component: Home
    },
    // TODO 定义content1的路由
    {
        path: "/content1",  // TODO
        component: Content1,
        redirect: "/content1/movie",
        // TODO 设置重定向
        // TODO 定义content1的两个子路由movie和music
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
    // TODO 定义content2的路由
    {
        path: "/content2",
        component: Content2
    }

]

const router = createRouter({
    history: createWebHashHistory(),
    routes
}) // TODO 创建路由

export default router