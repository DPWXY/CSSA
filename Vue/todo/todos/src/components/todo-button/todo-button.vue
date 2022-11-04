<template>
  <div class="btn-container  mt-3">
    <div class="btn-group" role="group" aria-label="Basic example">
      <!--TODO 修改class属性，动态绑定btn-primary与btn-secondary类-->
      <button type="button" class="btn" :class="'btn-primary'" @click="">全部</button>
      <button type="button" class="btn" :class="'btn-secondary'" @click="">已完成</button>
      <button type="button" class="btn" :class="'btn-secondary'" @click="">未完成</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "TodoButton"
}
</script>

<script setup>
const props = defineProps({
  // 定义active属性，类型为数字，可选值为0 1 2，必填
  active: {
    type: Number,
    required: true,
    default: 0,
    validator(value) {
      return [0, 1, 2].includes(value)
    }
  }
})

// TODO 定义v-model的update事件
const emit = defineEmits([])

// TODO 定义按钮点击事件
function onBtnClick(index){

}

</script>

<style lang="less" scoped>
  .btn-container {
    width: 400px;
    text-align: center;
  }
</style>