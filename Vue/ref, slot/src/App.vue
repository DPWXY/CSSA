<template>
  <button @click="onClick">外部按钮重置按钮</button>
  <!--TODO 给下面的组件一个ref属性-->
  <counter ref="myComp"></counter>
  <!--TODO 把tableData作为属性传给my-table组件-->
  <my-table :data="tableData">
    <!--TODO 使用default插槽，用scope接受数据-->
    <template #default="scope">
      <!--TODO 添加3行td，里面的值用scope里面的值，其中最后一个td要用<input type="checkbox" :checked="true">的类型形式来实现。-->
      <td>{{scope.item.id}}</td>
      <td>{{scope.item.task}}</td>
      <td>
        <input type="checkbox" :checked="scope.item.done">
      </td>
    </template>
  </my-table>
  <!--TODO 在main.js中定义全局自定义指令v-focus-->
  <input type="text" v-focus>
  <!--TODO 在页面内定义自定义指令v-color-->
  <h2 v-color="'blue'">nice</h2>
</template>

<script setup>
import Counter from "./components/counter.vue";
import MyTable from "./components/my-table.vue";

// TODO 建立ref属性做对应的变量
let myComp = $ref(null)

function onClick(){
  // TODO 调用Counter组件里reset函数
  myComp.reset()
}

const tableData = [
  {id: 1, task: "周一早晨9点开会", done: false},
  {id: 2, task: "周一晚上8点聚餐", done: false},
  {id: 3, task: "准备周三上午的演讲稿", done: true}
]

// TODO 声明vColor自定义指令，记得其要接受参数哦！
// const vColor = {
//   mounted(el) {
//     el.focus()
//   },
//   updated(el) {
//     el.focus()
//   },
// }

// const vColor = el =>el.focus()

const vColor = (el, binding) => {
  el.style.color = binding.value
}

</script>

<script>
export default {
  name: "App"
}
</script>

<style scoped lang="less">

</style>