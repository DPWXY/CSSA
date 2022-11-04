<template>
  <el-container>
    <el-header>
      <el-row :gutter="20" justify="center">
        <el-col :span="2">
          <!--TODO 给路由链接配上相应的路径-->
          <router-link to="/home">主页</router-link>
        </el-col>
        <el-col :span="2">
          <!--TODO 给路由链接配上相应的路径-->
          <router-link to="/content1">内容1</router-link>
        </el-col>
        <el-col :span="2">
          <!--TODO 给路由链接配上相应的路径-->
          <router-link to="/content2">内容2</router-link>
        </el-col>
        <el-divider/>

      </el-row>

    </el-header>
    <el-main>

    </el-main>
  </el-container>

  <!--TODO 增添路由视图-->
  <router-view></router-view>

</template>

<script>
export default {
  name: 'App',
}
</script>
<style scoped lang="less">
  // TODO 让被选中链接背景颜色为red
  .router-link-active{
    background-color: red;
  }
</style>
