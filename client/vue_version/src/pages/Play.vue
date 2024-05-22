<script setup lang="ts">
import { ref, watch, onMounted } from "vue";
const play = ref(1)
console.log(play.value);
play.value = 3
console.log(play.value);

// https://developer.mozilla.org/zh-CN/docs/Web/API/Window/localStorage
localStorage.setItem("myCat", "Tom");
let cat = localStorage.getItem("myCat");
console.log(cat);
localStorage.setItem("myCat", "Tom123");
console.log("ssdf", cat);
console.log("ssdf", localStorage.getItem("myCat"));


import { storeToRefs } from 'pinia'
import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { username } = storeToRefs(useIsLoggedInStore())
console.log(username.value);  // 导入pinia-plugin-persistedstate后，页面刷新还是"aaa"
username.value = "aaa";
console.log(username.value);

</script>

<template>
  play
  <div class="min-h-screen flex flex-col">
    <!-- 标题展示框 -->
    <header class="bg-gray-800 text-white p-4 text-center">
      <h1 class="text-2xl font-bold">标题展示框</h1>
    </header>

    <!-- 主内容区域 -->
    <div class="flex flex-1">
      <!-- 左半部分 -->
      <div class="w-2/3 bg-gray-200 p-4">
        <p class="text-lg">左半部分内容</p>
      </div>

      <!-- 右半部分 -->
      <div class="w-1/3 flex flex-col">
        <!-- 右上部分 -->
        <div class="flex-1 bg-gray-300 p-4">
          <p class="text-lg">右上部分内容</p>
        </div>
        <!-- 右下部分 -->
        <div class="flex-1 bg-gray-400 p-4">
          <!-- <p class="text-lg">右下部分内容</p> -->
          <v-textarea label="Input your notes here:" variant="outlined" v-model="notes"
            placeholder="Notes"></v-textarea>

          <button
            class="self-start bg-red-600 text-gray-300 font-semibold py-2 px-4 rounded-md hover:bg-red-700 hover:text-gray-100">
            Red Button with Gray Text
          </button>

          <el-button class="mt-4 " type="danger" plain>Danger</el-button>

          
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>