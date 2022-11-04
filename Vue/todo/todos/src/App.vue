<template>
  <h1>App 根组件</h1>
  <!--TODO 使用v-on接收todo-input的自定义事件，并用onAddNewTask方法来处理-->
  <todo-input/>
  <!--TODO 把todoList换成计算属性taskList-->
  <todo-list :list="todoList" class="mt-2"/>
  <todo-button v-model:active="activeBtnIndex"/>
</template>

<script>
export default {
  name: 'App',
}
</script>

<script setup>
import TodoList from "./components/todo-list/todo-list.vue"
import TodoInput from "./components/todo-input/todo-input.vue"
import TodoButton from "./components/todo-button/todo-button.vue";
import {computed} from "vue";

const todoList = $ref([
  {id: 1, task: "周一早晨9点开会", done: false},
  {id: 2, task: "周一晚上8点聚餐", done: false},
  {id: 3, task: "准备周三上午的演讲稿", done: true}
])

// TODO 把新的任务加到任务列表中
function onAddNewTask(taskName) {

}

let activeBtnIndex = $ref(0)

// TODO 根据activeBtnIndex的值，过滤todoList并显示在页面上
const taskList = computed(() => {
  switch (activeBtnIndex) {
    case 0:
      return // TODO
    case 1:
      return // TODO
    case 2:
      return // TODO
  }
})

</script>

<style lang="less" scoped>

</style>