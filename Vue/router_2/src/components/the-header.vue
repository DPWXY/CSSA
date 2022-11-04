<template>
  <el-container>
    <el-header>
      <el-row :gutter="20" justify="center">
        <el-col :span="2">
          <router-link to="/">主页</router-link>
        </el-col>
        <el-col :span="2">
          <router-link to="/content1">内容1</router-link>
        </el-col>
        <el-col :span="2">
          <router-link to="/content2">内容2</router-link>
        </el-col>
        <el-col :span="2">
          <router-link to="/content3">内容3</router-link>
        </el-col>
        <el-divider/>

      </el-row>

    </el-header>
    <el-main>

    </el-main>
  </el-container>
</template>

<script setup>

</script>

<script>
export default {
  name: "TheHeader"
}
</script>

<style scoped lang="less">
  .router-link-active {
    background-color: red;
  }
</style>