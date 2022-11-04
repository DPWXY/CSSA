<template>
  <the-header/>
  <el-row :gutter="20" justify="center">
    <el-col :span="2">
      <el-button type="primary" @click="goBackHome">回到主页</el-button>
    </el-col>
  </el-row>
  <el-divider/>
  <el-row :gutter="20" justify="center">
    <el-col :span="2">
      <el-button type="primary" @click="currentTab = 'Movie'">电影</el-button>
    </el-col>
    <el-col :span="2">
      <el-button type="primary" @click="currentTab = 'Music'">音乐</el-button>
    </el-col>
  </el-row>
  <el-divider/>
  <component :is="tabs[currentTab]"></component>
</template>

<script setup>
import Movie from "../components/movie.vue"
import Music from "../components/music.vue"
import {useRouter} from "vue-router"
import TheHeader from "../components/the-header.vue";


const router = useRouter()


function goBackHome() {
  router.push("/")
}

let currentTab = $ref("Movie")
const tabs = {
  Movie,
  Music
}

</script>

<script>
export default {
  name: "Content2"
}
</script>

<style scoped lang="less">

</style>