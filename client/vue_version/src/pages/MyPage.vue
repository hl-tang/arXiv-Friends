<script setup lang="ts">
import TopBar from "../components/TopBar.vue";
import PaperRow from "../components/PaperRow.vue";

import { ref } from 'vue';

import { storeToRefs } from 'pinia'
import { useIsLoggedInStore } from '../stores/isLoggedIn'
const { username } = storeToRefs(useIsLoggedInStore())

const currentTab = ref('favorites'); // 当前显示的标签页（'favorites' 或 'history'）

const likedPapers = ref([]);
import axios from 'axios';
axios.get('/api/like/')
  .then(res => {
    console.log("response data: ", res.data)
    likedPapers.value = res.data
    console.log("likedPapers: ", likedPapers.value);
  })
  .catch((err) => {
    console.log(err)
  })


</script>

<template>
  <TopBar />

  <div class="pt-[100px] 2xl:pl-[400px] lg:pl-[280px] lg:pr-0 pr-2 w-[calc(100%-90px)] max-w-[1800px] 2xl:mx-auto">
    <div class="flex w-[calc(100vw-230px)]">
      <img class="max-w-[100px]  max-h-[100px] rounded-full" src="../assets/default_avatar.png">

      <div class="ml-5 w-full">
        <div class="text-[30px] font-bold truncate">
          {{ username }}
        </div>
        <!-- <div class="text-[18px] truncate">email</div> -->
        <v-btn variant="tonal" class="mt-2">
          Edit Profile
        </v-btn>
      </div>
    </div>


    <!-- <div v-for="paper in likedPapers" :key="paper.paper_id" class="flex items-center space-x-3">
      <PaperRow :paper_id="paper.paper_id" :title_en="paper.title_en" :title_ja="paper.title_ja"
        :content_en="paper.content_en" :pdf_url="paper.pdf_url" :published="paper.published" :authors="paper.authors"
        :categories="paper.categories" />
    </div> -->

    <!-- <PaperRow author="ABCDEF" /> -->

    <div class="min-h-screen flex flex-col  p-4">
    <!-- User Info Section -->


    <!-- Tabs Section -->
    <div class="w-full max-w-md">
      <div class="flex justify-around border-b">
        <button @click="currentTab = 'favorites'"
          :class="currentTab === 'favorites' ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-600'"
          class="py-2 px-4 focus:outline-none">
          收藏
        </button>
        <button @click="currentTab = 'history'"
          :class="currentTab === 'history' ? 'border-b-2 border-blue-500 text-blue-500' : 'text-gray-600'"
          class="py-2 px-4 focus:outline-none">
          浏览历史
        </button>
      </div>

      <!-- Content Section -->
      <div class="mt-4">
        <div v-if="currentTab === 'favorites'">
          <!-- 收藏内容 -->
          <p>这里显示收藏的内容...</p>

          <div v-for="paper in likedPapers" :key="paper.paper_id" class="flex items-center space-x-3">
            <PaperRow :paper_id="paper.paper_id" :title_en="paper.title_en" :title_ja="paper.title_ja"
              :content_en="paper.content_en" :pdf_url="paper.pdf_url" :published="paper.published"
              :authors="paper.authors" :categories="paper.categories" />
          </div>

        </div>
        <div v-else-if="currentTab === 'history'">
          <!-- 浏览历史内容 -->
          <p>这里显示浏览历史的内容...</p>
        </div>
      </div>
    </div>
  </div>

  </div>

  
</template>

<style scoped></style>