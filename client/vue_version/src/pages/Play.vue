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
console.log("ssdf",cat);
console.log("ssdf",localStorage.getItem("myCat"));


import { storeToRefs } from 'pinia'
import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { username } = storeToRefs(useIsLoggedInStore())
console.log(username.value);  // 导入pinia-plugin-persistedstate后，页面刷新还是"aaa"
username.value = "aaa";
console.log(username.value);

</script>

<template>
  play
</template>

<style scoped>
</style>