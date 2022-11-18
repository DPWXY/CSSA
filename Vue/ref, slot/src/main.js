import {createApp} from 'vue'
import App from './App.vue'
import './index.css'

// TODO 首先把下行拆开赋值给app变量 记得mount需要是整个文件的最后一行
const app = createApp(App)

// TODO 自定义全局v-focus指令
app.directive("focus", el => el.focus())

app.mount('#app')

