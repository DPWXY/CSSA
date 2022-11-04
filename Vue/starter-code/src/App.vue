<template>
  <!--TODO 使用class-search组件-->
  <class-search></class-search>
  <!--TODO 使用header插槽-->
  <template #header>
    <p>123</p>
  </template>
  <!--TODO 使用默认插槽-->
  <template #default>
    <p>123</p>
  </template>
  <!--TODO 使用footer插槽-->
  <template #footer>
    <p>123</p>
  </template>
</template>

<script setup>
import ClassSearch from "./components/class-search.vue"

</script>

<script>
export default {
  name: "App"
}
</script>

<style scoped lang="less">

</style>