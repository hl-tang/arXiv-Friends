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
  <!-- {{ recommendPapers }} template里不加.value -->
  <div class="pt-[70px] items-center">
    <el-scrollbar height="850px" class="mt-2">
      <!-- fixed固定住，不会随着scrollなくなる -->
      <!-- space-y-6放着的话，mt mb都无效；  -->
      <div class="fixed flex flex-col justify-start m-6">
        <div class="rounded w-[155px] h-[40px] flex items-center justify-center"
          :class="[isDark ? 'bg-neutral-700' : 'bg-neutral-300']">
          <span class="text-[15px] font-bold" :class="[isDark ? 'text-gray-200' : 'text-gray-700']">
            {{ t('recommendForYou') }}
          </span>
        </div>

        <!-- <div class="border w-[130px] h-[60px] mt-4 ring-2 hover:ring-4"
          :class="[isDark ? 'bg-neutral-700' : 'bg-neutral-200']">
          <div class="flex items-center justify-center">{{ t('abstract') }}</div>
          <el-switch v-model="omitAbstract" class="flex items-center justify-center px-0.5 text-slate-200"
            style="--el-switch-on-color: #b91026; --el-switch-off-color: #c99898" :active-text="t('show')"
            :inactive-text="t('hide')" />
        </div> -->

        <div class="flex  items-center justify-center space-x-2">
          <v-switch v-model="omitAbstract" color="red-darken-3" label="" value="red-darken-3" hide-details></v-switch>
          <span>{{t('showAbstract')}}</span>
        </div>
      </div>

      <!-- <div class="flex justify-center"> 上下两个的区别好好体会，怎么居中，居中的是什么 -->
      <div class="grid justify-items-center space-y-6 ml-12">
        <!-- v-for显示10篇论文 -->
        <div v-for="paper in recommendPapers" :key="paper.paper_id" class="flex items-center space-x-3">
          <PaperRow :paper_id="paper.paper_id" :title_en="paper.title_en" :title_ja="paper.title_ja"
            :content_en="paper.content_en" :pdf_url="paper.pdf_url" :published="paper.published"
            :authors="paper.authors" :categories="paper.categories" />
        </div>
      </div>

    </el-scrollbar>

  </div>


</template>

<style scoped></style>