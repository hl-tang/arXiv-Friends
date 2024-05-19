<script setup lang="ts">
import TopBar from "../components/TopBar.vue";

import { ref } from "vue";
const recommendPapers = ref([]);

import axios from 'axios'
axios.get('/api/recommend') //recommend/后面有slash会导致ninja api 404(如果@recommendation_api.get("/recommend")最后也没有slash的话 )
  .then(res => {
    console.log(res.data)
    recommendPapers.value = res.data
    console.log(recommendPapers.value)
  })
  .catch((err) => {
    console.log(err)
  })


</script>

<template>
  <TopBar />
  <!-- {{ recommendPapers }} template里不加.value -->
  <div class="pt-[70px]">



    <div class="grid justify-items-center space-y-6 ml-12">
      <!-- v-for显示10篇论文 -->
      <div v-for="paper in recommendPapers" :key="paper.paper_id" class="flex items-center space-x-3">
        <PaperRow :paper_id="paper.paper_id" :title_en="paper.title_en" :title_ja="paper.title_ja"
          :content_en="paper.content_en" :pdf_url="paper.pdf_url" :published="paper.published" :authors="paper.authors"
          :Categories="paper.categories" />



      </div>
    </div>
  </div>


</template>

<style scoped></style>