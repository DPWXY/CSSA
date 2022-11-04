<template>
  <el-form :model="form" label-width="120px">
    <el-form-item label="用户名">
      <el-input v-model="form.username" />
    </el-form-item>
    <el-form-item label="密码">
      <el-input
          v-model="form.password"
          type="password"
          placeholder="请输入密码"
          show-password
      />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">登录</el-button>
    </el-form-item>
  </el-form>

</template>

<script setup>
import {useRoute, useRouter} from "vue-router";

// TODO 用useRouter
const router = useRouter()

// TODO 用useRoute
const route = useRoute()

const form = $ref({
  username: "",
  password: ""
})

function onSubmit() {
  if (form.username === "lol" && form.password === "666" ) {
    // TODO 给localStorage设置token
    localStorage.setItem("token", "CN DOTA, BEST DOTA")
    // TODO 重定向至route里面destination
    router.replace(route.query.destination)


  } else {
    // TODO 提示密码不正确
    alert("用户名密码不正确")
  }
}
</script>

<script>
export default {
  name: "Login"
}
</script>

<style scoped lang="less">

</style>