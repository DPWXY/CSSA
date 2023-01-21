<template>
  <!--<el-row class="mb-4">-->
  <!--  <el-button>Default</el-button>-->
  <!--  <el-button type="primary">Primary</el-button>-->
  <!--  <el-button type="success">Success</el-button>-->
  <!--  <el-button type="info">Info</el-button>-->
  <!--  <el-button type="warning">Warning</el-button>-->
  <!--  <el-button type="danger">Danger</el-button>-->
  <!--</el-row>-->
  <el-breadcrumb separator="/">
    <el-breadcrumb-item :to="{ path: '/' }">homepage</el-breadcrumb-item>
    <el-breadcrumb-item
      ><a href="/">promotion management</a></el-breadcrumb-item
    >
    <el-breadcrumb-item>promotion list</el-breadcrumb-item>
    <el-breadcrumb-item>promotion detail</el-breadcrumb-item>
  </el-breadcrumb>
  请使用移动设备打开此链接并刷新。
  <el-row :gutter="20">
    <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
    <el-col :span="6"><div class="grid-content ep-bg-purple" /></el-col>
  </el-row>
  <div class="common-layout">
    <el-container>
      <el-header>Header</el-header>
      <el-main>
        <el-button type="success">Success</el-button>
        <el-switch
          v-model="value"
          size="large"
          active-text="Open"
          inactive-text="Close"
        />

        <div>
          <span
            >I sit at my window this morning where the world like a passer-by stops
            for a moment, nods to me and goes.</span
          >
          <el-divider />
          <span
            >There little thoughts are the rustle of leaves; they have their whisper
            of joy in my mind.</span
          >
        </div>

        <div class="slider-demo-block">
          <el-slider v-model="value3" show-input />
        </div>

        <el-color-picker v-model="color" show-alpha />

        <el-button type="primary" style="margin-left: 16px" @click="drawer = true">
          open
        </el-button>

        <el-drawer v-model="drawer" title="I am the title" :with-header="false">
          <span>Hi there!</span>
        </el-drawer>

        <el-calendar v-model="value2" />
      </el-main>
    </el-container>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const value = ref(true)
const value2 = ref(new Date())
const value3 = ref(0)
const drawer = ref(false)
const color = ref('rgba(19, 206, 102, 0.8)')
</script>

<script>
export default {
  name: "Home"
}
</script>

<style scoped lang="less">
.el-row {
  margin-bottom: 20px;
}
.el-row:last-child {
  margin-bottom: 0;
}
.el-col {
  border-radius: 4px;
}

.grid-content {
  border-radius: 4px;
  min-height: 36px;
  background-color: blue;
}
.slider-demo-block {
  display: flex;
  align-items: center;
}
.slider-demo-block .el-slider {
  margin-top: 0;
  margin-left: 12px;
}
</style>