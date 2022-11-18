<template>
  <table bor>
    <tr>
      <th v-for="k in ['id', 'task', 'done']">{{ k }}</th>
    </tr>
    <tr v-for="i in data">
      <!--TODO 把i传递出去给使用者使用-->
      <slot :item="i"></slot>
    </tr>
  </table>
</template>

<script setup>

// TODO 用defineProps来定义data属性
const props = defineProps(["data"])

console.log(Object.keys(props.data[0]))

</script>

<script>
export default {
  name: "MyTable"
}
</script>

<style scoped lang="less">
  table, table tr th, table tr td {
    border: 1px solid #0094ff;
    text-align: center; border-collapse: collapse;
  }
</style>