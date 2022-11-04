<template>
  <el-row :gutter="20" justify="center">
    <el-col :span="2">
      <!--TODO 给路由链接配上相应的路径-->
      <router-link to="/content1/movie">电影</router-link>
    </el-col>
    <el-col :span="2">
      <!--TODO 给路由链接配上相应的路径-->
      <router-link to="/content1/music">音乐</router-link>
    </el-col>
  </el-row>
  <el-divider/>

  <!--TODO 增加子路由视图-->
  <router-view></router-view>

</template>

<script setup>

</script>

<script>
export default {
  name: "Content1"
}
</script>

<style scoped lang="less">
  // TODO 让被选中链接背景颜色为red
  .router-link-active{
    background-color: deepskyblue;
  }
</style>