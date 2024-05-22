<script setup lang="ts">
import TopBar from "../components/TopBar.vue";
import PaperRow from "../components/PaperRow.vue";

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

import { useI18n } from 'vue-i18n'
const { t } = useI18n()

import { storeToRefs } from 'pinia'
import { useOmitAbstractStore } from '../stores/omitAbstract'
const { omitAbstract } = storeToRefs(useOmitAbstractStore())

</script>

<template>
  <TopBar />
  <div class="pt-[70px]">

    <div v-if="loading">
      <!-- <el-skeleton :rows="30" animated /> -->
      <v-skeleton-loader color="error" type="article"></v-skeleton-loader>
      <v-skeleton-loader color="error" type="article"></v-skeleton-loader>
      <div v-for="(item, index) in [1, 2, 3]" :key="index">
        <!-- <span>{{ index }}</span> -->
        <v-skeleton-loader color="error" type="article"></v-skeleton-loader>
      </div>
    </div>

    <div v-else class="items-center">
      <el-scrollbar height="800px" class="mt-2">
        <!-- fixed固定住，不会随着scrollなくなる -->
        <!-- space-y-6放着的话，mt mb都无效；  -->
        <div class="fixed flex flex-col justify-start mx-2">
          <div class="rounded w-[130px] h-[40px] flex items-center justify-center"
            :class="[isDark ? 'bg-neutral-700' : 'bg-neutral-200']">
            <span class="text-[15px] font-bold" :class="[isDark ? 'text-gray-200' : 'text-gray-700']">
              {{ t('searchResult') }}
            </span>
          </div>

          <div class="border w-[130px] h-[60px] mt-4 ring-2 hover:ring-4"
            :class="[isDark ? 'bg-neutral-700' : 'bg-neutral-200']">
            <div class="flex items-center justify-center">{{ t('abstract') }}</div>
            <el-switch v-model="omitAbstract" class="flex items-center justify-center px-0.5"
              style="--el-switch-on-color: #b91026; --el-switch-off-color: #c99898" :active-text="t('show')"
              :inactive-text="t('hide')" />
          </div>
        </div>

        <!-- <div class="flex justify-center"> 上下两个的区别好好体会，怎么居中，居中的是什么 -->
        <div class="grid justify-items-center space-y-6 ml-12">
          <!-- v-for显示10篇论文 -->
          <div v-for="paper in searchedPapers" :key="paper.paper_id" class="flex items-center space-x-3">
            <PaperRow :paper_id="paper.paper_id" :title_en="paper.title_en" :title_ja="paper.title_ja"
              :content_en="paper.content_en" :pdf_url="paper.pdf_url" :published="paper.published"
              :authors="paper.authors" :categories="paper.categories" />
          </div>
        </div>

      </el-scrollbar>

    </div>





  </div>

</template>

<style scoped></style>