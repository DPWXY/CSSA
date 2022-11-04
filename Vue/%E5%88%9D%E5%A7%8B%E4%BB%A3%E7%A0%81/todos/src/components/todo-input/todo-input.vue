<template>
  <form class="form-inline" @submit.prevent="onFormSubmit">
    <div class="input-group mb-2 mr-sm-2">
      <div class="input-group-prepend">
        <div class="input-group-text">任务</div>
      </div>
      <input type="text" class="form-control" placeholder="请输入任务信息" style="width: 356px" v-model.trim="taskName">
    </div>
    <button type="submit" class="btn btn-primary mb-2">添加新任务</button>
  </form>
</template>

<script>
export default {
  name: "TodoInput"
}
</script>

<script setup>

// TODO 定义自定义事件
const emit = defineEmits([])

// TODO 定义taskName属性接受input的v-model数据

// TODO 定义“添加新任务”按钮的点击事件，记得需要触发自定义事件并向外传参
function onFormSubmit(){
  emit("", {taskName: taskName})
}

</script>

<style lang="less" scoped>

</style>