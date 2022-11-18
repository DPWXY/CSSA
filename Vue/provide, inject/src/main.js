import {createApp} from 'vue'
import App from './App.vue'
import './index.css'
import axios from "axios"

const app = createApp(App)


// TODO 设置默认网站前缀为https://api.ucsdcssa.com
 axios.defaults.baseURL = "https://api.ucsdcssa.com"

// TODO 使用provide注入axios
app.provide("axios", axios)

app.mount('#app')
