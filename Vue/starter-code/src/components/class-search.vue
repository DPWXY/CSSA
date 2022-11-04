<template>
  <input type="text" v-model="className" placeholder="请输入要搜索的课程名称">
  <button @click="onClick">提交</button>
  <br>
  <br>
  <img :src="url" style="width: 300px" :hidden="imgHidden">

  <div style="background-color: gray">
    <!--TODO 建立名字为header的插槽-->
    <slot name="header"></slot>
  </div>
  <div style="font-family: 华文行楷,serif">
    <!--TODO 建立默认的插槽-->
    <slot name="default"></slot>
  </div>
  <div style="font-size: 5px; background-color: deepskyblue">
    <!--TODO 建立名字为footer的插槽-->
    <slot name="footer"></slot>
  </div>

</template>

<script setup>
import {inject} from "vue";

const className = $ref("")

// TODO 使用inject获取axios
const axios = inject("axios")
const response = await axios.post("/courses/DSC%2010", {responseType: "arraybuffer"})


let url = $ref("")
let imgHidden = $ref(true)

async function onClick() {
  // TODO 使用axios发送get请求到/courses/课程名称，记得把responseType设置为"arraybuffer"
  url = 'data:image/jpeg;base64,' + btoa(
      new Uint8Array(data).reduce((data, byte) => data +
          String.fromCh arCode(byte), '')
  )
  // TODO 变更图片显示状态
}
</script>

<script>
export default {
  name: "ClassSearch"
}
</script>

<style scoped lang="less">

</style>