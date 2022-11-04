<template>
  <the-header/>
  <el-row :gutter="20" justify="center">
    <el-col :span="2">
      <router-link to="/content1/movie">电影</router-link>
    </el-col>
    <el-col :span="2">
      <router-link to="/content1/music">音乐</router-link>
    </el-col>
  </el-row>
  <el-divider/>
  <router-view/>
</template>

<script setup>
import TheHeader from "../components/the-header.vue";

</script>

<script>
export default {
  name: "Content1"
}
</script>

<style scoped lang="less">
  .router-link-active {
    background-color: deepskyblue;
  }

</style>