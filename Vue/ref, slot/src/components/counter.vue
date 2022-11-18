  <template>
  <div class="container">
    <h3>当前的计数值为：{{count}}</h3>
    <button @click="add">内部+1按钮</button>
  </div>

</template>

<script setup>
let count = $ref(0)

function add() {
  count++
}

function reset() {
  count = 0
}

// TODO 使用defineExpose来向外界暴露rest函数
defineExpose({reset})

</script>

<script>
export default {
  name: "Counter"
}
</script>

<style scoped lang="less">
  .container {
    border: 1px solid black;
    margin: 10px;
    padding: 10px;
  }
</style>