<script setup lang="ts">
import TopBar from "../components/TopBar.vue";

import { ref, watch } from "vue";
const searchedPapers = ref([]);
const loading = ref(false)


import axios from 'axios';

const fetchSearchResults = async (searchContent) => {
  loading.value = true
  try {
    await axios.post('/api/arxiv', null, { // null作为请求体（body）占位符
      params: {
        search_content: searchContent //不是ref，不带.value
      }
    }).then(res => {
      loading.value = false
      // console.log("Response Data:", res.data)
      searchedPapers.value = res.data
      console.log(searchedPapers.value)
    });
  } catch (err) {
    console.error(err);
  }
};

// Watch route query changes to trigger search
import { useRoute } from 'vue-router';
const route = useRoute();
watch(
  () => route.query.search_content,
  (newSearchContent) => {
    if (newSearchContent) {
      fetchSearchResults(newSearchContent);
    }
  },
  { immediate: true }
);



import { useDark } from '@vueuse/core'
const isDark = useDark()

</script>

<template>
  <TopBar />
  <div class="pt-[70px]">

    <div v-show="loading">
      <el-skeleton :rows="30" animated />
    </div>

    <div class="grid justify-items-center space-y-6 ml-12">
      <!-- v-for显示10篇论文 -->
      <div v-for="paper in searchedPapers" :key="paper.paper_id" class="flex items-center space-x-3">
        <PaperRow :paper_id="paper.paper_id" :title_en="paper.title_en" :title_ja="paper.title_ja"
          :content_en="paper.content_en" :pdf_url="paper.pdf_url" :published="paper.published" :authors="paper.authors"
          :Categories="paper.categories" />
      </div>
    </div>

  </div>

</template>

<style scoped></style>