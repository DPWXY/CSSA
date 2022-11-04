<template>
  <el-row :gutter="20" justify="center">
    <el-col :span="2">
      <!--TODO 给点击事件绑定函数goBackHome函数-->
      <el-button type="primary" @click="goBackHome">回到主页</el-button>
    </el-col>
  </el-row>
  <el-divider/>
  <el-row :gutter="20" justify="center">
    <el-col :span="2">
      <!--TODO 处理click事件 更改currentTab的值-->
      <el-button type="primary" @click="currentTab = 'Movie'">电影</el-button>
    </el-col>
    <el-col :span="2">
      <!--TODO 处理click事件 更改currentTab的值-->
      <el-button type="primary" @click="currentTab = 'Music'">音乐</el-button>
    </el-col>
  </el-row>
  <el-divider/>
  <!--TODO 看一下下一行的原理-->
  <component :is="tabs[currentTab]"></component>
</template>

<script setup>
import Movie from "../components/movie.vue"
import Music from "../components/music.vue"
import {useRouter} from "vue-router"

// TODO 使用userRouter创建router变量
const router = useRouter()

function goBackHome() {
  // TODO 用router变量跳转到首页
  router.push("/")
}

let currentTab = $ref("Movie")
// TODO 定义tabs
const tabs = {
  "Movie": Movie,
  "Music": Music
}

</script>

<script>
export default {
  name: "Content2"
}
</script>

<style scoped lang="less">

</style>